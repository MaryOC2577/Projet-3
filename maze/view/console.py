"""CLI view."""
from maze.model.myhero import MyHero


class CliView:
    """View in console mode."""

    def __init__(self):
        """Initialized."""
        self.hero = MyHero()

    def display_maze(self, maze):
        """Display the maze."""
        for line in range(0, 15):
            for char in range(0, 15):
                if (line, char) == self.hero.position:
                    print(" ", "H", end="")
                else:
                    print(" ", maze[line][char], end="")
            print("\n")
