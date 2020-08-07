"""Class application."""

from maze.model.mymaze import MyMaze


class Software:
    """Holds the main loop."""

    def __init__(self, controller, view):
        """Initialize class software."""
        self.maze = MyMaze()
        self.view = view
        self.keys = controller

    def run_maze(self):
        """Maze loop."""
        while self.keys.pressed_key != "exit":
            self.view.display(self.maze)
            self.keys.check_keys()
            self.maze.update(self.keys.pressed_key, self.view)
