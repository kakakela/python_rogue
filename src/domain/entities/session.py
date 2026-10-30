"""Игровая сессия."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from domain.entities.character import Character
from domain.entities.level import Level
from domain.entities.stats import RunStats


class SessionStatus(Enum):
    PLAYING = "PLAYING"
    DEAD = "DEAD"
    VICTORY = "VICTORY"


@dataclass
class GameSession:
    level_number: int
    level: Level
    character: Character
    stats: RunStats = field(default_factory=RunStats)
    turn: int = 0
    status: SessionStatus = SessionStatus.PLAYING
    player_asleep: bool = False    # змей-маг усыпил: следующий ход пропускается

    @classmethod
    def new(cls, level_number: int, level: Level, character: Character) -> GameSession:
        """Новая сессия; статистика начинается с номера уровня."""
        return cls(level_number, level, character, RunStats(level=level_number))
