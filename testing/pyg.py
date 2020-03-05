#!/usr/bin/python3
# Playing around with pygame

import pygame, sys
from pygame.locals import *

orange = pygame.Color(255, 150, 0)
blue = pygame.Color(0, 0, 255, 128)
aqua = pygame.Color(120, 220, 255, 128)
green = pygame.Color(0, 255, 0, 128)
black = pygame.Color(0, 0, 0)
baseh = 100
basev = 100

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
DISPLAYSURF.fill(orange)

pygame.display.set_caption('PyGame is amazing')

pygame.draw.polygon(DISPLAYSURF, blue, ((146, 0), (291, 106), (236, 277),(56, 277), (0, 106)))
pygame.draw.rect(DISPLAYSURF, green, (50, 60, 100, 100))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            pygame.time.delay(10)
            baseh -= 1
        if event.key == pygame.K_RIGHT:
            pygame.time.delay(10)
            baseh += 1
        if event.key == pygame.K_UP:
            pygame.time.delay(10)
            basev -= 1
        if event.key == pygame.K_DOWN:
            pygame.time.delay(10)
            basev += 1
    pygame.draw.rect(DISPLAYSURF, aqua, (baseh, basev, 10, 10))
