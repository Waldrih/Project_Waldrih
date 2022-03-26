import pygame
from pygame import Surface
from Scene import Scene

pygame.init()

GRAY = (111,111,111)
HEIGHT = 360
WIDTH = 690
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(GRAY)

img_1 = pygame.image.load('button_1.png')
img_2 = pygame.image.load('button_2.png')
img_scene_1 = pygame.image.load('scene_1.png')
img_scene_2 = pygame.image.load('scene_2.png')
img_scene_3 = pygame.image.load('scene_3.png')

scene_1 = Scene(img_scene_1)
scene_2 = Scene(img_scene_2)
scene_3 = Scene(img_scene_3)

scene_2.draw()
pygame.display.update()
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                screen.blit(scene_1.scene_1, (0, 0))
                pygame.display.update()
            elif event.key == pygame.K_LEFT:
                screen.blit(scene_1.scene_2, (0, 0))
                pygame.display.update()
            elif event.key == pygame.K_UP:
                screen.blit(scene_1.scene_3, (0, 0))
                pygame.display.update()

pygame.display.update()