import time

import pygame
from pygame import Surface
from Position import Position

pygame.init()

GRAY = (111, 111, 111)
HEIGHT = 360
WIDTH = 690
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Button demo')
screen.fill(GRAY)

# button class
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
        #chech mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

img_scene_1 = pygame.image.load('scenes\scene_1.png')
img_scene_2 = pygame.image.load('scenes\scene_2.png')
img_scene_3 = pygame.image.load('scenes\scene_3.png')
img_scene_4 = pygame.image.load('scenes\scene_3.png')
img_scene_5 = pygame.image.load('scenes\scene_3.png')
img_button_DES = pygame.image.load('buttons_138px\DES.png')
img_button_N = pygame.image.load('buttons_138px\Polnoc.png')
img_button_E = pygame.image.load('buttons_138px\E.png')
img_button_S = pygame.image.load('buttons_138px\S.png')
img_button_W = pygame.image.load('buttons_138px\W.png')

button_des = Button(552, 300, img_button_DES )
button_N = Button(0,300,img_button_N)
button_E = Button(138,300,img_button_E)
button_S = Button(276,300,img_button_S)
button_W = Button(414,300,img_button_W)

position_1 = Position(1,1,img_scene_1,True,False,False,False)
position_2 = Position(1,0,img_scene_2,False,True,True,False)
position_3 = Position(2,0,img_scene_3,True,False,True,True)

def choise_button(N: bool, E: bool, S: bool, W: bool):
    if N and True:
        print("Idymy na PO")
    if E and True:
        print("Pódziesz Ty na wschód")
    if S and True:
        pass

def draw_board(main_board: Surface):
    screen.blit(img_scene_1, (0, 0))
    if button_des.draw():
        print("Malowniczy opis nudnego terenu")

    if button_N.draw():
        print("Pójdem na PÓŁNOC")
    button_E.draw()

    button_S.draw()

    button_W.draw()

current_position = Position(0,0)

def draw_board(board_position: Position):
    screen.blit(board_position.image, (0, 0))
    current_position.x = board_position.x
    current_position.y = board_position.y
    if button_des.draw():
        print("Malowniczy opis nudnego terenu")
        time.sleep(5)
        print("W trakcie realizacji")
    if button_N.draw() and board_position.N:
        print("Pójdem na PÓŁNOC")
        time.sleep(3)
    if button_E.draw() and board_position != True:
        print("Nie woln Ci iść na wschód")

while True:
    draw_board(Position(1,1))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            quit()

pygame.display.update()