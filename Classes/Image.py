"""Program by William Stoneham 2020"""
import pygame


class Image(object):
    """image definer"""

    def __init__(self, game_display, image, x, y, convert=False, collision=False):
        self.game_display = game_display
        self.image_name = "Assets/" + image
        self.width = x
        self.height = y
        self.x = -self.width
        self.y = -self.height
        self.xlocs = []
        self.ylocs = []
        if collision:
            self.image = pygame.image.load(self.image_name).convert_alpha()
            self.map = pygame.mask.from_surface(self.image)
        if convert:
            self.image = pygame.image.load(self.image_name).convert()
        else:
            self.image = pygame.image.load(self.image_name)

    def blit(self, x, y):
        self.x = x
        self.y = y
        self.game_display.blit(self.image, (x, y))

    def return_map(self):
        return self.map
