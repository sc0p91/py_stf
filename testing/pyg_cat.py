#!/usr/bin/python3
# Playing around with pygame

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
DISPLAYSURF.fill(orange)
pygame.display.set_caption('Catty McCatface')

catImg = pygame.image.load('cat.png')

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
