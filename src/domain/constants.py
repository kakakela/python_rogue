"""Все числовые константы баланса и размеров игры."""

# --- Размеры карты ---------------------------------------------------------
REGION_WIDTH = 26          # ширина секции (карта делится на 3x3 секции)
REGION_HEIGHT = 9          # высота секции
MAP_WIDTH = 3 * REGION_WIDTH     # 78
MAP_HEIGHT = 3 * REGION_HEIGHT   # 27
ROOMS_COUNT = 9
ROOM_MIN_WIDTH = 6         # размеры комнаты включают стены
ROOM_MAX_WIDTH = 24
ROOM_MIN_HEIGHT = 5
ROOM_MAX_HEIGHT = 7
MAX_EXTRA_CORRIDORS = 3    # дополнительные рёбра сверх остовного дерева
MAX_GENERATION_ATTEMPTS = 50

# --- Терминал --------------------------------------------------------------
MIN_TERMINAL_H = 34
MIN_TERMINAL_W = 80
LOG_LINES = 4

# --- Уровни ----------------------------------------------------------------
LEVEL_COUNT = 21

# --- Рюкзак ----------------------------------------------------------------
MAX_PER_TYPE = 9

# --- Видимость -------------------------------------------------------------
VIEW_RADIUS = 12
RAY_ANGLE_STEP_DEG = 2     # шаг угла лучей Ray Casting (в градусах)

# --- Игрок -----------------------------------------------------------------
PLAYER_START_HEALTH = 100
PLAYER_START_AGILITY = 60
PLAYER_START_STRENGTH = 60

# --- Бой -------------------------------------------------------------------
HIT_BASE = 70              # базовый шанс попадания, %
HIT_AGI_FACTOR = 0.3       # вклад разницы ловкости
HIT_MIN = 15
HIT_MAX = 95
DAMAGE_STR_FACTOR = 0.4

# --- Лут -------------------------------------------------------------------
LOOT_BASE_PER_STAT = 1.0
LOOT_HOSTILITY_FACTOR = 2.0
LOOT_LEVEL_BONUS = 0.1

# --- Особые эффекты врагов -------------------------------------------------
SLEEP_CHANCE = 0.15        # змей-маг: шанс усыпить игрока
VAMPIRE_DRAIN = 5          # вампир: уменьшение макс. HP за укус
GHOST_TELEPORT_P = 0.25    # привидение: шанс телепорта за ход
GHOST_INVISIBLE_P = 0.3    # привидение: шанс сменить невидимость за ход
OGRE_MOVE_STEPS = 2        # огр: клеток за ход

# --- Враги: базовые статы; ключ — имя EnemyType (чтобы избежать цикла импорта)
ENEMY_BASE_STATS: dict[str, dict[str, int]] = {
    "ZOMBIE": {"health": 100, "agility": 30, "strength": 50, "hostility": 4},
    "VAMPIRE": {"health": 100, "agility": 70, "strength": 50, "hostility": 6},
    "GHOST": {"health": 40, "agility": 70, "strength": 25, "hostility": 2},
    "OGRE": {"health": 140, "agility": 30, "strength": 90, "hostility": 4},
    "SNAKE_MAGE": {"health": 70, "agility": 90, "strength": 40, "hostility": 6},
}

# --- Сложность -------------------------------------------------------------
STAT_SCALE_PER_LEVEL = 0.04      # рост статов врагов за уровень
ENEMIES_PER_ROOM_STEP = 6        # +1 враг в комнате каждые N уровней
ENEMIES_PER_ROOM_CAP = 4
ENEMY_ROOM_PROB_START = 0.5
ENEMY_ROOM_PROB_END = 0.9
ITEMS_PER_ROOM_START = 3
ITEMS_PER_ROOM_STEP = 7          # -1 предмет в комнате каждые N уровней
ITEMS_PER_ROOM_MIN = 1
ITEM_ROOM_PROB_START = 0.8
ITEM_ROOM_PROB_END = 0.35

# --- Диапазоны характеристик предметов -------------------------------------
FOOD_HEALTH_RANGE = (15, 40)
ELIXIR_STAT_RANGE = (5, 15)          # ловкость / сила
ELIXIR_MAX_HEALTH_RANGE = (10, 25)
ELIXIR_DURATION_RANGE = (20, 40)     # ходов игрока
SCROLL_STAT_RANGE = (3, 8)           # ловкость / сила
SCROLL_MAX_HEALTH_RANGE = (5, 12)
WEAPON_STRENGTH_RANGE = (8, 30)
WEAPON_STRENGTH_BY_SUBTYPE = {       # кинжал < меч < топор < булава
    "DAGGER": 8,
    "SWORD": 14,
    "AXE": 22,
    "MACE": 30,
}
