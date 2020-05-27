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
        # afficher les positions des objets
        print(hero_position)
        print(guardian_position)
        print(tube_position)
        print(needle_position)
        print(ether_position)
        # Init the maze
        self.display_maze()

    def start_maze(
        self,
        hero_position,
        guardian_position,
        tube_position,
        needle_position,
        ether_position,
    ):
        """Initialization of the maze."""
        current_maze = []
        with LEVEL1.open("r") as file:
            current_maze = file.read().splitlines()
            current_line = ""
            current_mazetwo = []
            for line in range(0, 15):
                for char in range(0, 15):
                    if line == hero_position[0] and char == hero_position[1]:
                        current_maze += "H"
                    if line == guardian_position[0] and char == guardian_position[1]:
                        current_line += "G"
                    if line == tube_position[0] and char == tube_position[1]:
                        current_line += "T"
                    if line == needle_position[0] and char == needle_position[1]:
                        current_maze += "N"
                    if line == ether_position[0] and char == ether_position[1]:
                        current_line += "E"
                    else:
                        current_line += current_maze[line][char]
                current_mazetwo.append(current_line)
        return current_mazetwo

    def display_maze(self):
        """Display the maze at current state."""
        with LEVEL1.open("r") as file:
            current_maze = file.read().splitlines()
        for line in range(0, 15):
            for char in range(0, 15):
                print(" ", current_maze[line][char], end="")
            print("\n")

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
