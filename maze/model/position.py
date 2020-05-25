"""Class position."""

from maze.config import CURRENTMAZE


class Position:
    """Calculate position."""

    def __init__(self):
        """Constructor."""

    def ObjectPosition(search_object):
        """Determine position of an object.
        S : start
        F : finish
        H : hero
        G : guardian
        N : needle
        T : tube
        E : ether
        """
        with open(CURRENTMAZE, "r") as file:
            listfile = file.read().splitlines()

        for X in range(0, 15):
            for Y in range(0, 15):
                if search_object == "start" and listfile[X][Y] == "S":
                    return (X, Y)
                if search_object == "finish" and listfile[X][Y] == "F":
                    return (X, Y)
                if search_object == "hero" and listfile[X][Y] == "H":
                    return (X, Y)
                if search_object == "guardian" and listfile[X][Y] == "G":
                    return (X, Y)
                if search_object == "needle" and listfile[X][Y] == "N":
                    return (X, Y)
                if search_object == "tube" and listfile[X][Y] == "T":
                    return (X, Y)
                if search_object == "ether" and listfile[X][Y] == "E":
                    return (X, Y)
