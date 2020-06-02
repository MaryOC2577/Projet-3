"""Class MyMaze."""

from random import randint
from maze.config import LEVEL1
from maze.model.myhero import MyHero


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

    def display_maze(self, current_maze):
        """Display the maze at current state."""
        for line in range(0, 15):
            for char in range(0, 15):
                print(" ", current_maze[line][char], end="")
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

    def init_needle(self):
        """Position of the needle."""
        needle_possition = ()
        while needle_possition not in self.check_path():
            needle_possition = (randint(0, 13), randint(0, 13))
        return needle_possition

    def init_tube(self):
        """Position of the tube."""
        tube_position = ()
        while tube_position not in self.check_path():
            tube_position = (randint(0, 13), randint(0, 13))
        return tube_position

    def init_ether(self):
        """Position of the ether."""
        ether_position = ()
        while ether_position not in self.check_path():
            ether_position = (randint(0, 13), randint(0, 13))
        return ether_position

    def set_items(self):
        """First position of all items."""
        temp_line = ""
        current_mazetwo = []
        for line in range(0, 15):
            for char in range(0, 15):
                if self.current_maze[line][char] == "S":
                    temp_line += "H"
                if line == 8 and char == 13:
                    temp_line += "G"
                else:
                    temp_line += self.current_maze[line][char]
            print("la temp line :", temp_line)
            current_mazetwo.append(temp_line)
            temp_line = ""
        self.current_maze = current_mazetwo
        print(self.current_maze)

    def load_maze(self):
        """Load the game."""
        self.set_walls()
        self.set_paths()
        self.set_items()
