# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:41:08 2020

@author: Dell
"""


from random import randrange
import pygame
import numpy as np

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = pygame.Color("#00b906")
red = (255, 0, 0)

displayX = 500
displayY = 500

blockSize = 10
borderSize = 10

FPS = 15

gameDisplay = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)


def scoreDisplay(score, color):
    text = font.render(score, True, color)
    gameDisplay.blit(text, [300, 300])
    print("msg")


def increseLength(snakeX, snakeY):
    snakeX.append(snakeX[-1] - 10)
    snakeY.append(snakeY[-1] - 10)


def snake():
    gameExit = False

    lead_x = displayX / 2
    lead_y = displayY / 2
    lead_x_change = 0
    lead_y_change = 0
    keyX = True
    keyY = True

    foodX = randrange(borderSize, displayX-(2*borderSize)+10, 10)
    foodY = randrange(borderSize, displayY-(2*borderSize)+10, 10)

    score = 0

    # image = pygame.image.load("background.png")
    # image = pygame.transform.scale(image, (displayX, displayY))

    snakeX = [lead_x]
    snakeY = [lead_y]

    while not gameExit:
        for event in pygame.event.get():
            # print(event)

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and keyY and not lead_x == borderSize:
                    lead_x_change = -blockSize
                    lead_y_change = 0
                    keyX = True
                    keyY = False
                    print("left")

                elif event.key == pygame.K_RIGHT and keyY and not lead_x == displayX-(2*borderSize):
                    lead_x_change = blockSize
                    lead_y_change = 0
                    keyX = True
                    keyY = False
                    print("right")

                elif event.key == pygame.K_UP and keyX and not lead_y == borderSize:
                    lead_y_change = -blockSize
                    lead_x_change = 0
                    keyX = False
                    keyY = True
                    print("up")

                elif event.key == pygame.K_DOWN and keyX and not lead_y == displayY-(2*borderSize):
                    lead_y_change = blockSize
                    lead_x_change = 0
                    keyX = False
                    keyY = True
                    print("down")

        #lead_x += lead_x_change
        #lead_y += lead_y_change
        
        lead_x = lead_x + lead_x_change
        lead_y = lead_y + lead_y_change


        if not (lead_y_change == 0 and lead_x_change == 0):
            snakeX.pop(-1)
            snakeX.insert(0, lead_x)
            snakeY.pop(-1)
            snakeY.insert(0, lead_y)

        if lead_x >= displayX - 20 or lead_x < 0 + 20:
            lead_x_change = 0
            # lead_y_change = blockSize
            # keyX = True
            # keyY = False

        if lead_y >= displayY - 20 or lead_y < 0 + 20:
            lead_y_change = 0
            # lead_x_change = blockSize
            # keyY = True
            # keyX = False

        # print(lead_x, lead_y)
        distance = np.sqrt( ((foodX-lead_x)**2)+((foodY-lead_y)**2) )
        print(distance)
        #print(foodX,foodY)

        #if foodX - 10 <= lead_x <= foodX + 10 and foodY - 10 <= lead_y <= foodY + 10:
        if foodX == lead_x  and foodY == lead_y:

            foodX = randrange(borderSize, displayX-(2*borderSize)+10, 10)
            foodY = randrange(borderSize, displayY-(2*borderSize)+10, 10)
            score = score + 1
            scoreDisplay("you", red)
            increseLength(snakeX, snakeY)
            # pygame.display.update()
            
        

            

        gameDisplay.fill(black)
        # gameDisplay.blit(image, (0, 0))
        for i in range(1, len(snakeX)):
            pygame.draw.rect(gameDisplay, green, [snakeX[i], snakeY[i], blockSize, blockSize])
        pygame.draw.rect(gameDisplay, green, [lead_x, lead_y, blockSize, blockSize])

        pygame.draw.rect(gameDisplay, red, [0, 0, borderSize, displayY])
        pygame.draw.rect(gameDisplay, red, [0, 0, displayX, borderSize])
        pygame.draw.rect(gameDisplay, red, [0, displayY-borderSize, displayX, borderSize])
        pygame.draw.rect(gameDisplay, red, [displayX-borderSize, 0, borderSize, displayY])

        pygame.draw.rect(gameDisplay, red, [foodX, foodY, 10, 10])

        pygame.display.update()

        clock.tick(FPS)


snake()

pygame.quit()

quit()
