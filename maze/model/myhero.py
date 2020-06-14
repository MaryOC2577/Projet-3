"""Class Hero."""


class MyHero:
    """Create a hero."""

    def __init__(self):
        """Constructor Hero."""
        self.position = ()
        self.inventory = []

    def moves(self, move):
        """Hero moves."""
        next_case = ()
        if move == "left":
            next_case = (self.position[0], self.position[1] - 1)
        if move == "right":
            next_case = (self.position[0], self.position[1] + 1)
        if move == "up":
            next_case = (self.position[0] - 1, self.position[1])
        if move == "down":
            next_case = (self.position[0] + 1, self.position[1])
        return next_case
