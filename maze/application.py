"""Class application."""
import os
from maze.model.mymaze import MyMaze
from maze.view.console import CliView
from maze.controller.console import InputKeys


class Software:
    """Holds the main loop."""

    def __init__(self):
        """Initialized software."""
        self.maze = MyMaze()
        self.view = CliView()
        self.keys = InputKeys()

    def run_maze(self):
        """Main loop of the maze."""
        # tant que le joueur n'appuie pas sur la touche e le jeu continue.
        self.view.display_maze()
        while self.keys.pressed_key != "exit":
            self.keys.check_keys()
            os.system("cls")
            self.maze.update(self.keys.pressed_key)
            self.view.display_maze()
        print("Game over.")
