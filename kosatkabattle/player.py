import pygame

from .utils import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game, surface):
        super().__init__(game.all_sprites)
