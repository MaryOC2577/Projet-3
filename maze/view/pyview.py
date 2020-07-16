"""Pygame view."""

import sys
import pygame
from os import sys

class PyView:
    """View with pygame."""

    def __init__(self):
        """Initialized."""

    def display(self, maze):
        """Main method."""
        system("cls")
        self.display_maze(maze)

    def display_maze(self, maze):
    """Display the maze."""

        pygame.init()

        size = width, height = (480, 480)
        background_color = (0, 50, 0)

        screen = pygame.display.set_mode(size)
        screen.fill(background_color)

        wall = pygame.image.load(
            "c:/Users/Utilisateur/OneDrive/Documents/prog/projet3/maze/data/wall.png"
        )

        for index_y in range(maze.height + 1):
            for index_x in range(maze.width + 1):
                position = (index_x, index_y)
                if position in maze.walls:
                    screen.blit(wall, (position[0]*32, position[1]*32)

        #screen.blit(wall, (0, 32))

        pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
