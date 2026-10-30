"""Противники."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from domain.entities.position import Direction, Position


class EnemyType(Enum):
    ZOMBIE = "ZOMBIE"
    VAMPIRE = "VAMPIRE"
    GHOST = "GHOST"
    OGRE = "OGRE"
    SNAKE_MAGE = "SNAKE_MAGE"


@dataclass
class Enemy:
    type: EnemyType
    position: Position
    health: int
    max_health: int
    agility: int
    strength: int
    hostility: int                          # радиус начала преследования
    room_index: int                         # комната, в которой «живёт»
    chasing: bool = False
    invisible: bool = False                 # привидение
    resting: bool = False                   # огр: пропускает ход после атаки
    counter_pending: bool = False           # огр: следующая атака точно попадёт
    first_hit_shield: bool = True           # вампир: первый удар игрока — промах
    move_dir: Direction | None = None       # змей-маг: текущая диагональ
