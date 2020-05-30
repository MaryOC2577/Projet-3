"""Main file."""

from maze.model.mymaze import MyMaze
from maze.controller import console
from maze.model.position import Position

MAZE = MyMaze()
CONTROLLER = console.Moves()
POSITION = Position()

CONTROLLER.hero_move()
POSITION.hero_position()
