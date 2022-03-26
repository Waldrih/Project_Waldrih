import pygame.image
from pygame import Surface
from Button import Button

class Scene:
    def __int__(self, image: Surface):
        self.HEIGHT = 360
        self.WIDTH = 690
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.image = image

    def __init__(self,image: Surface, image_button_1: Surface, image_button_2: Surface):
        self.HEIGHT = 360
        self.WIDTH = 690
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.image = image
        self.img_button_1 = image_button_1
        self.img_button_2 = image_button_2
        self.image_button_1 = Button(0,300,image_button_1)
        self.image_button_2 = Button(345,300,image_button_2)

    def draw(self):
        self.screen.blit(self.image,(0,0))
        self.image_button_1.draw()
        pygame.display.update()




