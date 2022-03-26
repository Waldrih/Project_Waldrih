import pygame
from pygame import Surface
from Scene import Scene

pygame.init()

GRAY = (111,111,111)
HEIGHT = 360
WIDTH = 690
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(GRAY)
#scene_1_path = str(r'C:\Users\waldr\Desktop\Project_Waldrih\Testy\2\scene_1.png')

scene_1 = Scene()
screen.blit(scene_1.scene_1,(0,0))
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