#!/usr/bin/python3
# Playing around with pygame

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

orange = (240, 100, 40)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Catty McCatface')

while True:

    DISPLAYSURF.fill(orange)
    if direction == 'right':
        catx += 5
        if catx == 320:
            direction = 'down'
    elif direction == 'down':
        caty +=5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -=5 
        if caty == 10:
                direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
