"""Class Hero."""

from maze.config import LEVEL1


class MyHero:
    """Create a hero."""

    def __init__(self):
        """Constructor Hero."""

    def init_hero(self):
        """Initialized position of the Hero."""
        with open(LEVEL1, "r") as file:
            listfor = file.read().splitlines()
        for line in range(0, 15):
            for char in range(0, 15):
                if listfor[line][char] == "S":
                    hero_position = (line, char)
        return hero_position
