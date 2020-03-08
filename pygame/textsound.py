#!/usr/bin/python3
# Playing around with pygame

import pygame, sys, time
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('PyGame is amazing')

orange = pygame.Color(255, 150, 0)
blue = pygame.Color(0, 0, 255, 128)
black = pygame.Color(0, 0, 0)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello World', True, blue, orange)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

pygame.mixer.music.load('files/bell.mp3')
pygame.mixer.music.play(-1, 0.0)

while True:
    DISPLAYSURF.fill(black)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
