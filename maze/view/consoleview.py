"""CLI view."""

import time

from os import system

from maze.model.message import messages
from maze.config import FRAMES_PER_SECOND


class CliView:
    """View in console mode."""

    def __init__(self):
        """Initialized."""

    def display(self, maze):
        """Main method."""
        system("cls")
        self.commands()
        self.display_maze(maze)
        self.display_messages()

    def commands(self):
        """Display controls."""
        commands = {
            "q": "left",
            "d": "right",
            "z": "up",
            "s": "down",
            "e": "exit",
        }
        for key, command in commands.items():
            print(" ", key, ":", command)
        print("\n")

    def display_maze(self, maze):
        """Display the maze."""
        for index_y in range(maze.height + 1):
            for index_x in range(maze.width + 1):
                position = (index_x, index_y)
                if position in maze.walls:
                    print("X", end="")
                elif position in maze.paths:
                    items_positions = [item.position for item in maze.items]
                    items_char = [item.char for item in maze.items]
                    if position == maze.hero.position:
                        print("H", end="")
                    elif position == maze.guardian:
                        print("G", end="")
                    elif position in items_positions:
                        print(
                            items_char[items_positions.index(position)], end=""
                        )
                    else:
                        print(".", end="")
            print()

    def display_messages(self):
        """Display the messages."""
        print(messages.get_message())

    def exit(self, maze):
        """Exit."""
        self.display(maze)
        time.sleep(2)
