"""Class application."""

from maze.model.mymaze import MyMaze
from maze.view.console import CliView


class Software:
    """Holds the main loop."""

    def __init__(self):
        """Initialized software."""
        self.maze = MyMaze()
        self.view = CliView()

    def run_maze(self):
        """Main loop of the maze."""
        # tant que le joueur n'appuie pas sur la touche echap, le jeu continue.
        self.view.display_maze(self.maze.current_maze)
