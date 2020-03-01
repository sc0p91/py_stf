# Playing around with pygame

import pygame, sys
from pygame.locals import *

orange = pygame.Color(255, 150, 0)
blue = pygame.Color(0, 0, 255, 128)
aqua = pygame.Color(50, 50, 255, 128)
green = pygame.Color(0, 255, 0, 128)
black = pygame.Color(0, 0, 0)

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
DISPLAYSURF.fill(orange)

pygame.display.set_caption('PyGame is amazing')

pygame.draw.polygon(DISPLAYSURF, blue, ((146, 0), (291, 106), (236, 277),(56, 277), (0, 106)))
pygame.draw.rect(DISPLAYSURF, aqua, (90, 100, 100, 100))
pygame.draw.rect(DISPLAYSURF, green, (50, 60, 100, 100))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
