"""Class application."""
from os import system
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
        while self.keys.pressed_key != "exit":
            system("cls")
            self.maze.update(self.keys.pressed_key)
            self.keys.check_keys()
            self.view.display(self.maze)

        print("Game over.")
