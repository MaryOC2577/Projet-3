"""Class Hero."""


class MyHero:
    """Create a hero."""

    def __init__(self, maze):
        """Constructor Hero."""
        self.maze = maze
        self.position = ()
        self.inventory = []

    def moves(self, move):
        """Hero moves."""
        x, y = self.position
        if move == "left":
            new_position = x - 1, y
        if move == "right":
            new_position = x + 1, y
        if move == "up":
            new_position = x, y - 1
        if move == "down":
            new_position = x, y + 1
        if new_position not in self.maze.paths:
            return False
        self.position = new_position

