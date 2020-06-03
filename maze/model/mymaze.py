"""Class MyMaze."""

from random import randint
from maze.config import LEVEL1


class MyMaze:
    """Create the maze."""

    def __init__(self):
        """Initialize the maze, objects."""
        self.paths = []
        self.walls = []
        self.current_maze = []
        self.init_file()
        self.load_maze()

    def init_file(self):
        """Load maze1.txt and save on current_maze."""
        with LEVEL1.open("r") as file:
            self.current_maze = file.read().splitlines()

    def display_maze(self):
        """Display the maze at current state."""
        for line in range(0, 15):
            for char in range(0, 15):
                print(" ", self.current_maze[line][char], end="")
            print("\n")

    def set_paths(self):
        """Check empty space, return positions in a list."""
        for line in range(0, 15):
            for char in range(0, 15):
                if self.current_maze[line][char] == "0":
                    self.paths.append((line, char))

    def set_walls(self):
        """Content walls positions."""
        for line in range(0, 15):
            for char in range(0, 15):
                if self.current_maze[line][char] == "X":
                    self.walls.append((line, char))

    def set_items(self):
        """First position of all items."""
        tube_position = (-1, -1)
        needle_position = (-2, -2)
        ether_position = (-3, -3)
        while tube_position and needle_position and ether_position not in self.paths:
            tube_position = (randint(1, 13), randint(1, 13))
            needle_position = (randint(1, 13), randint(1, 13))
            ether_position = (randint(1, 13), randint(1, 13))
        if tube_position == needle_position:
            tube_position = (randint(1, 13), randint(1, 13))
            needle_position = (randint(1, 13), randint(1, 13))
        elif needle_position == ether_position:
            needle_position = (randint(1, 13), randint(1, 13))
            ether_position = (randint(1, 13), randint(1, 13))
        elif ether_position == tube_position:
            ether_position = (randint(1, 13), randint(1, 13))
            tube_position = (randint(1, 13), randint(1, 13))

        temp_line = ""
        current_mazetwo = []
        for line in range(0, 15):
            for char in range(0, 15):
                if self.current_maze[line][char] == "S":
                    temp_line += "H"
                elif line == 8 and char == 13:
                    temp_line += "G"
                elif line == tube_position[0] and char == tube_position[1]:
                    temp_line += "T"
                elif line == needle_position[0] and char == needle_position[1]:
                    temp_line += "N"
                elif line == ether_position[0] and char == ether_position[1]:
                    temp_line += "E"
                else:
                    temp_line += self.current_maze[line][char]
            current_mazetwo.append(temp_line)
            temp_line = ""
        self.current_maze = current_mazetwo

    def load_maze(self):
        """Load the game."""
        self.set_walls()
        self.set_paths()
        self.set_items()
        self.display_maze()
