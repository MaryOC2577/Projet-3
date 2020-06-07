"""Class Hero."""


class MyHero:
    """Create a hero."""

    def __init__(self):
        """Constructor Hero."""
        self.hero_position = ()
        self.inventory = []

    def hero_moves(self, move, position):
        """Hero moves."""
        next_case = ()
        if move == "left":
            print("Hero goes left.")
            next_case = (position[0], position[1] - 1)
        if move == "right":
            print("Hero goes right.")
            next_case = (position[0], position[1] + 1)
        if move == "up":
            print("Hero goes up.")
            next_case = (position[0] - 1, position[1])
        if move == "down":
            print("Hero goes down.")
            next_case = (position[0] + 1, position[1])
        print("Next case is :", next_case)
        return next_case
