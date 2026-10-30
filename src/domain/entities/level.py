"""Уровень: комнаты, коридоры, предметы, враги."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar

from domain.constants import MAP_HEIGHT, MAP_WIDTH
from domain.entities.enemy import Enemy
from domain.entities.items import Item
from domain.entities.position import Position


class CellType(Enum):
    VOID = "VOID"
    WALL = "WALL"
    FLOOR = "FLOOR"
    DOOR = "DOOR"
    CORRIDOR = "CORRIDOR"
    EXIT = "EXIT"


@dataclass
class Room:
    index: int                    # 0..8 = row*3 + col
    x: int
    y: int
    width: int                    # размеры включают стены
    height: int
    doors: list[Position] = field(default_factory=list)

    def interior(self) -> list[Position]:
        """Клетки пола (внутренность без стен)."""
        return [
            Position(px, py)
            for py in range(self.y + 1, self.y + self.height - 1)
            for px in range(self.x + 1, self.x + self.width - 1)
        ]

    def walls(self) -> list[Position]:
        """Клетки периметра (проёмы тоже входят)."""
        result: list[Position] = []
        for py in range(self.y, self.y + self.height):
            for px in range(self.x, self.x + self.width):
                on_edge = (px in (self.x, self.x + self.width - 1)
                           or py in (self.y, self.y + self.height - 1))
                if on_edge:
                    result.append(Position(px, py))
        return result

    def contains(self, p: Position) -> bool:
        """Точка в прямоугольнике комнаты, включая стены."""
        return (self.x <= p.x < self.x + self.width
                and self.y <= p.y < self.y + self.height)

    def interior_contains(self, p: Position) -> bool:
        """Точка строго внутри комнаты (на полу)."""
        return (self.x < p.x < self.x + self.width - 1
                and self.y < p.y < self.y + self.height - 1)


@dataclass
class Corridor:
    room_a: int
    room_b: int
    door_a: Position
    door_b: Position
    cells: list[Position] = field(default_factory=list)  # между проёмами, от a к b


@dataclass
class Level:
    WIDTH: ClassVar[int] = MAP_WIDTH
    HEIGHT: ClassVar[int] = MAP_HEIGHT

    number: int
    rooms: list[Room]
    corridors: list[Corridor]
    start_room: int
    exit_room: int
    exit_pos: Position
    items: dict[Position, Item] = field(default_factory=dict)
    enemies: list[Enemy] = field(default_factory=list)
    seen_rooms: set[int] = field(default_factory=set)
    explored: set[Position] = field(default_factory=set)
    # Индекс клеток; не участвует в сравнении и repr
    tiles: dict[Position, CellType] = field(
        default_factory=dict, compare=False, repr=False)

    def rebuild_index(self) -> None:
        """Пересчитать tiles из комнат, коридоров и выхода."""
        tiles: dict[Position, CellType] = {}
        for room in self.rooms:
            for p in room.walls():
                tiles[p] = CellType.WALL
            for p in room.interior():
                tiles[p] = CellType.FLOOR
            for p in room.doors:
                tiles[p] = CellType.DOOR
        for corridor in self.corridors:
            for p in corridor.cells:
                tiles[p] = CellType.CORRIDOR
        tiles[self.exit_pos] = CellType.EXIT
        self.tiles = tiles

    def cell_at(self, p: Position) -> CellType:
        """Тип клетки (VOID, если там ничего нет)."""
        return self.tiles.get(p, CellType.VOID)

    def is_walkable(self, p: Position) -> bool:
        """Можно ли встать на клетку."""
        return self.cell_at(p) in (
            CellType.FLOOR, CellType.DOOR, CellType.CORRIDOR, CellType.EXIT)

    def room_at(self, p: Position) -> Room | None:
        """Комната, в прямоугольник которой (со стенами) попадает точка."""
        for room in self.rooms:
            if room.contains(p):
                return room
        return None

    def enemy_at(self, p: Position) -> Enemy | None:
        """Враг в клетке p или None."""
        for enemy in self.enemies:
            if enemy.position == p:
                return enemy
        return None
