"""Config file."""
from pathlib import Path

BASE_DIR = Path(".").resolve()
MAZE_DIR = BASE_DIR / "maze"
DATA_DIR = MAZE_DIR / "data"
LEVEL1 = DATA_DIR / "maze1.txt"

with LEVEL1.open("r") as file:
    print(file.read())

