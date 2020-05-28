"""Main file."""

from maze.model.mymaze import MyMaze
from maze.controller import console

MAZE = MyMaze()
CONTROLLER = console.Moves()
CONTROLLER.hero_move()
