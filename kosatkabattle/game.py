import pygame

from .utils import *
from .start_screen import StartScreen

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.game = True
        self.all_sprites = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

    def update(self):
        pass

    def run(self):
        start = StartScreen(self.surface)
        start.run()

        while self.game:
            self.events()
            self.update()
            self.clock.tick(FPS)
