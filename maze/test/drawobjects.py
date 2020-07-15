"""Draws objects."""

import sys
import pygame

pygame.init()

size = width, height = (320, 240)
background_color = (80, 80, 200)
color_line = (0, 0, 0)

screen = pygame.display.set_mode(size)

screen.fill(background_color)
pygame.draw.line(screen, color_line, [30, 30], [30, 90])
pygame.draw.circle(screen, color_line, [150, 150], 10)

pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
