"""Статистика одного прохождения."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RunStats:
    treasures: int = 0
    level: int = 1
    enemies_defeated: int = 0
    food_eaten: int = 0
    elixirs_drunk: int = 0
    scrolls_read: int = 0
    hits_dealt: int = 0      # нанесено ударов
    hits_missed: int = 0     # промахи игрока
    hits_taken: int = 0      # получено ударов
    cells_walked: int = 0
