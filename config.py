from enum import Enum

class TimeUnit(Enum):
    WORKTIME = 0
    CHILLTIME = 1

PRESETS = {
    "25|5": (1500, 300),
    "30|10": (1800, 600),
    "45|15": (2700, 900)
}

DEFAULT_WINDOW_WIDTH = 250
DEFAULT_WINDOW_HEIGHT = 250