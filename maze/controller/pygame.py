"""Pygame controller."""

import sys

import pygame


class InputKeys:
    """Check input keys."""

    def __init__(self):
        """Init keys."""

        pygame.init()

        self.pressed_key = ""

    def check_keys(self):
        """Check pressed keys."""

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.pressed_key = "left"
                if event.key == pygame.K_RIGHT:
                    self.pressed_key = "right"
                if event.key == pygame.K_UP:
                    self.pressed_key = "up"
                if event.key == pygame.K_DOWN:
                    self.pressed_key = "down"
