"""Class MyMaze."""

from random import randint
from maze.config import LEVEL1
from maze.model.myhero import MyHero
from maze.model.item import Item


class MyMaze:
    """Create the maze."""

    def __init__(self):
        """Initialize objects."""
        self.paths = []
        self.walls = []
        self.items = []
        self.guardian = ()
        self.hero = MyHero(self)
        self.height = self.width = 0

        self.init_maze()
        self.set_items()

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
        items = [
            ("needle", "N"),
            ("tube", "T"),
            ("ether", "E"),
        ]
        position_blacklist = self.walls + [self.guardian, self.hero.position]
        for name, char in items:
            position = ()
            while position in position_blacklist or not position:
                position = (randint(0, self.width), randint(0, self.height))

            item = Item(name, char, position)
            self.items.append(item)
            position_blacklist.append(position)

    def check_inventory(self):
        """Check inventory."""
        if self.hero.position in self.items:
            # self.hero.position == self.items[0][2]
            # or self.hero.position == self.items[1][2]
            # or self.hero.position == self.items[2][2]
            self.hero.inventory.append("*")

    def check_guardian(self):
        """Inventory complete."""
        if self.hero.position == self.guardian:
            if self.hero.inventory == ["*", "*", "*"]:
                print("You win !")
                # Proposer une nouvelle partie ou quitter le jeu.

    def exit_maze(self):
        """Leave the maze."""

    def update(self, pressed_key):
        """Update hero postion."""
        self.hero.moves(pressed_key)
        self.check_inventory()
        print("Inventory :", self.hero.inventory)
        self.check_inventory()
