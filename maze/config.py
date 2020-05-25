"""Config file."""

from pathlib import Path

BASE_DIR = Path(".").resolve()
MAZE_DIR = BASE_DIR / "maze"
DATA_DIR = MAZE_DIR / "data"
LEVEL1 = DATA_DIR / "maze1.txt"
CURRENTMAZE = DATA_DIR / "currentmaze.txt"
