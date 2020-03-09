#!/usr/bin/python3
# Playing around with pygame

import pygame, sys
from pygame.locals import *

orange = pygame.Color(255, 150, 0)
blue = pygame.Color(0, 0, 255, 128)
green = pygame.Color(0, 255, 0, 128)
black = pygame.Color(0, 0, 0)
baseh = 100
basev = 100

pygame.init()
pygame.display.set_caption('PyGame is amazing')
DISPLAYSURF = pygame.display.set_mode((400, 300))

while True:
    DISPLAYSURF.fill(orange)
    
    pygame.draw.polygon(DISPLAYSURF, blue, ((146, 0), (291, 106), (236, 277),(56, 277), (0, 106)))
    pygame.draw.rect(DISPLAYSURF, green, (50, 60, 100, 100))
    pygame.draw.rect(DISPLAYSURF, black, (baseh, basev, 10, 10))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            baseh -= 1
        if event.key == pygame.K_RIGHT:
            baseh += 1
        if event.key == pygame.K_DOWN:
            basev += 1
        if event.key == pygame.K_UP:
            basev -= 1

        if event.key == pygame.K_q or event.key == K_ESCAPE:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    FPSCLOCK = pygame.time.Clock()
    FPSCLOCK.tick(60)
