# coding=utf-8
"""
This is an example script.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
import pygame
import sys
import time
import settings
from gameMode import GameMode, Tile


pygame.init()

speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(settings.SCREEN_SIZE)

gameMode = GameMode()
screen.blit(gameMode.world.get_surface(), (0, 0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    gameMode.world.update()
    time.sleep(1.5)
    screen.blit(gameMode.world.get_surface(), (0, 0))
    pygame.display.flip()
