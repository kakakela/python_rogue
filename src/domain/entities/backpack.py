"""Рюкзак: по 9 предметов каждого типа и одна ячейка сокровищ."""

from __future__ import annotations

from dataclasses import dataclass, field

from domain.constants import MAX_PER_TYPE
from domain.entities.items import Item, ItemType

# Типы, которые лежат в рюкзаке списками (сокровища — отдельный счётчик)
STORED_TYPES = (ItemType.FOOD, ItemType.ELIXIR, ItemType.SCROLL, ItemType.WEAPON)


def _empty_items() -> dict[ItemType, list[Item]]:
    return {t: [] for t in STORED_TYPES}


@dataclass
class Backpack:
    items: dict[ItemType, list[Item]] = field(default_factory=_empty_items)
    treasure: int = 0

    def count(self, t: ItemType) -> int:
        """Сколько предметов типа t лежит в рюкзаке."""
        return len(self.items[t])

    def is_full(self, t: ItemType) -> bool:
        """Заполнен ли отсек типа t."""
        return self.count(t) >= MAX_PER_TYPE

    def add(self, item: Item) -> bool:
        """Положить предмет; False, если отсек полон. Сокровища суммируются."""
        if item.type == ItemType.TREASURE:
            self.treasure += item.value
            return True
        if self.is_full(item.type):
            return False
        self.items[item.type].append(item)
        return True

    def get(self, t: ItemType, index: int) -> Item:
        """Предмет по индексу (с 0), без извлечения."""
        return self.items[t][index]

    def pop(self, t: ItemType, index: int) -> Item:
        """Достать предмет из рюкзака."""
        return self.items[t].pop(index)

    def list(self, t: ItemType) -> list[Item]:
        """Список предметов типа t."""
        return self.items[t]
