"""Main file."""

from maze.application import Software
from maze.controller import consolecontroller, pygamecontroller
from maze.view import consoleview, pygameview


modes = {
    "console": (consolecontroller.InputKeysCli, consoleview.CliView),
    "pygame": (pygamecontroller.InputKeysGame, pygameview.PyGameView),
}
mode = input("Choose mode (console / pygame) : ")
if mode not in modes:
    print("mode not valid.")
else:
    controller, view = modes[mode]
    application = Software(controller(), view())
    application.run_maze()

