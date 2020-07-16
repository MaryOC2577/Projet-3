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
        self.hero = pygame.image.load(
            "c:/Users/Utilisateur/OneDrive/Documents/prog/projet3/maze/data/hero.png"
        )
        self.guardian = pygame.image.load(
            "c:/Users/Utilisateur/OneDrive/Documents/prog/projet3/maze/data/guardian.png"
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
                elif position in maze.paths:
                    items_positions = [item.position for item in maze.items]
                    items_char = [item.char for item in maze.items]
                    if position == maze.hero.position:
                        self.screen.blit(
                            self.hero, (position[0] * 32, position[1] * 32)
                        )
                    elif position == maze.guardian:
                        self.screen.blit(
                            self.guardian, (position[0] * 32, position[1] * 32)
                        )
                    elif position in items_positions:
                        if items_char[items_positions.index(position)] == "T":
                            self.screen.blit(
                                self.tube, (position[0] * 32, position[1] * 32)
                            )
                        if items_char[items_positions.index(position)] == "N":
                            self.screen.blit(
                                self.needle,
                                (position[0] * 32, position[1] * 32),
                            )
                        if items_char[items_positions.index(position)] == "E":
                            self.screen.blit(
                                self.ether, (position[0] * 32, position[1] * 32)
                            )

        pygame.display.flip()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
