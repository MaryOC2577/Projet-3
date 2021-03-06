"""Config file."""

from pathlib import Path

BASE_DIR = Path(".").resolve()
MAZE_DIR = BASE_DIR / "maze"
DATA_DIR = MAZE_DIR / "data"
MODEL_DIR = MAZE_DIR / "model"
LEVEL1 = DATA_DIR / "maze1.txt"

IMG_DIR = DATA_DIR / "img"

SPRITE_SIZE = 32

FRAMES_PER_SECOND = 30

NUMBER_BOX = 15
