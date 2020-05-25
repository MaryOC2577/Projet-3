"""Class MyMaze."""

from random import randint
from maze.config import LEVEL1
from maze.config import CURRENTMAZE
from maze.model.classhero import MyHero


class MyMaze:
    """Create the maze."""

    def __init__(self):
        """Constructor of MyMaze."""

    def display_maze(self):
        """Display the maze with objects and caracters in current position"""
        with CURRENTMAZE.open("r") as file:
            for line in file:
                for char in line:
                    print(" ", char, end="")

    def init_maze():
        """Set the maze in start position."""
        # Initial position of the hero, always the same "START"
        MyHero.init_hero()
        # Initial position of the guardian, always the same (8,13)
        MyMaze.init_guardian()
        # position 3 objets tube = T, aiguille = N, ether = E
        MyMaze.init_objects()
        MyMaze.display_maze()

    def checkspace():
        """Check empty space, return positions in a list."""
        with open(CURRENTMAZE, "r") as file:
            listfor = file.read().splitlines()
        listemptyspace = []
        for nbline in range(0, 15):
            for nbchar in range(0, 15):
                if listfor[nbline][nbchar] == "0":
                    listemptyspace.append((nbline, nbchar))
        return listemptyspace

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

    def init_guardian():
        """Guardian position initialization.
        Position is (8,13)
        """
        with CURRENTMAZE.open("r") as file:
            listfor = file.read().splitlines()
        listchange = ""
        listwrite = []
        for nbline in range(0, 15):
            for nbchar in range(0, 15):
                if nbline == 8 and nbchar == 13:
                    listchange = listchange + "G"
                else:
                    listchange = listchange + listfor[nbline][nbchar]
            listwrite.append(listchange)
            listchange = ""

        with CURRENTMAZE.open("w") as file:
            for line in listwrite:
                file.writelines(line)
                file.writelines("\n")

    def init_objects():
        """Random position of :
        Needle = N
        Tube = T
        Ether = E
        """
        needle_position = (randint(0, 13), randint(0, 13))
        tube_position = (randint(0, 13), randint(0, 13))
        ether_position = (randint(0, 13), randint(0, 13))
        empty_space = MyMaze.checkspace()

        while needle_position and tube_position and ether_position not in empty_space:
            needle_position = (randint(0, 13), randint(0, 13))
            tube_position = (randint(0, 13), randint(0, 13))
            ether_position = (randint(0, 13), randint(0, 13))

        # print("Needle :", needle_position)
        # print("Tube :", tube_position)
        # print("Ether :", ether_position)

        with CURRENTMAZE.open("r") as file:
            listfor = file.read().splitlines()
        listchange = ""
        listwrite = []
        for nbline in range(0, 15):
            for nbchar in range(0, 15):
                if nbline == needle_position[0] and nbchar == needle_position[1]:
                    listchange = listchange + "N"
                elif nbline == tube_position[0] and nbchar == tube_position[1]:
                    listchange = listchange + "T"
                elif nbline == ether_position[0] and nbchar == ether_position[1]:
                    listchange = listchange + "E"
                else:
                    listchange = listchange + listfor[nbline][nbchar]

            listwrite.append(listchange)
            listchange = ""

        with CURRENTMAZE.open("w") as file:
            for line in listwrite:
                file.writelines(line)
                file.writelines("\n")
