#!/usr/bin/python3

import pygame, time, random

pygame.init()

white =     (255, 255, 255)
black =     (0, 0, 0)
blue =      (0, 178, 169)
green =     (0, 154, 23)
red =       (255, 0, 0)
yellow =    (255, 100, 0)
dis_width = 800
dis_height = 600
snake_block = 10
snake_speed = 20 
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Super Swane Snake")

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [100, dis_height/3])

def our_score(score):
    if score > 0:
        value = font_style.render("Pünkt: " + str(score), True, yellow)
        dis.blit(value, [10, 10])


def gameLoop():

    game_over = False
    game_close = False
    x1 = int(dis_width/2)
    y1 = int(dis_height/2)
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0)) * 10
    foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0)) * 10

    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("Verlore! <Q> für use, <C> für nomou", red)
            our_score(Length_of_snake -5)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        # Stürig
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if Length_of_snake == 1 and (x1 != int(dis_width/2) or y1 != int(dis_height/2)):
            Length_of_snake += 4

        
        dis.fill(black)
        
        # Check Border Collision
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Draw Food
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # Create Snake
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        our_score(Length_of_snake -5)

        # Eat Food
        if x1 == foodx and y1 == foody:
            foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0)) * 10
            foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0)) * 10
            Length_of_snake += 1

        # Move Snake
        x1 += x1_change
        y1 += y1_change
        
        pygame.display.update()
        
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
