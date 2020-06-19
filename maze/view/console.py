"""CLI view."""
from maze.model.mymaze import MyMaze


class CliView:
    """View in console mode."""

    def __init__(self):
        """Initialized."""
        self.maze = MyMaze()

    def display_maze(self):
        """Display the maze."""
        for index_y in range(self.maze.height + 1):
            for index_x in range(self.maze.width + 1):
                position = (index_x, index_y)
                if position in self.maze.walls:
                    print(" ", "X", end="")
                elif position in self.maze.paths:
                    if position == self.maze.hero.position:
                        print(" ", "H", end="")
                    elif position == self.maze.items[0][2]:
                        print(" ", self.maze.items[0][1], end="")
                    elif position == self.maze.items[1][2]:
                        print(" ", self.maze.items[1][1], end="")
                    elif position == self.maze.items[2][2]:
                        print(" ", self.maze.items[2][1], end="")
                    else:
                        print(" ", "0", end="")
                elif position == self.maze.guardian:
                    print(" ", "G", end="")
                elif position == self.maze.finish:
                    print(" ", "F", end="")
            print("\n")
        print("self.maze.hero.position :", self.maze.hero.position)
