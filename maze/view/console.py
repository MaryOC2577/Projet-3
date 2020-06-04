"""CLI view."""


class CliView:
    """View in console mode."""

    def display_maze(self, maze):
        """Display the maze."""
        for line in range(0, 15):
            for char in range(0, 15):
                print(" ", maze[line][char], end="")
            print("\n")
