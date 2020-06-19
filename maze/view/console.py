"""CLI view."""


class CliView:
    """View in console mode."""

    def __init__(self):
        """Initialized."""

    def display_maze(self, maze):
        """Display the maze."""
        for index_y in range(maze.height + 1):
            for index_x in range(maze.width + 1):
                position = (index_x, index_y)
                if position in maze.walls:
                    print(" ", "X", end="")
                elif position in maze.paths:
                    if position == maze.hero.position:
                        print(" ", "H", end="")
                    elif position == maze.items[0][2]:
                        print(" ", maze.items[0][1], end="")
                    elif position == maze.items[1][2]:
                        print(" ", maze.items[1][1], end="")
                    elif position == maze.items[2][2]:
                        print(" ", maze.items[2][1], end="")
                    else:
                        print(" ", "0", end="")
                elif position == maze.guardian:
                    print(" ", "G", end="")
                elif position == maze.finish:
                    print(" ", "F", end="")
            print("\n")
        print("self.maze.hero.position :", maze.hero.position)
