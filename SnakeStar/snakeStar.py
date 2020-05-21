# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:43:59 2020

@author: Dell
"""

import pygame
import numpy as np
# import time
from random import randrange


# =============================================================================
# ##############  A Star Algorithm  ##############
# =============================================================================

class AStar():

    def __init__(self):

        pygame.init()

        self.width = 600
        self.height = 600

        # =============================================================================
        #         self.gameDisplay = pygame.display.set_mode((self.width, self.height))
        #         pygame.display.set_caption("A Star")
        #         self.black = (0, 0, 0)
        #         self.blue = pygame.Color("#035aa6")
        # =============================================================================

        self.gameExit = False
        self.status = True

        self.cols = 30
        self.rows = 30
        self.grid = [[] for _ in range(self.cols)]
        self.w = self.width / self.cols
        self.h = self.height / self.rows
        self.path = []

        #### Make Objects
        for i in range(self.cols):
            for j in range(self.rows):
                self.grid[i].append(self.Spot(self, i, j))

        ########### Add Neighbors
        for i in range(self.cols):
            for j in range(self.rows):
                self.grid[i][j].addNeighbors(self.grid)

        self.openSet = []
        self.closeSet = []

        # self.start = self.grid[0][0]
        # self.end = self.grid[self.cols-10][self.rows-6]
        self.start = None
        self.end = None

        # self.start.wall = False
        # self.end.wall = False

    def getSpotObj(self):
        return self.Spot(self)

    class Spot():
        def __init__(self, aStar, i, j):
            self.aStar = aStar
            self.i = i
            self.j = j
            self.f = 0
            self.g = 0
            self.h = 0
            self.neighbors = []
            self.previous = None
            self.wall = False

            # if randrange(1, 10) < 3:
            #     self.wall = True

            if i == 0 or i == self.aStar.cols - 1 or j == 0 or j == self.aStar.rows - 1:
                self.wall = True

        # =============================================================================
        #         def showGrid(self):
        #             if self.wall:
        #                 pygame.draw.rect(self.aStar.gameDisplay, self.aStar.black, [self.i * self.aStar.w, self.j * self.aStar.h, self.aStar.w, self.aStar.h])
        #                 return
        #             pygame.draw.rect(self.aStar.gameDisplay, self.aStar.black, [self.i * self.aStar.w, self.j * self.aStar.h, self.aStar.w, self.aStar.h], 1)
        #
        #         def show(self, colr):
        #             pygame.draw.rect(self.aStar.gameDisplay, colr, [self.i * self.aStar.w, self.j * self.aStar.h, self.aStar.w, self.aStar.h])
        # =============================================================================

        def addNeighbors(self, grid):
            i = self.i
            j = self.j

            if i < (self.aStar.cols) - 1:
                self.neighbors.append(self.aStar.grid[i + 1][j])
            if i > 0:
                self.neighbors.append(self.aStar.grid[i - 1][j])
            if j < self.aStar.rows - 1:
                self.neighbors.append(self.aStar.grid[i][j + 1])
            if j > 0:
                self.neighbors.append(self.aStar.grid[i][j - 1])

    def hueristic(self, a, b):
        # d = np.sqrt( ((a.i-b.i)**2)+((a.j-b.j)**2) )
        d = abs(a.i - b.i) + abs(a.j - b.j)

        return d

    def main(self, startX, startY, endX, endY, snakeX, snakeY):

        # ,startX, startY, endX, endY
        obstacle = []

        for i in range(len(snakeX)):
            tempX = snakeX[i] / 20
            tempY = snakeY[i] / 20
            obstacle.append(self.grid[int(tempX)][int(tempY)])

        self.gameExit = False
        self.status = True

        # self.cols = 30
        # self.rows = 30
        # self.grid = [[] for _ in range(self.cols)]
        # self.w = self.width / self.cols
        # self.h = self.height / self.rows
        self.path = []

        self.openSet = []
        self.closeSet = []

        print("hello")

        self.start = self.grid[int(startX / 20)][int(startY / 20)]
        self.end = self.grid[int(endX / 20)][int(endY / 20)]

        #### Global variables

        ######### Make Spot objects

        coorPathX = []
        coorPathY = []

        # print(grid.shape)
        self.openSet.append(self.start)

        while not self.gameExit:
            ### Pygame Content
            # print("till")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameExit = True
            # self.gameDisplay.fill((255,255,255))

            if self.status:
                if len(self.openSet) > 0:
                    winner = 0
                    for i in range(len(self.openSet)):
                        if self.openSet[i].f < self.openSet[winner].f:
                            winner = i

                    current = self.openSet[winner]

                    if current == self.end:

                        self.status = False
                        self.path.insert(0,
                                         self.end)  #######################################################################
                        for itr in self.path:
                            ti = itr.i
                            tj = itr.j
                            coorPathX.append(ti * 20)
                            coorPathY.append(tj * 20)

                        coorPathX.reverse()
                        coorPathY.reverse()

                        pathXY = [coorPathX, coorPathY]
                        print(coorPathX, coorPathY)

                        print("All Done")
                        return pathXY
                        # break;

                    self.openSet.remove(current)
                    self.closeSet.append(current)

                    self.neighbors = current.neighbors
                    for i in range(len(self.neighbors)):

                        neighbor = self.neighbors[i]

                        if (not (neighbor in self.closeSet)) and not neighbor.wall and (not (neighbor in obstacle)):
                            tempG = current.g + 1

                            if neighbor in self.openSet:
                                if tempG < neighbor.g:
                                    neighbor.g = tempG

                            else:
                                neighbor.g = tempG
                                self.openSet.append(neighbor)

                            neighbor.h = self.hueristic(neighbor, self.end)
                            neighbor.f = neighbor.g + neighbor.h
                            neighbor.previous = current


                else:
                    print("No Solution")
                    self.status = False

            # for i in range(len(self.openSet)):
            #     self.openSet[i].show((0, 255, 0)) #Green

            # for i in range(len(self.closeSet)):
            #     self.closeSet[i].show((255, 0, 0)) #Red
            #     #print("Red")

            # for i in range(len(self.path)):
            #     self.path[i].show((0, 0, 255)) # may be blue
            #     print("Blue")

            self.path = []
            temp = current
            self.path.append(temp)
            while temp.previous:
                # print("loop")

                self.path.append(temp.previous)
                temp = temp.previous

            # for i in range(self.cols):
            #    for j in range(self.rows):
            #        self.grid[i][j].showGrid()

            # pygame.display.update()
        # time.sleep(86400)
        # while not resumed.wait(): # wait until resumed
        # "continue waiting"

        pygame.quit()
        quit()


# game = AStar()
# #spot = game.
# print("obj")
# game.main()


# =============================================================================
# ############## Snake Game Logic ########################
# =============================================================================


class Snake():
    def __init__(self, x, y, FPS):

        pygame.init()

        ###  A Star Algorithm #############

        self.aStar = AStar()

        self.displayX = x
        self.displayY = y

        self.blockSize = 20
        self.borderSize = self.blockSize

        # self.FPS = 15
        self.FPS = FPS

        self.lead_x = self.displayX / 2
        self.lead_y = self.displayY / 2
        self.lead_x_change = 0
        self.lead_y_change = 0
        self.keyX = True
        self.keyY = True

        self.snakeX = [self.lead_x]
        self.snakeY = [self.lead_y]

    # def scoreDisplay(self, score, color):
    # text = font.render(score, True, color)
    # gameDisplay.blit(text, [300, 300])
    # print("msg")

    def increseLength(self, snakeX, snakeY):
        snakeX.append(snakeX[-1] - self.blockSize)
        snakeY.append(snakeY[-1] - self.blockSize)
        print("Increase")

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

        # self.FPS = 15
        FPS = self.FPS

        green = pygame.Color("#00b906")
        blue = pygame.Color("#035aa6")
        # white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)

        gameDisplay = pygame.display.set_mode((displayX, displayY))
        pygame.display.set_caption("Snake")

        clock = pygame.time.Clock()

        # font = pygame.font.SysFont(None, 25)

        gameExit = False

        # lead_x = displayX / 2
        # lead_y = displayY / 2
        # lead_x_change = 0
        # lead_y_change = 0
        # keyX = True
        # keyY = True

        foodX = randrange(borderSize, displayX - (2 * borderSize) + blockSize, blockSize)
        foodY = randrange(borderSize, displayY - (2 * borderSize) + blockSize, blockSize)

        score = 0
        # temp=False

        # image = pygame.image.load("background.png")
        # image = pygame.transform.scale(image, (displayX, displayY))
        pathXY = []
        tempStar = AStar()
        pathXY = tempStar.main(self.lead_x, self.lead_y, foodX, foodY, self.snakeX, self.snakeY)
        pathX = pathXY[0]
        pathY = pathXY[1]
        # pathX.reverse()
        # pathY.reverse()
        tempCount = 0

        while not gameExit:
            print(self.lead_x, self.lead_y)
            print(self.snakeX, self.snakeY)
            print(foodX, foodY)
            # for i in range(len(self.snakeX)):
            #     print("new")
            #     pygame.draw.rect(gameDisplay, green, [self.snakeX[i], self.snakeY[i], blockSize, blockSize])
            # =============================================================================
            #
            #             ##############  Automation Logic  ################
            #             ###Logic For Walls
            #             if self.keyX and self.lead_x == displayX-(2*self.blockSize):
            #                 self.down()
            #             elif self.keyX and self.lead_x == self.blockSize:
            #                 self.up()
            #             elif self.keyY and self.lead_y == displayY-(2*self.blockSize):
            #                 self.left()
            #             elif self.keyY and self.lead_y == self.blockSize:
            #                 self.right()
            #
            #
            #
            #             ###Logic for Food
            #             if self.keyX and self.lead_x == foodX and foodY > self.lead_y:
            #                 self.down()
            #             elif self.keyX and self.lead_x == foodX and foodY < self.lead_y:
            #                 self.up()
            #             elif self.keyY and self.lead_y == foodY and foodX > self.lead_x:
            #                 self.right()
            #             elif self.keyY and self.lead_y == foodY and foodX < self.lead_x:
            #                 self.left()
            #
            #
            #
            #             #Logic For Stucking in Corners
            #             if self.lead_x==560 and self.lead_y==580:
            #                 self.left()
            #             elif self.lead_x==20 and self.lead_y==0:
            #                 self.right()
            #             elif self.lead_x==580 and self.lead_y==20:
            #                 self.down()
            #             elif self.lead_x==0 and self.lead_y==560:
            #                 self.up()
            #
            #
            #             ####### Automation Logic End   ##################
            #
            # =============================================================================

            for event in pygame.event.get():
                # print(event)

                if event.type == pygame.QUIT:
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.keyY and not self.lead_x == borderSize:
                        self.left()

                    elif event.key == pygame.K_RIGHT and self.keyY and not self.lead_x == displayX - (2 * borderSize):
                        self.right()

                    elif event.key == pygame.K_UP and self.keyX and not self.lead_y == borderSize:
                        self.up()

                    elif event.key == pygame.K_DOWN and self.keyX and not self.lead_y == displayY - (2 * borderSize):
                        self.down()

            # lead_x += lead_x_change
            # lead_y += lead_y_change

            # lead_x , lead_y, foodX, foodY||||startX, startY, endX, endY, obstacle

            self.lead_x = pathX[tempCount]
            self.lead_y = pathY[tempCount]
            tempCount = tempCount + 1

            self.snakeX.pop(-1)
            self.snakeX.insert(0, self.lead_x)
            self.snakeY.pop(-1)
            self.snakeY.insert(0, self.lead_y)

            # self.snakeX.pop(0)
            # self.snakeX.append(self.lead_x)
            # self.snakeY.pop(0)
            # self.snakeY.append(self.lead_y)

            # =============================================================================
            #             # self.lead_x = self.lead_x + self.lead_x_change
            #             # self.lead_y = self.lead_y + self.lead_y_change
            # =============================================================================

            # =============================================================================
            #             if not (self.lead_y_change == 0 and self.lead_x_change == 0):
            #                 self.snakeX.pop(-1)
            #                 self.snakeX.insert(0, self.lead_x)
            #                 self.snakeY.pop(-1)
            #                 self.snakeY.insert(0, self.lead_y)
            #
            #
            #             if self.lead_x >= displayX - (2*blockSize) or self.lead_x < 0 + (2*blockSize):
            #                 self.lead_x_change = 0
            #                 # lead_y_change = blockSize
            #                 # keyX = True
            #                 # keyY = False
            #
            #             if self.lead_y >= displayY - (2*blockSize) or self.lead_y < 0 + (2*blockSize):
            #                 self.lead_y_change = 0
            #                 # lead_x_change = blockSize
            #                 # keyY = True
            #                 # keyX = False
            # =============================================================================

            # print(lead_x, lead_y)
            distance = np.sqrt(((foodX - self.lead_x) ** 2) + ((foodY - self.lead_y) ** 2))
            # print(distance)
            # print(foodX,foodY)
            print(score)
            # print("Lead", self.lead_x, self.lead_y)

            # if temp:
            # print("Back", self.snakeX[1], self.snakeY[1])

            # if foodX - 10 <= lead_x <= foodX + 10 and foodY - 10 <= lead_y <= foodY + 10:
            if foodX == self.lead_x and foodY == self.lead_y:
                print("Food")
                foodX = randrange(borderSize, displayX - (2 * borderSize) + blockSize, blockSize)
                foodY = randrange(borderSize, displayY - (2 * borderSize) + blockSize, blockSize)
                score = score + 1
                # self.scoreDisplay("you", red)
                self.increseLength(self.snakeX, self.snakeY)

                tempStar = AStar()
                pathXY = tempStar.main(self.lead_x, self.lead_y, foodX, foodY, self.snakeX, self.snakeY)
                print("Color")
                pathX = pathXY[0]
                pathY = pathXY[1]
                # pathX.reverse()
                # pathY.reverse()
                tempCount = 0

                # temp = True
                # pygame.display.update()

            gameDisplay.fill(black)
            # gameDisplay.blit(image, (0, 0))
            # self.snakeX.reverse()
            # self.snakeY.reverse()
            for i in range(1, len(self.snakeX)):
                # print("snake color")
                pygame.draw.rect(gameDisplay, green, [self.snakeX[i], self.snakeY[i], blockSize, blockSize])
            pygame.draw.rect(gameDisplay, green, [self.lead_x, self.lead_y, blockSize, blockSize])
            # self.snakeX.reverse()
            # self.snakeY.reverse()
            pygame.draw.rect(gameDisplay, red, [0, 0, borderSize, displayY])
            pygame.draw.rect(gameDisplay, red, [0, 0, displayX, borderSize])
            pygame.draw.rect(gameDisplay, red, [0, displayY - borderSize, displayX, borderSize])
            pygame.draw.rect(gameDisplay, red, [displayX - borderSize, 0, borderSize, displayY])

            pygame.draw.rect(gameDisplay, blue, [foodX, foodY, blockSize, blockSize])

            pygame.display.update()

            clock.tick(FPS)
        pygame.quit()
        quit()


ob = Snake(600, 600, 60)
ob.snake_run()

# snake()
