"""CLI view."""

from maze.model.mymaze import MyMaze


class CliView:
    """View in console mode."""

    def display_maze(self):
        """Display the maze."""
        for line in range(0, 15):
            for char in range(0, 15):
                print(" ", MyMaze.current_maze[line][char], end="")
            print("\n")
