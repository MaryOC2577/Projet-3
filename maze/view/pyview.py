"""Pygame view."""

import sys
from os import sys
import pygame


class PyView:
    """View with pygame."""

    def __init__(self):
        """Initialized."""

        pygame.init()

        self.size = width, height = (480, 480)
        self.background_color = (0, 50, 0)
        self.screen = pygame.display.set_mode(self.size)

        self.wall = pygame.image.load(
            "c:/Users/Utilisateur/OneDrive/Documents/prog/projet3/maze/data/wall.png"
        )

    def display(self, maze):
        """Main method."""
        self.display_maze(maze)

    def display_maze(self, maze):
        """Display the maze."""

        self.screen.fill(self.background_color)

        for index_y in range(maze.height + 1):
            for index_x in range(maze.width + 1):
                position = (index_x, index_y)
                if position in maze.walls:
                    self.screen.blit(
                        self.wall, (position[0] * 32, position[1] * 32)
                    )

        pygame.display.flip()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
