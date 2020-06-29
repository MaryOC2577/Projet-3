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
                    items_positions = [item.position for item in maze.items]
                    items_char = [item.char for item in maze.items]
                    if position in maze.guardian:
                        print(" ", "G", end="")
                    elif position == maze.hero.position:
                        print(" ", "H", end="")
                    elif position in items_positions:
                        print(" ", items_char[items_positions.index(position)], end="")
                    else:
                        print(" ", "0", end="")
            print("\n")
