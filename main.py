import pygame
from pygame.locals import *
from sys import exit

pygame.init()
width = 400
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simulador Equação de Drake')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(window, (255, 0, 0),
                     (width/4, height/4, width/2, height/2))
    pygame.draw.circle(window, (0, 0, 120), (width/2, height/2), width/4)
    pygame.display.update()
