import pygame

from os import path

SIZE = WIDTH, HEIGHT = 1280, 720
FPS = 60


def load_image(filename):
    fullname = path.join("data", "images", filename)
    return pygame.image.load(fullname).convert_alpha()


def terminate():
    pygame.quit()
    exit()
