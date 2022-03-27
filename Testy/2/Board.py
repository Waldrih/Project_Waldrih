import pygame
from Scene import Scene
from Button import Button

class Board:
    DES_img = pygame.image.load('buttons_138px\DES.png')
    N_img = pygame.image.load('buttons_138px\N.png')
    E_img = pygame.image.load('buttons_138px\E.png')
    S_img = pygame.image.load('buttons_138px\S.png')
    W_img = pygame.image.load('buttons_138px\W.png')

    def __init__(self, main_scene: Scene, N_scene: Scene, E_scene: Scene, S_scene: Scene, W_scene):
        self.main_scene = main_scene
        self.N_scene = N_scene
        self.E_scene = E_scene
        self.S_scene = S_scene
        self.W_scene = W_scene





