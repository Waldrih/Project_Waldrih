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

class Direction:
    NORTH = -1
    EAST = 1
    SOUTH = 1
    WEST = -1

class Board:
    # main_img = None
    def __init__(self, main_img: Surface \
                 , N: bool, E: bool, S: bool, W: bool, \
                 description_img: Surface):
        self.main_img = main_img
        self.N = N
        self.E = E
        self.S = S
        self.W = W
        self.description_img = description_img

    def get_main_img(self):
        return self.main_img

    def get_description_img(self):
        return self.description_img


class Position:
    def __init__(self, x: int, y: int, board: Board):
        self.x = x
        self.y = y
        self.board = board

    def __eq__(self, other):
        return isinstance(other, Position) and \
        self.x == other.x and \
        self.y == other.y

    def get_board(self):
        return self.board

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_position_north(self):
        self.y -= 1

    def set_position_east(self):
        self.x += 1

    def set_position_west(self):
        self.x -= 1

    def set_position_south(self):
        self.y += 1

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
        # get mouse position
        pos = pygame.mouse.get_pos()
        # chech mouseover and clicked conditions
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
img_scene_4 = pygame.image.load('scenes\scene_4.png')
img_scene_5 = pygame.image.load('scenes\scene_5.png')
img_scene_6 = pygame.image.load('scenes\scene_6.png')
img_scene_7 = pygame.image.load('scenes\scene_7.png')
img_scene_8 = pygame.image.load('scenes\scene_8.png')
img_scene_9 = pygame.image.load('scenes\scene_9.png')

img_button_DES = pygame.image.load('buttons_138px\DES.png')
img_button_N = pygame.image.load('buttons_138px\Polnoc.png')
img_button_E = pygame.image.load('buttons_138px\E.png')
img_button_S = pygame.image.load('buttons_138px\S.png')
img_button_W = pygame.image.load('buttons_138px\W.png')
img_no_way = pygame.image.load('buttons_138px\way.png')

img_description_1 = pygame.image.load('descriptions\des_1.png')
img_description_2 = pygame.image.load('descriptions\des_2.png')
img_description_3 = pygame.image.load('descriptions\des_3.png')
img_description_4 = pygame.image.load('descriptions\des_4.png')
img_description_5 = pygame.image.load('descriptions\des_5.png')
img_description_6 = pygame.image.load('descriptions\des_6.png')
img_description_7 = pygame.image.load('descriptions\des_7.png')
img_description_8 = pygame.image.load('descriptions\des_8.png')
img_description_9 = pygame.image.load('descriptions\des_9.png')

button_des = Button(552, 300, img_button_DES)
button_N = Button(0, 300, img_button_N)
button_E = Button(138, 300, img_button_E)
button_S = Button(276, 300, img_button_S)
button_W = Button(414, 300, img_button_W)

board_1 = Board(img_scene_1, True, False, False, False, img_description_1)
board_2 = Board(img_scene_2, False, True, True, False, img_description_2)
board_3 = Board(img_scene_3, False, False, True, True, img_description_3)
board_4 = Board(img_scene_4, True, False, True, True, img_description_4)
board_5 = Board(img_scene_5, True, False, False, True, img_description_5)
board_6 = Board(img_scene_6, False, True, False, True, img_description_6)
board_7 = Board(img_scene_7, True, True, False, False, img_description_7)
board_8 = Board(img_scene_8, True, False, True, False, img_description_8)
board_9 = Board(img_scene_9, False, False, True, False, img_description_9)

position_1_1 = Position(1, 1, board_1)
position_1_0 = Position(1, 0, board_2)
position_2_0 = Position(2, 0, board_3)
position_2_1 = Position(2, 1, board_4)
position_2_2 = Position(2, 2, board_5)
position_1_2 = Position(1, 2, board_6)
position_0_2 = Position(0, 2, board_7)
position_0_1 = Position(0, 1, board_8)
position_0_0 = Position(0, 0, board_9)


positions = [position_1_1, position_1_0, position_2_0, position_2_1, position_2_2,position_1_2,position_0_2,position_0_1,position_0_0]
revers_positions = list(reversed(positions))

def choise_button(N: bool, E: bool, S: bool, W: bool, pos: Position):
    if N and button_N.draw():
        print("Możesz iść na połnoc")
        print(f"Kierunek {Direction.NORTH}")
        print(pos)
        return pos.set_position_north()
    elif N == False and button_N.draw():
        print("Nie możesz iść na północ")

    if E and button_E.draw():
        print("Możesz iść na wschód")
        print(f"Kierunek {Direction.EAST}")
        return pos.set_position_east()
    elif E == False and button_E.draw():
        print("Nie możesz iść na wschód")

    if S and button_S.draw():
        print("Możesz iść na południe")
        print(f"Kierunek {Direction.SOUTH}")
        return pos.set_position_south()
    elif S == False and button_S.draw():
        print("Nie możesz iść na południe")

    if W and button_W.draw():
        print("Możesz iść na zachód")
        print(f"Kierunek {Direction.WEST}")
        return pos.set_position_west()
    elif W == False and button_W.draw():
        print("Nie możesz iść na zachód")

def draw_board(start_Position: Position, positions_list):

    for position in positions_list:
        if position.x == start_Position.x and position.y == start_Position.y:
            screen.blit(position.board.get_main_img(), (0, 0))

            if button_des.draw():
                screen.blit(position.board.get_description_img(), (45, 30))
                pygame.display.update()
                time.sleep(5)
                print("opis")
                print(f"Start pozycja {start_Position}")
                print(f"Pozycja z tablicy {positions.index(position)}")

        return choise_button(position.board.N, position.board.E, position.board.S, position.board.W,
                                 start_Position)

def draw_board_new(start_Position: Position, positions_list):

    for position in positions_list:
        if start_Position.__eq__(position):
            screen.blit(position.board.get_main_img(), (0, 0))
            if button_des.draw():
                screen.blit(position.board.get_description_img(), (45, 30))
                pygame.display.update()
                time.sleep(4)
                print("opis")
                print(f"Start pozycja {start_Position}")
                print(f"Pozycja z tablicy {positions.index(position)}")
                print("")

            return choise_button(position.board.N, position.board.E, position.board.S, position.board.W,start_Position)

def print_index(list, position: Position):
    for pos in list:
        if pos.__eq__(position):
            print(list.index(pos))



while True:
    draw_board_new(position_1_1,revers_positions)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

