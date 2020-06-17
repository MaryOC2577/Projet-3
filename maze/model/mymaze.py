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
        self.tube = []
        self.needle = []
        self.ether = []
        self.guardian = ()
        self.finish = ()
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
                if char == "F":
                    self.finish = position
                if char in ["0", "H"]:
                    self.paths.append(position)
                elif char == "X":
                    self.walls.append(position)

            self.width = index_x
        self.height = index_y
        self.set_items()

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

        self.tube = ["tube", "T", tube_position]
        self.needle = ["needle", "N", needle_position]
        self.ether = ["ether", "E", ether_position]

    def check_inventory(self):
        """Check inventory."""
        if self.hero.position == self.tube[2] or self.needle[2] or self.ether[2]:
            self.hero.inventory.append("*")

    def exit_maze(self):
        """Leave the maze."""

    def update(self, pressed_key):
        """Update hero postion."""
        self.hero.moves(pressed_key)
        print("Inventory :", self.hero.inventoryù)
