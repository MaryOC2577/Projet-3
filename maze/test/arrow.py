"""Test saisie touches fléchées."""

from os import sys

import pygame


class test:
    """test."""

    def __init__(self):
        """init."""

        pygame.init()

        self.size = width, height = (480, 480)
        self.background_color = (0, 50, 0)
        self.screen = pygame.display.set_mode(self.size)
        self.fontion_test()

    def fontion_test(self):
        """test"""
        self.screen.fill(self.background_color)

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        pygame.display.flip()
