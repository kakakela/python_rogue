"""Персонаж игрока и временные эффекты."""

from __future__ import annotations

from dataclasses import dataclass, field

from domain.constants import (
    PLAYER_START_AGILITY,
    PLAYER_START_HEALTH,
    PLAYER_START_STRENGTH,
)
from domain.entities.backpack import Backpack
from domain.entities.items import Item, StatKind
from domain.entities.position import Position


@dataclass
class Buff:
    """Временный эффект эликсира."""

    stat: StatKind
    amount: int
    turns_left: int


@dataclass
class Character:
    position: Position
    max_health: int
    health: int
    agility: int
    strength: int
    weapon: Item | None
    backpack: Backpack
    buffs: list[Buff] = field(default_factory=list)

    @classmethod
    def new(cls, position: Position) -> Character:
        """Новый персонаж со стартовыми характеристиками."""
        return cls(
            position=position,
            max_health=PLAYER_START_HEALTH,
            health=PLAYER_START_HEALTH,
            agility=PLAYER_START_AGILITY,
            strength=PLAYER_START_STRENGTH,
            weapon=None,
            backpack=Backpack(),
            buffs=[],
        )
