import pygame
from Scene import Scene
from Main_2 import Button

class Board:
    DES_img = pygame.image.load('buttons_138px\DES.png')
    N_img = pygame.image.load('buttons_138px\Polnoc.png')
    E_img = pygame.image.load('buttons_138px\E.png')
    S_img = pygame.image.load('buttons_138px\S.png')
    W_img = pygame.image.load('buttons_138px\W.png')

    def __init__(self, main_scene: Scene, N_scene: Scene, E_scene: Scene, S_scene: Scene, W_scene):
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

        self.DES_button = Button(552,300,self.DES_img)
        self.N_button = Button(0,300,self.N_img)

    def draw(self):
        self.screen.blit(self.main_scene.image,(0,0))
        self.screen.fill((111,111,111))
        self.N_button.draw()
        self.DES_button.draw()
        self.N_button.draw()
        pygame.display.update()







