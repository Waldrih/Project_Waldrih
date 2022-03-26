import pygame
from Scene import Scene
from Button import Button

class Board:
    def __init__(self, main_scene: Scene, first_button: Button, second_button: Button, second_scene: Scene):
        self.main_scene = main_scene
        self.first_button = first_button
        self.second_button = second_button
        self.second_scene = second_scene

