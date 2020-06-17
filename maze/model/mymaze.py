"""Class MyMaze."""

from random import randint
from maze.config import LEVEL1
from maze.model.myhero import MyHero


class MyMaze:
    """Create the maze."""

    def __init__(self):
        """Initialize objects."""
        self.paths = []
        self.walls = []
        self.tube = ()
        self.needle = ()
        self.ether = ()
        self.guardian = ()
        self.current_maze = []
        self.hero = MyHero(self)
        self.height = self.width = 0

        self.init_maze()

    def init_maze(self):
        """Initialization of the maze."""
        index_x = index_y = 0
        with LEVEL1.open("r") as file:
            content = file.readlines()

        for index_y, line in enumerate(content):
            for index_x, char in enumerate(line):
                position = (index_x, index_y)
                if char == "H":
                    self.hero.position = position
                if char == "G":
                    self.guardian = position
                if char in ["0", "H"]:
                    self.paths.append(position)
                elif char == "X":
                    self.walls.append(position)
            self.width = index_x
        self.height = index_y

    def set_items(self):
        """First position of all items."""
        tube_position = (14, 14)
        needle_position = (14, 13)
        ether_position = (14, 12)
        while tube_position and needle_position and ether_position not in self.paths:
            while tube_position and needle_position and ether_position in self.walls:
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

        self.tube = tube_position
        self.needle = needle_position
        self.ether = ether_position

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

    def exit_maze(self):
        """Leave the maze."""

    def update(self, pressed_key):
        """Update hero postion."""
        self.hero.moves(pressed_key)
