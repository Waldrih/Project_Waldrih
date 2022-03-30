import time

import pygame
from pygame import Surface



pygame.init()

GRAY = (111, 111, 111)
HEIGHT = 360
WIDTH = 690
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Button demo')
screen.fill(GRAY)

class Board:
    main_img = None
    def __init__(self, main_img: Surface, N: bool, E: bool, S: bool, W: bool, description_img: Surface ):
        self.main_img = main_img
        self.N = N
        self.E = E
        self.S = S
        self.W = W
        self.description_img = description_img

    def get_main_img(self):
        return self.main_img

class Position:
    def __init__(self, x: int, y: int, board: Board ):
        self.x = x
        self.y = y
        self.board = board

    def get_board(self):
        return self.board

    def __str__(self):
        return f"Pozycja x: {self.x}. y: {self.y}"

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

img_description_1 = pygame.image.load('descriptions\des_1.png.bmp')
img_description_2 = pygame.image.load('descriptions\des_2.png.bmp')
img_description_3 = pygame.image.load('descriptions\des_3.png.bmp')

button_des = Button(552, 300, img_button_DES )
button_N = Button(0,300,img_button_N)
button_E = Button(138,300,img_button_E)
button_S = Button(276,300,img_button_S)
button_W = Button(414,300,img_button_W)

board_1 = Board(img_scene_1,True,False,False,False,img_description_1)
board_2 = Board(img_scene_2, False,True,True,False,img_description_2)
board_3 = Board(img_scene_3,False,False,True,True,img_description_3)

position_1_1 = Position(1,1,Board(img_scene_1,True,False,False,False,img_description_1))
position_1_0 = Position(1,0,board_2)
position_2_0 = Position(2,0,board_2)

positions = [position_1_1,position_1_0,position_2_0]

def choise_button(N: bool, E: bool, S: bool, W: bool):
    if N and True:
        print("Idymy na PO")
    if E and True:
        print("Pódziesz Ty na wschód")
    if S and True:
        pass

def draw_board(positions: list, x_start: int, y_start: int):
    i = 0
    current_position = positions[i]

    for i in range(len(positions)):
        pass

    cur_board = current_position.board


while True:


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            quit()

pygame.display.update()