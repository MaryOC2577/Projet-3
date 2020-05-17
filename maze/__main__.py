"""Main file."""
"""Main program in console mode."""

import os

from maze.model.classmymaze import MyMaze
from maze.model.classposition import Position

MAZE = MyMaze()
FINISH = "finish"


MAZE.display_maze()
print("\n")
print("Finish is in :", Position.ObjectPosition(FINISH), "position.")

print("Position des espaces vides :\n", MyMaze.checkspace())
print("Liste des murs :\n", MyMaze.checkwall())
