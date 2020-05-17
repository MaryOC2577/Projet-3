"""Class position."""

from maze.config import LEVEL1


class Position:
    """Calculate position."""

    def __init__(self):
        """Constructor."""

    def ObjectPosition(typeO):
        """Determine position of an object.
        S : start
        F : finish
        H : hero
        G : guardian
        N : needle
        T : tube
        E : ether
        """
        with open(LEVEL1, "r") as file:
            listfile = file.read().splitlines()

        for X in range(0, 15):
            for Y in range(0, 15):
                if typeO == "start" and listfile[X][Y] == "S":
                    return (X, Y)
                if typeO == "finish" and listfile[X][Y] == "F":
                    return (X, Y)
                if typeO == "hero" and listfile[X][Y] == "H":
                    return (X, Y)
                if typeO == "guardian" and listfile[X][Y] == "G":
                    return (X, Y)
                if typeO == "needle" and listfile[X][Y] == "N":
                    return (X, Y)
                if typeO == "tube" and listfile[X][Y] == "T":
                    return (X, Y)
                if typeO == "ether" and listfile[X][Y] == "E":
                    return (X, Y)
