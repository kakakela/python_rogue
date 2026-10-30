"""Позиция на карте и направления движения."""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    """Направление; значение — (dx, dy)."""

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    UP_LEFT = (-1, -1)
    UP_RIGHT = (1, -1)
    DOWN_LEFT = (-1, 1)
    DOWN_RIGHT = (1, 1)

    @property
    def dx(self) -> int:
        return self.value[0]

    @property
    def dy(self) -> int:
        return self.value[1]


# Группы направлений (добавляются после создания Enum, чтобы не стать членами)
Direction.CARDINAL = (Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT)  # type: ignore[attr-defined]
Direction.DIAGONAL = (  # type: ignore[attr-defined]
    Direction.UP_LEFT, Direction.UP_RIGHT, Direction.DOWN_LEFT, Direction.DOWN_RIGHT,
)


@dataclass(frozen=True)
class Position:
    """Неизменяемая клетка карты."""

    x: int
    y: int

    def __add__(self, d: Direction) -> Position:
        """Сдвиг на направление."""
        return Position(self.x + d.dx, self.y + d.dy)

    def neighbors4(self) -> list[Position]:
        """Четыре соседние клетки (без диагоналей)."""
        return [self + d for d in Direction.CARDINAL]  # type: ignore[attr-defined]

    def neighbors8(self) -> list[Position]:
        """Восемь соседних клеток."""
        return [self + d for d in Direction]

    def chebyshev(self, o: Position) -> int:
        """Расстояние Чебышёва."""
        return max(abs(self.x - o.x), abs(self.y - o.y))

    def manhattan(self, o: Position) -> int:
        """Манхэттенское расстояние."""
        return abs(self.x - o.x) + abs(self.y - o.y)

    def euclid(self, o: Position) -> float:
        """Евклидово расстояние."""
        return math.hypot(self.x - o.x, self.y - o.y)
