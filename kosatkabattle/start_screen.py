import pygame

from .utils import load_image, terminate


class StartScreen:
    def __init__(self, surface):
        self.surface = surface
        self.background = load_image("menu_background.png")
        self.logo = load_image("logo.png")
        self.start = False

    def run(self):
        while not self.start:
            self.events()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type in [pygame.MOUSEBUTTONDOWN, pygame.key]:
                self.start = True

    def update(self):
        self.surface.blit(self.background, (0, 0))
        self.surface.blit(self.logo, (57, 100))
        pygame.display.flip()