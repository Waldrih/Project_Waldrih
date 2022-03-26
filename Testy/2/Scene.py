import pygame.image
from pygame import Surface


class Scene:
    def __init__(self,image: Surface):
        self.HEIGHT = 360
        self.WIDTH = 690
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.image = image

    def draw(self):
        self.screen.blit(self.image,(0,0))
