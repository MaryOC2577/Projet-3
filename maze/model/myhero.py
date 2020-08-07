"""Class Hero."""

from maze.model.message import messages


class MyHero:
    """Create a hero."""

    def __init__(self, maze):
        """Constructor Hero."""
        self.maze = maze
        self.position = ()
        self.inventory = []

    def moves(self, move):
        """Hero moves."""
        new_position = ()
        pos_x, pos_y = self.position
        if move == "left":
            new_position = pos_x - 1, pos_y
        if move == "right":
            new_position = pos_x + 1, pos_y
        if move == "up":
            new_position = pos_x, pos_y - 1
        if move == "down":
            new_position = pos_x, pos_y + 1
        if new_position not in self.maze.paths:
            if new_position in self.maze.walls:
                messages.set_message("Hero can't move in a wall !")
            return False
        self.position = new_position
        return True
