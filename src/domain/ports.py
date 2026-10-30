"""Порты: абстракции хранилищ, реализуемые в datalayer."""

from __future__ import annotations

from abc import ABC, abstractmethod

from domain.entities import GameSession, RunStats


class GameRepository(ABC):
    """Хранилище сохранённой игры."""

    @abstractmethod
    def save(self, session: GameSession) -> None:
        """Сохранить сессию целиком."""

    @abstractmethod
    def load(self) -> GameSession | None:
        """Загрузить сессию; None, если сохранения нет или файл повреждён."""

    @abstractmethod
    def exists(self) -> bool:
        """Есть ли сохранение."""

    @abstractmethod
    def clear(self) -> None:
        """Удалить сохранение."""


class StatisticsRepository(ABC):
    """Хранилище статистики прохождений."""

    @abstractmethod
    def add(self, stats: RunStats) -> None:
        """Добавить запись о прохождении."""

    @abstractmethod
    def all(self) -> list[RunStats]:
        """Все записи."""

    @abstractmethod
    def top(self, limit: int | None = None) -> list[RunStats]:
        """Лучшие записи: сокровища по убыванию, затем уровень по убыванию."""
