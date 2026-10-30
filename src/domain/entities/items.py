"""Предметы."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ItemType(Enum):
    FOOD = "FOOD"
    ELIXIR = "ELIXIR"
    SCROLL = "SCROLL"
    WEAPON = "WEAPON"
    TREASURE = "TREASURE"


class StatKind(Enum):
    MAX_HEALTH = "MAX_HEALTH"
    AGILITY = "AGILITY"
    STRENGTH = "STRENGTH"


class ItemSubtype(Enum):
    BREAD = "BREAD"      # еда
    APPLE = "APPLE"
    MEAT = "MEAT"
    DAGGER = "DAGGER"    # оружие
    SWORD = "SWORD"
    AXE = "AXE"
    MACE = "MACE"
    COINS = "COINS"      # сокровище


@dataclass
class Item:
    """Предмет; значимые поля зависят от типа."""

    type: ItemType
    subtype: ItemSubtype | None = None   # еда/оружие/сокровище
    stat: StatKind | None = None         # эликсир/свиток: что повышает
    health: int = 0                      # еда: восстанавливаемое HP
    max_health: int = 0                  # эликсир/свиток: прибавка макс. HP
    agility: int = 0                     # эликсир/свиток: прибавка ловкости
    strength: int = 0                    # эликсир/свиток/оружие: сила
    value: int = 0                       # сокровище: стоимость
    duration: int = 0                    # эликсир: длительность в ходах игрока
