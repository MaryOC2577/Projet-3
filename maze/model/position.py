"""Class position."""

from maze.model.mymaze import MyMaze


class Position:
    """Calculate position."""

    def __init__(self):
        """Constructor."""

    def hero_position(self):
        """Hero position."""
        for line in range(0, 15):
            for char in range(0, 15):
                if MyMaze.current_mazetwo[line][char] == "H":
                    hero_position = (line, char)
                    return hero_position

    def tube_position(self):
        """Tube position."""
        for line in range(0, 15):
            for char in range(0, 15):
                if MyMaze.current_mazetwo[line][char] == "T":
                    tube_position = (line, char)
                    return tube_position

    def needle_position(self):
        """Needle position."""
        for line in range(0, 15):
            for char in range(0, 15):
                if MyMaze.current_mazetwo[line][char] == "N":
                    needle_position = (line, char)
                    return needle_position

    def ether_position(self):
        """Ether position."""
        for line in range(0, 15):
            for char in range(0, 15):
                if MyMaze.current_mazetwo[line][char] == "E":
                    ether_position = (line, char)
                    return ether_position
