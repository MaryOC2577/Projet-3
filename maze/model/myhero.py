"""Class Hero."""


class MyHero:
    """Create a hero."""

    def __init__(self):
        """Constructor Hero."""
        self.position = (0, 0)
        self.inventory = []

    def moves(self, move):
        """Hero moves."""
        if move == "left":
            new_position = (self.position[0], self.position[1] - 1)
        if move == "right":
            new_position = (self.position[0], self.position[1] + 1)
        if move == "up":
            new_position = (self.position[0] - 1, self.position[1])
        if move == "down":
            new_position = (self.position[0] + 1, self.position[1])
        return new_position
