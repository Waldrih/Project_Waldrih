import pygame
from pygame.time import Clock
from time import sleep
from Position import Position
from Model import Model

pygame.init()

GRAY = (111,111,111)
HEIGHT = 360
WIDTH = 690
MODEL_WIDTH = 90
model_1 = Model(180,180)
Y_POSITION = 180
#grass = pygame.image.load(r'C:\Users\waldr\Desktop\Project_Waldrih\Testy\1\grass.png')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(GRAY)

screen.blit(model_1.model_1_2, (0, Y_POSITION))


def draw_model(x_position: int, model: Model):
    if x_position % 2 == 0:
        if x_position == 0:
            screen.fill(GRAY)
            screen.blit(model.model_1_1, (30, Y_POSITION))
            pygame.display.update()
        else:
            screen.fill(GRAY)
            screen.blit(model.model_1_1, ((x_position + 45 + 30), Y_POSITION))
            pygame.display.update()
    else:
        screen.fill(GRAY)
        screen.blit(model.model_1_2, ((x_position + 45 + 30), Y_POSITION))
        pygame.display.update()
    pygame.display.update()

x_position = 0
screen.blit(model_1.model_1_2, (x_position, Y_POSITION))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if x_position % 90 == 0:
                    x_position += 45
                    print("krok")
                    print(f"Pozycja x: {x_position}")
                    screen.fill(GRAY)
                    screen.blit(model_1.model_1_1, (x_position, Y_POSITION))
                    pygame.display.update()
                    print(f"kolejna pozycja: {x_position}")
                    print("")
                else:
                    x_position += 45
                    print("stop")
                    print(f"Pozycja x: {x_position}")
                    screen.fill(GRAY)
                    screen.blit(model_1.model_1_2, (x_position, Y_POSITION))
                    pygame.display.update()
                    print(f"kolejna pozycja: {x_position}")
                    print("")
            elif event.key == pygame.K_LEFT:
                if x_position % 90 == 0:
                    print("krok w tył")
                    print(f"Pozycja x: {x_position}")
                    screen.fill(GRAY)
                    screen.blit(model_1.model_1_2, (x_position, Y_POSITION))
                    pygame.display.update()
                    x_position -= 45
                    print(f"num: {x_position}")
                    print("")
                else:
                    print("stop w tył")
                    print(f"Pozycja x: {x_position}")
                    screen.fill(GRAY)
                    screen.blit(model_1.model_1_1, (x_position, Y_POSITION))
                    pygame.display.update()
                    x_position -= 45
                    print(f"num: {x_position}")
                    print("")


    pygame.display.update()

