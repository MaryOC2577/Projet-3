"""Class application."""

from maze.model.mymaze import MyMaze


# from maze.view.pygame import PyGameView

# from maze.controller.pygame import InputKeys

# from maze.view.console import CliView
# from maze.controller.console import InputKeys


class Software:
    """Holds the main loop."""

    def __init__(self, controller, view):
        """Initialized software."""
        self.maze = MyMaze()
        self.view = view
        self.keys = controller

    def run_maze(self):
        """Main loop of the maze."""
        while self.keys.pressed_key != "exit":
            self.view.display(self.maze)
            self.keys.check_keys()
            self.maze.update(self.keys.pressed_key, self.view)
