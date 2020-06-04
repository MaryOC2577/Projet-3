"""Class application."""

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
        self.view.display_maze(self.maze.current_maze)
        while self.keys.key_press != "exit":
            self.keys.check_keys()
            self.maze.hero.hero_moves(self.keys.key_press)
        print("Game over.")
