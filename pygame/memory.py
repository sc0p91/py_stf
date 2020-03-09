#!/usr/bin/python3
# Playing around with pygame

import pygame, random, sys
from pygame.locals import *

################################################
# START INITIALISATION
################################################

FPS = 30
winwidth = 640
winheight = 480
boardwidth = 3
boardheight = 4
revealspeed = 8
boxsize = 40
gapsize = 10
assert (boardwidth * boardheight) % 2 == 0
xmargin = int((winwidth - (boardwidth * (boxsize + gapsize))) / 2)
ymargin = int((winheight - (boardheight * (boxsize + gapsize))) / 2)

#               R    G    B
GRAY        = (100, 100, 100)
NAVYBLUE    = ( 60,  60, 100)
WHITE       = (255, 255, 255)
RED         = (255,   0, 0)
GREEN       = (  0, 255, 0)
BLUE        = (  0,   0, 255)
YELLOW      = (255, 255, 0)
ORANGE      = (255, 128, 0)
PURPLE      = (255,   0, 255)
CYAN        = (  0, 255, 255)

bgcolor = NAVYBLUE
lightbgcolor = GRAY
boxcolor = WHITE
highlightcolor = BLUE

donut = 'donut'
square = 'square'
diamond = 'diamond'
lines = 'lines'
oval = 'oval'

allcolors = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
allshapes = (donut, square, diamond, lines, oval)

assert len(allcolors) * len(allshapes) * 2 >= boardwidth * boardheight,\
"Board is too big for the number of shapes / colors defined." 

################################################
# STOP INITIALISATION
################################################

################################################
# START MAIN FUNCTION
################################################

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((winwidth, winheight))

    mousex = 0
    mousey = 0
    pygame.display.set_caption('Swans Memory Spili')

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None

    DISPLAYSURF.fill(bgcolor)
    startGameAnimation(mainBoard)

    while True:
        mouseClicked = False

        DISPLAYSURF.fill(bgcolor)
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE) or (event.type == KEYUP and event.key == K_q):
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex, mousey)
        if boxx != None and boxy != None:
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx, boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxesAnimation(mainBoard, [(boxx, boxy)])
                revealedBoxes[boxx][boxy] = True
                if firstSelection == None:
                    firstSelection = (boxx, boxy)
                else:
                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)
                    
                    if icon1shape != icon2shape or icon1color != icon2color:
                        pygame.time.wait(1000)
                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                    elif hasWon(revealedBoxes):
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)

                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)

                        drawBoard(mainBoard, revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        startGameAnimation(mainBoard)
                    firstSelection = None

    pygame.display.update() 
    FPSCLOCK.tick(FPS)

################################################
# END MAIN FUNCTION
################################################

################################################
# START HELPER FUNCTIONS
################################################

def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(boardwidth):
        revealedBoxes.append([val] * boardheight)
    return revealedBoxes

def getRandomizedBoard():
    icons = []
    for color in allcolors:
        for shape in allshapes:
            icons.append( (shape, color) )

    random.shuffle(icons)
    numIconsUsed = int(boardwidth * boardheight / 2)
    icons  = icons[:numIconsUsed] * 2
    random.shuffle(icons)

    board = []
    for x in range(boardwidth):
        column = []
        for y in range(boardheight):
            column.append(icons[0])
            del icons[0]
        board.append(column)
    return board

def splitIntoGroupsOf(groupSize, theList):
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i + groupSize])
    return result

def leftTopCoordsOfBox(boxx, boxy):
    left = boxx * (boxsize + gapsize) + xmargin
    top = boxy * (boxsize + gapsize) + ymargin
    return (left, top)

def getBoxAtPixel(x, y):
    for boxx in range(boardwidth):
        for boxy in range(boardheight):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, boxsize, boxsize)
            if boxRect.collidepoint(x, y):
                return(boxx, boxy)
    return (None, None)

def drawIcon(shape, color, boxx, boxy):
    quarter = int(boxsize * 0.25)
    half    = int(boxsize * 0.5)

    left, top = leftTopCoordsOfBox(boxx, boxy)
    if shape == donut:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
        pygame.draw.circle(DISPLAYSURF, bgcolor, (left + half, top + half), quarter - 5)
    elif shape == square:
        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, boxsize - half, boxsize - half))
    elif shape == diamond:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top),(left + boxsize - 1, top + half), (left + half, top + boxsize - 1), (left, top + half)))
    elif shape == lines:
        for i in range (0, boxsize, 4):
            pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
            pygame.draw.line(DISPLAYSURF, color, (left + i, top + boxsize -  1), (left + boxsize - 1, top + i)) 
    elif shape == oval:
        pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, boxsize, half))

def getShapeAndColor(board, boxx, boxy):
    return board[boxx][boxy][0], board[boxx][boxy][1]

def drawBoxCovers(board, boxes, coverage):
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1])
        pygame.draw.rect(DISPLAYSURF, bgcolor, (left, top, boxsize, boxsize))
        shape, color = getShapeAndColor(board, box[0], box[1])
        drawIcon(shape, color, box[0], box[1])
        if coverage > 0:
            pygame.draw.rect(DISPLAYSURF, boxcolor, (left, top, coverage, boxsize))
    pygame.display.update()
    FPSCLOCK.tick(FPS)

def revealBoxesAnimation(board, boxesToReveal):
    for coverage in range(boxsize, (-revealspeed) - 1, -revealspeed):
        drawBoxCovers(board, boxesToReveal, coverage)

def coverBoxesAnimation(board, boxesToCover):
    for coverage in range(0, boxsize + revealspeed, revealspeed):
        drawBoxCovers(board, boxesToCover, coverage)

def drawBoard(board, revealed):
    for boxx in range(boardwidth):
        for boxy in range(boardheight):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                pygame.draw.rect(DISPLAYSURF, boxcolor, (left, top, boxsize, boxsize))
            else:
                shape, color = getShapeAndColor(board, boxx, boxy)
                drawIcon(shape, color, boxx, boxy)

def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, highlightcolor, (left - 5, top - 5, boxsize + 10, boxsize + 10), 4)

def startGameAnimation(board):
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(boardwidth):
        for y in range(boardheight):
            boxes.append( (x, y) )
    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(8, boxes)

    drawBoard(board, coveredBoxes)
    for boxGroup in boxGroups:
        revealBoxesAnimation(board, boxGroup)
        coverBoxesAnimation(board, boxGroup)

def gameWonAnimation(board):
    coveredBoxes = generateRevealedBoxesData(True)
    color1 = lightbgcolor
    color2 = bgcolor

    for i in range(13):
        color1, color2 = color2, color1
        DISPLAYSURF.fill(color1)
        drawBoard(board, coveredBoxes)
        pygame.display.update()
        pygame.time.wait(250)

def hasWon(revealedBoxes):
    for i in revealedBoxes:
        if False in i:
            return False
    return True

if __name__ == '__main__':
    main()

################################################
# END HELPER FUNCTIONS
################################################
