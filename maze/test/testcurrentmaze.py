"""Record position test."""

from maze.config import LEVEL1
from maze.config import CURRENTMAZE


def record_maze():
    """Record current maze."""
    with LEVEL1.open("r") as file:
        content = file.read()

    with CURRENTMAZE.open("w") as file:
        file.write(content)
