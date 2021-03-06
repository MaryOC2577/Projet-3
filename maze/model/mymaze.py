"""Class MyMaze."""

from os import sys
from random import randint
from maze.config import LEVEL1
from maze.model.myhero import MyHero
from maze.model.item import Item
from maze.model.message import messages


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
        self.messages = messages

        self.init_maze()
        self.set_items()

    def init_maze(self):
        """Initialize of the maze."""
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
                if char in ["0", "H", "G"]:
                    self.paths.append(position)
                elif char == "X":
                    self.walls.append(position)

            self.width = index_x
        self.height = index_y

    def set_items(self):
        """First position of all items."""
        items = [
            ("needle", "n"),
            ("tube", "t"),
            ("ether", "e"),
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
        items_positions = [item.position for item in self.items]
        items_name = [item.name for item in self.items]
        if self.hero.position in items_positions:
            self.hero.inventory.append("*")
            self.messages.set_message(
                "Hero pick the "
                + items_name[items_positions.index(self.hero.position)]
                + ".",
            )
            del self.items[items_positions.index(self.hero.position)]

    def check_guardian(self, view):
        """Inventory complete."""
        if self.hero.position == self.guardian:
            if self.hero.inventory == ["*", "*", "*"]:
                self.messages.set_message("You win !")
            else:
                self.messages.set_message("You loose !")
            self.exit_maze(view)

    def exit_maze(self, view):
        """Leave the maze."""
        view.exit(self)
        sys.exit()

    def update(self, pressed_key, view):
        """Update hero postion."""
        self.hero.moves(pressed_key)
        self.check_inventory()
        self.check_guardian(view)
