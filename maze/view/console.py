"""CLI view."""
from maze.model.mymaze import MyMaze


class CliView:
    """View in console mode."""

    def __init__(self):
        """Initialized."""
        self.maze = MyMaze()

    def display_maze(self):
        """Display the maze."""
        for x in range(15):
            for y in range(15):
                if (x, y) in self.maze.walls:
                    print(" ", "X", end="")
                if (x, y) in self.maze.paths:
                    if (x, y) == self.maze.tube:
                        print(" ", "T", end="")
                    if (x, y) == self.maze.needle:
                        print(" ", "N", end="")
                    if (x, y) == self.maze.ether:
                        print(" ", "E", end="")
                    if (x, y) == self.maze.guardian:
                        print(" ", "G", end="")
                    if (x, y) == self.maze.hero.position:
                        print(" ", "H", end="")
                    print(" ", "0", end="")
            print("\n")
