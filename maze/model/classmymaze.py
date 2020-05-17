"""Class MyMaze."""

from maze.config import LEVEL1


class MyMaze:
    """Create the maze."""

    def __init__(self):
        """Constructor of MyMaze."""

    def display_maze(self):
        """Display the maze with objects and caracters in current position"""
        with LEVEL1.open("r") as file:
            for line in file:
                for char in line:
                    print(" ", char, end="")

    def init_maze(self):
        """Set the maze in start position."""
        # Check empty space = 0, return
        # position 3 objets tube = T, aiguille = N, ether = E
        # position héros, toujours meme position case départ
        # position gardien, le gardien se trouve toujours meme position

    def checkspace():
        """Check empty space, return positions in a list."""
        with open(LEVEL1, "r") as file:
            listfor = file.read().splitlines()
        listemptyspace = []
        for X in range(0, 15):
            for Y in range(0, 15):
                if listfor[X][Y] == "0":
                    listemptyspace.append((X, Y))
        return listemptyspace

    def checkwall():
        """ liste contenant l'emplacement des murs."""
        with open(LEVEL1, "r") as file:
            listfor = file.read().splitlines()
        listofwall = []
        for X in range(0, 15):
            for Y in range(0, 15):
                if listfor[X][Y] == "X":
                    listofwall.append((X, Y))
        return listofwall
