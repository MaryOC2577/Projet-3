"""Pygame controller."""

from os import sys
import pygame
from maze.model.message import messages


class InputKeys:
    """Check input keys."""

    def __init__(self):
        """Init keys."""
        pygame.init()

        self.pressed_key = ""

    def check_keys(self):
        """Check pressed keys."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.key == pygame.K_LEFT:
                self.pressed_key = "left"
            elif event.key == pygame.K_RIGHT:
                self.pressed_key = "right"
            elif event.key == pygame.K_DOWN:
                self.pressed_key = "down"
            elif event.key == pygame.K_UP:
                self.pressed_key = "up"
            else:
                messages.add_message("Invalid key !")
                self.pressed_key = ""
                return
