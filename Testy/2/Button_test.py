import time

import pygame
from pygame import Surface
from pygame import Rect
from Scene import Scene

pygame.init()

GRAY = (111, 111, 111)
HEIGHT = 360
WIDTH = 690
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Button demo')
screen.fill(GRAY)

scene_1 = Scene()
screen.blit(scene_1.scene_1, (0, 0))
pygame.display.set_caption('Button demo')
pygame.display.update()

# load button image
start_img = pygame.image.load('button_1.png').convert_alpha()
exit_img = pygame.image.load('button_2.png').convert_alpha()
print("Typ image")
print(type(start_img))

# button class
class Button():
    def __init__(self, x, y, image: Surface, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        #chech mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                print("click")

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                print("not click")
        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


# create button instance
button_1 = Button(0,270,start_img, 1)
button_2 = Button(540,270,exit_img, 1)

# game loop
run = True
while run:

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
quit()
