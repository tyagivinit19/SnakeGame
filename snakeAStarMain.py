# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:07:02 2020

@author: Dell
"""

from random import randrange
import pygame
import numpy as np




class Snake():
    def __init__(self, x, y, FPS):

        pygame.init()

        self.displayX = x
        self.displayY = y



        self.blockSize = 20
        self.borderSize = self.blockSize

        #self.FPS = 15
        self.FPS = FPS

        self.lead_x = self.displayX / 2
        self.lead_y = self.displayY / 2
        self.lead_x_change = 0
        self.lead_y_change = 0
        self.keyX = True
        self.keyY = True

        self.snakeX = [self.lead_x]
        self.snakeY = [self.lead_y]


    #def scoreDisplay(self, score, color):
        #text = font.render(score, True, color)
        #gameDisplay.blit(text, [300, 300])
        #print("msg")


    def increseLength(self, snakeX, snakeY):
        snakeX.append(snakeX[-1] - self.blockSize)
        snakeY.append(snakeY[-1] - self.blockSize)

    def up(self):
        self.lead_y_change = -self.blockSize
        self.lead_x_change = 0
        self.keyX = False
        self.keyY = True
        print("up")

    def down(self):
        self.lead_y_change = self.blockSize
        self.lead_x_change = 0
        self.keyX = False
        self.keyY = True
        print("down")

    def left(self):
        self.lead_x_change = -self.blockSize
        self.lead_y_change = 0
        self.keyX = True
        self.keyY = False
        print("left")

    def right(self):
        self.lead_x_change = self.blockSize
        self.lead_y_change = 0
        self.keyX = True
        self.keyY = False
        print("right")


    def snake_run(self):


        displayX = self.displayX
        displayY = self.displayY



        blockSize = self.blockSize
        borderSize = self.blockSize

        #self.FPS = 15
        FPS = self.FPS
        bodyClr = pygame.Color("#79d70f")
        headClr = pygame.Color("#d32626")
        borderClr = pygame.Color("#f5a31a")
        foodClr = pygame.Color("#edf4f2")

        green = pygame.Color("#00b906")
        blue = pygame.Color("#035aa6")
        #white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)

        gameDisplay = pygame.display.set_mode((displayX, displayY))
        pygame.display.set_caption("Snake")

        clock = pygame.time.Clock()

        #font = pygame.font.SysFont(None, 25)

        gameExit = False

        #lead_x = displayX / 2
        #lead_y = displayY / 2
        #lead_x_change = 0
        #lead_y_change = 0
        #keyX = True
        #keyY = True

        foodX = randrange(borderSize, displayX-(2*borderSize)+blockSize, blockSize)
        foodY = randrange(borderSize, displayY-(2*borderSize)+blockSize, blockSize)

        score = 0
        #temp=False

        # image = pygame.image.load("background.png")
        # image = pygame.transform.scale(image, (displayX, displayY))



        while not gameExit:

            #
            # ##############  Automation Logic  ################
            # ###Logic For Walls
            # if self.keyX and self.lead_x == displayX-(2*self.blockSize):
            #     self.down()
            # elif self.keyX and self.lead_x == self.blockSize:
            #     self.up()
            # elif self.keyY and self.lead_y == displayY-(2*self.blockSize):
            #     self.left()
            # elif self.keyY and self.lead_y == self.blockSize:
            #     self.right()
            #
            #
            #
            # ###Logic for Food
            # if self.keyX and self.lead_x == foodX and foodY > self.lead_y:
            #     self.down()
            # elif self.keyX and self.lead_x == foodX and foodY < self.lead_y:
            #     self.up()
            # elif self.keyY and self.lead_y == foodY and foodX > self.lead_x:
            #     self.right()
            # elif self.keyY and self.lead_y == foodY and foodX < self.lead_x:
            #     self.left()
            #
            #
            #
            # #Logic For Stucking in Corners
            # if self.lead_x==560 and self.lead_y==580:
            #     self.left()
            # elif self.lead_x==20 and self.lead_y==0:
            #     self.right()
            # elif self.lead_x==580 and self.lead_y==20:
            #     self.down()
            # elif self.lead_x==0 and self.lead_y==560:
            #     self.up()
            #
            #
            # ####### Automation Logic End   ##################
            #


            for event in pygame.event.get():
                # print(event)

                if event.type == pygame.QUIT:
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.keyY and not self.lead_x == borderSize:
                        self.left()

                    elif event.key == pygame.K_RIGHT and self.keyY and not self.lead_x == displayX-(2*borderSize):
                        self.right()

                    elif event.key == pygame.K_UP and self.keyX and not self.lead_y == borderSize:
                        self.up()

                    elif event.key == pygame.K_DOWN and self.keyX and not self.lead_y == displayY-(2*borderSize):
                       self.down()

            #lead_x += lead_x_change
            #lead_y += lead_y_change

            self.lead_x = self.lead_x + self.lead_x_change
            self.lead_y = self.lead_y + self.lead_y_change

            if not (self.lead_y_change == 0 and self.lead_x_change == 0):
                self.snakeX.pop(-1)
                self.snakeX.insert(0, self.lead_x)
                self.snakeY.pop(-1)
                self.snakeY.insert(0, self.lead_y)


            if self.lead_x >= displayX - (2*blockSize) or self.lead_x < 0 + (2*blockSize):
                self.lead_x_change = 0
                # lead_y_change = blockSize
                # keyX = True
                # keyY = False

            if self.lead_y >= displayY - (2*blockSize) or self.lead_y < 0 + (2*blockSize):
                self.lead_y_change = 0
                # lead_x_change = blockSize
                # keyY = True
                # keyX = False








            # print(lead_x, lead_y)
            distance = np.sqrt( ((foodX-self.lead_x)**2)+((foodY-self.lead_y)**2) )
            #print(distance)
            #print(foodX,foodY)
            print(score)
            #print("Lead", self.lead_x, self.lead_y)


            #if temp:
                #print("Back", self.snakeX[1], self.snakeY[1])

            #if foodX - 10 <= lead_x <= foodX + 10 and foodY - 10 <= lead_y <= foodY + 10:
            if foodX == self.lead_x  and foodY == self.lead_y:

                foodX = randrange(borderSize, displayX-(2*borderSize)+blockSize, blockSize)
                foodY = randrange(borderSize, displayY-(2*borderSize)+blockSize, blockSize)
                score = score + 1
                #self.scoreDisplay("you", red)
                self.increseLength(self.snakeX, self.snakeY)
                #temp = True
                # pygame.display.update()





            gameDisplay.fill(black)
            # gameDisplay.blit(image, (0, 0))
            for i in range(1, len(self.snakeX)):
                pygame.draw.rect(gameDisplay, bodyClr, [self.snakeX[i], self.snakeY[i], blockSize, blockSize], 3)
            pygame.draw.rect(gameDisplay, headClr, [self.lead_x, self.lead_y, blockSize, blockSize], 10)
            # self.snakeX.reverse()
            # self.snakeY.reverse()
            pygame.draw.rect(gameDisplay, borderClr, [0, 0, borderSize, displayY])
            pygame.draw.rect(gameDisplay, borderClr, [0, 0, displayX, borderSize])
            pygame.draw.rect(gameDisplay, borderClr, [0, displayY - borderSize, displayX, borderSize])
            pygame.draw.rect(gameDisplay, borderClr, [displayX - borderSize, 0, borderSize, displayY])

            pygame.draw.rect(gameDisplay, foodClr, [foodX, foodY, blockSize, blockSize])

            pygame.display.update()

            clock.tick(FPS)
        pygame.quit()
        quit()

ob = Snake(600,600,15)
ob.snake_run()


#snake()


