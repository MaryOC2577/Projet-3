"""Pygame controller."""

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
        self.pressed_key = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.pressed_key = "exit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.pressed_key = "left"
                elif event.key == pygame.K_RIGHT:
                    self.pressed_key = "right"
                elif event.key == pygame.K_UP:
                    self.pressed_key = "up"
                elif event.key == pygame.K_DOWN:
                    self.pressed_key = "down"
                else:
                    messages.set_message("Invalid Key !")
