import pygame

from kosatkabattle.game import Game
from kosatkabattle.utils import *

pygame.init()
screen = pygame.display.set_mode(SIZE)
game = Game(screen)

running = True

while running:
    game.run()
