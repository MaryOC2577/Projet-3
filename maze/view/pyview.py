"""Pygame view."""

import sys
from os import sys

import pygame

from maze import config


class PyView:
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
                    items_char = [item.char for item in maze.items]
                    if position == maze.hero.position:
                        self.screen.blit(self.hero, pygame_position)
                    elif position == maze.guardian:
                        self.screen.blit(self.guardian, pygame_position)

        pygame.display.flip()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
