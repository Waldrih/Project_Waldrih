import pygame
from pygame import Surface

class Board:
    def __init__(self, main_img: Surface, N: bool, E: bool, S: bool, W: bool, description_img: Surface ):
        self.main_img = main_img
        self.N = N
        self.E = E
        self.S = S
        self.W = W
        self.description_img = description_img

