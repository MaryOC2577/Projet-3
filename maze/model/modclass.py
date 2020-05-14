"""Content all class."""

from pathlib import Path

BASE_DIR = Path(".").resolve()
MAZE_DIR = BASE_DIR / "maze"
DATA_DIR = MAZE_DIR / "data"


class MyMaze:
    """Create the maze."""

    def __init__(self):
        self.mazefile = DATA_DIR / "maze1.txt"
        self.emptyspace = ()

    def displaymaze(self):
        """Display the maze with objects and caracters in current position"""
        listf = []
        with open(self.mazefile, "r") as file:
            listf = file.read()
        counter = 0
        print("  ", end="")
        for x in range(0, 239):
            if counter == 14:
                print("\n")
                print(" ", listf[x], " ", end="")
                counter += 1
            else:
                print(listf[x], " ", end="")
        print("\n")

    def setmaze(self):
        """Set the maze in start position."""
        # Check empty space = 0, return
        # position 3 objets tube = T, aiguille = N, ether = E
        # position héros, toujours meme position case départ
        # position gardien, le gardien se trouve toujours meme position

    def checkspace(self):
        """Check empty space, return positions in a list."""
        with open(self.mazefile, "r") as file:
            content = file.read()
