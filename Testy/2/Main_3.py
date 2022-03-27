import pygame
from Scene import Scene
from Button import Button
from Board import Board
from pygame import Surface

pygame.init()

GRAY = (111,111,111)
HEIGHT = 360
WIDTH = 690
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(GRAY)

class Button():
    def __init__(self, x, y, image: Surface):
        width = image.get_width()
        height = image.get_height()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False


        # draw button on screen
        HEIGHT = 360
        WIDTH = 690
        screen.blit(self.image, (self.rect.x, self.rect.y))


        #return action


#load images
button_img_345_idz_na_polnoc = pygame.image.load('buttons\idz_na_polnoc_345px.png')
button_img_345_opis_okolicy = pygame.image.load('buttons\opis_okolicy_345px.png')
img_1 = pygame.image.load('button_1.png')
img_2 = pygame.image.load('button_2.png')
img_scene_1 = pygame.image.load('scene_1.png')
img_scene_2 = pygame.image.load('scene_2.png')
img_scene_3 = pygame.image.load('scene_3.png')

#create instances
scene_1 = Scene(img_scene_1, button_img_345_idz_na_polnoc, button_img_345_opis_okolicy)
scene_2 = Scene(img_scene_2, button_img_345_idz_na_polnoc, button_img_345_opis_okolicy)
#scene_3 = Scene(img_scene_3)
button_345_N = Button
#boards instances
board_1 = Board(scene_1,scene_2,scene_2,scene_2,scene_2)
board_1.draw()


pygame.display.update()
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()



pygame.display.update()