"""Main file."""

from maze.application import Software

from maze.controller.console import InputKeysCli
from maze.controller.pygame import InputKeysGame
from maze.view.console import CliView
from maze.view.pygame import PyGameView

modes = {
    "console": (InputKeysCli, CliView),
    "pygame": (InputKeysGame, PyGameView),
}
mode = input("Choose mode (console / pygame) : ")
if mode not in modes:
    print("mode not valid.")
else:
    controller, view = modes[mode]
    application = Software(controller(), view())
    application.run_maze()
