"""Class MyMaze."""

from random import randint
from maze.config import LEVEL1
from maze.model.myhero import MyHero


class MyMaze:
    """Create the maze."""

    def __init__(self):
        """Constructor of MyMaze."""
        # Return position of the hero, always the same "START"
        hero = MyHero()
        hero_position = hero.init_hero()
        # Initial position of the guardian, always the same (8,13)
        guardian_position = (8, 13)
        # positions of tube, ether, needle.
        tube_position = self.init_tube()
        needle_position = self.init_needle()
        ether_position = self.init_ether()
        # afficher position de tous les objets
        print("Hero is at :", hero_position)
        print("Guardian is at :", guardian_position)
        print("Tube is at :", tube_position)
        print("Needle is at :", needle_position)
        print("Ether is at :", ether_position)
        print("¨Paths :", self.check_path())
        # display the maze

    def display_maze(self):
        """Display the maze with objects and caracters in current position"""
        with LEVEL1.open("r") as file:
            for line in file:
                for char in line:
                    print(" ", char, end="")

    def check_path(self):
        """Check empty space, return positions in a list."""
        with LEVEL1.open("r") as file:
            listfor = file.read().splitlines()
        list_path = []
        for nbline in range(0, 15):
            for nbchar in range(0, 15):
                if listfor[nbline][nbchar] == "0":
                    list_path.append((nbline, nbchar))
        return list_path

    def check_wall(self):
        """ liste contenant l'emplacement des murs."""
        with open(LEVEL1, "r") as file:
            listfor = file.read().splitlines()
        listofwall = []
        for nbline in range(0, 15):
            for nbchar in range(0, 15):
                if listfor[nbline][nbchar] == "X":
                    listofwall.append((nbline, nbchar))
        return listofwall

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
