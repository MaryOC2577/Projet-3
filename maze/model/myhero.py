"""Class Hero."""

from maze.config import LEVEL1


class MyHero:
    def __init__(self):
        """Constructor Hero."""

    def init_hero(self):
        """Initialized position of the Hero."""
        with open(LEVEL1, "r") as file:
            listfor = file.read().splitlines()
        for X in range(0, 15):
            for Y in range(0, 15):
                if listfor[X][Y] == "S":
                    hero_position = (X, Y)
        return hero_position
