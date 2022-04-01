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
time_to_blit = None

class Board:
    main_img = None
    def __init__(self, main_img: Surface \
        ,N: bool, E: bool, S: bool, W: bool,\
        description_img: Surface ):
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

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

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
                print(action)
                return action
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
position_2_0 = Position(2,0,board_3)

positions = [position_1_1,position_1_0,position_2_0]

def choise_button(N: bool, E: bool, S: bool, W: bool):
    if N and button_N.draw():
        print("Możesz iść na połnoc")
        bool_n = button_N.draw()
    elif N == False and button_N.draw():
        print("Nie możesz iść na północ")

    if E and button_E.draw():
        print("Możesz iść na wschód")
        bool_e = button_E.draw()
    elif E == False and button_E.draw():
        print("Nie możesz iść na wschód")

    if S and button_S.draw():
        print("Możesz iść na południe")
        bool_s = button_S.draw()
    elif S == False and button_S.draw():
        print("Nie możesz iść na południe")

    if W and button_W.draw():
        print("Możesz iść na zachód")
        bool_w = button_W.draw()
    elif W == False and button_W.draw():
        print("Nie możesz iść na zachód")

def draw_board(x_start: int, y_start: int):
    for position in positions:
        if position.get_x() == x_start and position.get_y() == y_start:
            screen.blit(position.board.get_main_img(),(0,0))
        if button_des.draw():
            screen.blit(img_description_1,(45,30))

            pygame.display.update()
            time.sleep(3)
            print("opis")


    choise_button(True,False,False,False)


while True:
    draw_board(1,1)
    pygame.display.update()
    #choise_button(True, False, False, False)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            quit()

pygame.display.update()