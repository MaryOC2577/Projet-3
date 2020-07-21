"""Pygame view."""

import sys
from os import sys

import pygame

from maze import config


class PyGameView:
    """View with pygame."""

    def __init__(self):
        """Initialized."""

        pygame.init()

        self.size = width, height = (480, 480)
        self.background_color = (0, 50, 0)
        self.screen = pygame.display.set_mode(self.size)

        self.wall = pygame.image.load(str(config.IMG_DIR / "wall.png"))
        self.hero = pygame.image.load(str(config.IMG_DIR / "hero.png"))
        self.guardian = pygame.image.load(str(config.IMG_DIR / "guardian.png"))
        self.ether = pygame.image.load(str(config.IMG_DIR / "ether.png"))
        self.needle = pygame.image.load(str(config.IMG_DIR / "needle.png"))
        self.tube = pygame.image.load(str(config.IMG_DIR / "tube.png"))

    def display(self, maze):
        """Main method."""
        self.display_maze(maze)

    def display_maze(self, maze):
        """Display the maze."""

        self.screen.fill(self.background_color)

        for index_y in range(maze.height + 1):
            for index_x in range(maze.width + 1):
                position = (index_x, index_y)
                pygame_position = (
                    index_x * config.SPRITE_SIZE,
                    index_y * config.SPRITE_SIZE,
                )
                if position in maze.walls:
                    self.screen.blit(self.wall, pygame_position)
                elif position in maze.paths:
                    items_positions = [item.position for item in maze.items]
                    items_names = [item.name for item in maze.items]
                    if position == maze.hero.position:
                        self.screen.blit(self.hero, pygame_position)
                    elif position == maze.guardian:
                        self.screen.blit(self.guardian, pygame_position)
                    elif position in items_positions:
                        if (
                            items_names[items_positions.index(position)]
                            == "tube"
                        ):
                            self.screen.blit(self.tube, pygame_position)
                        elif (
                            items_names[items_positions.index(position)]
                            == "ether"
                        ):
                            self.screen.blit(self.ether, pygame_position)
                        elif (
                            items_names[items_positions.index(position)]
                            == "needle"
                        ):
                            self.screen.blit(self.needle, pygame_position)
                        # self.screen.blit(self.  +
                        # items_names[items_positions.index(position)],pygame_position)
        pygame.display.flip()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def display_messages(self, maze):
        """Display the messages."""
        for message in maze.messages:
            print(message)
            # afficher le message en bas de la fenêtre pendant 2 secondes
        maze.messages.clear()
