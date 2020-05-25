"""Main file."""
import keyboard
from maze.model.classmymaze import MyMaze
from maze.model.classhero import MyHero
from maze.model.classposition import Position

MAZE = MyMaze()
MyHero.init_hero()
MyMaze.init_guardian()
MyMaze.init_objects()
MAZE.display_maze()
