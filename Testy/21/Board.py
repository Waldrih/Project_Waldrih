import pygame
from pygame import Surface

class Board:

    def __init__(self, main_scene: Surface, N_scene: Surface, E_scene: Surface, S_scene: Surface, W_scene: Surface):
        GRAY = (111, 111, 111)
        HEIGHT = 360
        WIDTH = 690
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill(GRAY)

        self.main_scene = main_scene
        self.N_scene = N_scene
        self.E_scene = E_scene
        self.S_scene = S_scene
        self.W_scene = W_scene

        self.DES_img = pygame.image.load('buttons_138px\DES.png')
        self.N_img = pygame.image.load('buttons_138px\Polnoc.png')
        self.E_img = pygame.image.load('buttons_138px\E.png')
        self.S_img = pygame.image.load('buttons_138px\S.png')
        self.W_img = pygame.image.load('buttons_138px\W.png')

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
                    if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False
                # draw button on screen
                Board.screen.blit(self.image, (self.rect.x, self.rect.y))

                return action

        self.DES_button = Button(552,300,self.DES_img)
        self.N_button = Button(0,300,self.N_img)

    def draw(self):
        self.screen.blit(self.main_scene,(0,0))
        #self.screen.fill((111,111,111))
        self.DES_button.draw()
        self.N_button.draw()
        pygame.display.update()







