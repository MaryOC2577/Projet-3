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
        self.tube = ()
        self.needle = ()
        self.ether = ()
        self.guardian = (8, 13)
        self.current_maze = []
        self.init_file()
        self.hero = MyHero()
        self.load_maze()

    def init_file(self):
        """Load maze1.txt and save on current_maze."""
        with LEVEL1.open("r") as file:
            self.current_maze = file.read().splitlines()

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

    def load_maze(self):
        """Load the game."""
        self.set_walls()
        self.set_paths()
        self.set_items()

    def exit_maze(self):
        """Leave the maze."""

    def update(self, pressed_key):
        """Update hero postion."""
        new_position = self.hero.moves(pressed_key)
        if new_position in self.paths:
            self.hero.position = new_position
        elif new_position in self.walls:
            new_position = self.hero.position
        elif (
            new_position == self.tube
            or new_position == self.needle
            or new_position == self.ether
        ):
            self.hero.inventory.append("*")
            self.hero.position = new_position
        elif new_position == self.guardian:
            if self.hero.inventory == ["*", "*", "*"]:
                # class message le héros a gagné la partie
                # lancer méthode qui quitte le jeu
                print("Inventaire complet")
