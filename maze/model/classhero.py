"""Class Hero."""

from maze.config import CURRENTMAZE
from maze.config import LEVEL1


class MyHero:
    def __init__(self):
        """Constructor Hero."""

    def init_hero():
        """Initialized position of the Hero."""
        with open(LEVEL1, "r") as file:
            listfor = file.read().splitlines()
            listchange = ""
            listwrite = []
        for X in range(0, 15):
            for Y in range(0, 15):
                if listfor[X][Y] == "S":
                    listchange += listchange + "H"
                else:
                    listchange = listchange + listfor[X][Y]
            listwrite.append(listchange)
            listchange = ""

        with CURRENTMAZE.open("w") as file:
            for line in listwrite:
                file.writelines(line)
                file.writelines("\n")

