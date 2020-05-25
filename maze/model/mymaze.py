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
        # afficher position de tous les objets
        print("Hero is at :", hero_position)
        print("Guardian is at :", guardian_position)
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

    def checkwall():
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
        maze_paths = MyMaze.check_path()
        needle_possition = (randint(0, 13), randint(0, 13))
        while needle_possition not in maze_paths:
            needle_possition = (randint(0, 13), randint(0, 13))
        return needle_possition

    def init_objects(self):
        """Random position of :
        Needle = N
        Tube = T
        Ether = E
        """
        needle_position = (randint(0, 13), randint(0, 13))
        tube_position = (randint(0, 13), randint(0, 13))
        ether_position = (randint(0, 13), randint(0, 13))
        maze_paths = MyMaze.check_path()

        while needle_position and tube_position and ether_position not in maze_paths:
            needle_position = (randint(0, 13), randint(0, 13))
            tube_position = (randint(0, 13), randint(0, 13))
            ether_position = (randint(0, 13), randint(0, 13))

        return needle_position, tube_position, ether_position
