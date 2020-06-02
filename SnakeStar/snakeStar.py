# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:43:59 2020

@author: Dell
"""

# import time
from random import randrange

import pygame


# =============================================================================
# ##############  A Star Algorithm  ##############
# =============================================================================

class AStar:

    def __init__(self):

        pygame.init()
        self.neighbors = None
        self.width = 600
        self.height = 600

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

    class Spot:

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

        def addNeighbors(self, grid):
            i = self.i
            j = self.j

            if i < self.aStar.cols - 1:
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

        self.path = []

        # print("hello")

        self.start = self.grid[int(startX / 20)][int(startY / 20)]
        self.end = self.grid[int(endX / 20)][int(endY / 20)]

        coorPathX = []
        coorPathY = []

        self.openSet.append(self.start)

        while not self.gameExit:

            # print("till")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameExit = True

            if self.status:
                # print("openSet: ", self.openSet)
                if len(self.openSet) > 0:
                    winner = 0
                    for i in range(len(self.openSet)):
                        if self.openSet[i].f < self.openSet[winner].f:
                            winner = i

                    current = self.openSet[winner]

                    if current == self.end:

                        self.status = False
                        self.path.insert(0, self.end)
                        for itr in self.path:
                            ti = itr.i
                            tj = itr.j
                            coorPathX.append(ti * 20)
                            coorPathY.append(tj * 20)

                        coorPathX.reverse()
                        coorPathY.reverse()

                        pathXY = [coorPathX, coorPathY]
                        # print(coorPathX, coorPathY)

                        # print("All Done")
                        return pathXY
                        # break;

                    self.openSet.remove(current)
                    # print("openSet: ", len(self.openSet))

                    self.closeSet.append(current)
                    # print("closeSet: ", len(self.closeSet))

                    self.neighbors = current.neighbors
                    for i in range(len(self.neighbors)):

                        neighbor = self.neighbors[i]

                        if (not (neighbor in self.closeSet)) and not neighbor.wall and (not (neighbor in obstacle)):
                            tempG = current.g + 1
                            # print("neighbors: ", len(self.neighbors))

                            if neighbor in self.openSet:
                                if tempG < neighbor.g:
                                    neighbor.g = tempG

                            else:
                                neighbor.g = tempG
                                self.openSet.append(neighbor)

                                # print("neighbor: ", neighbor)
                                # print("append in openSet")

                            neighbor.h = self.hueristic(neighbor, self.end)
                            neighbor.f = neighbor.g + neighbor.h
                            neighbor.previous = current


                else:
                    # print("No Solution")
                    self.status = False
                    self.path = []
                    temp = current
                    self.path.append(temp)

                    while temp.previous:
                        self.path.append(temp.previous)
                        temp = temp.previous

                    for itr in self.path:
                        ti = itr.i
                        tj = itr.j
                        coorPathX.append(ti * 20)
                        coorPathY.append(tj * 20)

                    coorPathX.reverse()
                    coorPathY.reverse()

                    pathXY = [coorPathX, coorPathY]
                    # print(coorPathX, coorPathY)

                    # print("All Done")
                    return pathXY

            self.path = []
            temp = current
            self.path.append(temp)
            while temp.previous:
                # print("loop")

                self.path.append(temp.previous)
                temp = temp.previous

        pygame.quit()
        quit()


# =============================================================================
# ############## Snake Game Logic ########################
# =============================================================================


class Snake:

    def __init__(self, x, y, FPS):

        pygame.init()

        # A Star Object #############

        self.aStar = AStar()

        self.displayX = x
        self.displayY = y

        self.blockSize = 20
        self.borderSize = self.blockSize

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
        # print("Increase")

    def snake_run(self):

        displayX = self.displayX
        displayY = self.displayY

        blockSize = self.blockSize
        borderSize = self.blockSize

        FPS = self.FPS

        # green = pygame.Color("#00b906")
        # blue = pygame.Color("#035aa6")
        # white = (255, 255, 255)
        # red = (255, 0, 0)
        black = (0, 0, 0)

        bodyClr = pygame.Color("#79d70f")
        headClr = pygame.Color("#d32626")
        borderClr = pygame.Color("#f5a31a")
        foodClr = pygame.Color("#edf4f2")

        gameDisplay = pygame.display.set_mode((displayX, displayY))
        pygame.display.set_caption("Snake")

        clock = pygame.time.Clock()

        # font = pygame.font.SysFont(None, 25)

        gameExit = False

        foodX = randrange(borderSize, displayX - (2 * borderSize) + blockSize, blockSize)
        foodY = randrange(borderSize, displayY - (2 * borderSize) + blockSize, blockSize)

        score = 0

        # image = pygame.image.load("background.png")
        # image = pygame.transform.scale(image, (displayX, displayY))
        # pathXY = []

        tempStar = AStar()
        pathXY = tempStar.main(self.lead_x, self.lead_y, foodX, foodY, self.snakeX, self.snakeY)
        pathX = pathXY[0]
        pathY = pathXY[1]
        tempCount = 0

        while not gameExit:
            # print(self.lead_x, self.lead_y)
            # print(self.snakeX, self.snakeY)
            # print(foodX, foodY)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    gameExit = True

            self.lead_x = pathX[tempCount]
            self.lead_y = pathY[tempCount]
            tempCount = tempCount + 1

            self.snakeX.pop(-1)
            self.snakeX.insert(0, self.lead_x)

            self.snakeY.pop(-1)
            self.snakeY.insert(0, self.lead_y)

            # print(lead_x, lead_y)
            # distance = np.sqrt(((foodX - self.lead_x) ** 2) + ((foodY - self.lead_y) ** 2))
            # print(distance)
            # print(foodX,foodY)

            # print("Lead", self.lead_x, self.lead_y)

            if self.lead_x == pathX[-1] and self.lead_y == pathY[-1]:
                tempStar = AStar()
                pathXY = tempStar.main(self.lead_x, self.lead_y, foodX, foodY, self.snakeX, self.snakeY)
                # print("Color")
                pathX = pathXY[0]
                pathY = pathXY[1]
                tempCount = 0

            if foodX == self.lead_x and foodY == self.lead_y:
                # print("Food")
                foodX = randrange(borderSize, displayX - (2 * borderSize) + blockSize, blockSize)
                foodY = randrange(borderSize, displayY - (2 * borderSize) + blockSize, blockSize)

                tempFood = True
                while tempFood:
                    foodX = randrange(borderSize, displayX - (2 * borderSize) + blockSize, blockSize)
                    foodY = randrange(borderSize, displayY - (2 * borderSize) + blockSize, blockSize)
                    if foodX in self.snakeX and foodY in self.snakeY:
                        if self.snakeX.index(foodX) == self.snakeY.index(foodY):
                            pass
                        else:
                            tempFood = False

                    else:
                        tempFood = False

                score = score + 1
                print("Score: ", score)
                self.increseLength(self.snakeX, self.snakeY)

                tempStar = AStar()
                pathXY = tempStar.main(self.lead_x, self.lead_y, foodX, foodY, self.snakeX, self.snakeY)
                # print("Color")
                pathX = pathXY[0]
                pathY = pathXY[1]
                tempCount = 0

            mergeXY = list(zip(self.snakeX, self.snakeY))

            if len(set(mergeXY[1:])) <= len(mergeXY[1:]) <= len(set(mergeXY[1:])) + 10:
                pass

            else:
                print("Game Over")
                break;

            gameDisplay.fill(black)
            # gameDisplay.blit(image, (0, 0))

            # Snake Body
            for i in range(1, len(self.snakeX)):
                pygame.draw.rect(gameDisplay, bodyClr, [self.snakeX[i], self.snakeY[i], blockSize, blockSize], 3)

            # Snake Head
            pygame.draw.rect(gameDisplay, headClr, [self.lead_x, self.lead_y, blockSize, blockSize], 10)

            # Borders
            pygame.draw.rect(gameDisplay, borderClr, [0, 0, borderSize, displayY])
            pygame.draw.rect(gameDisplay, borderClr, [0, 0, displayX, borderSize])
            pygame.draw.rect(gameDisplay, borderClr, [0, displayY - borderSize, displayX, borderSize])
            pygame.draw.rect(gameDisplay, borderClr, [displayX - borderSize, 0, borderSize, displayY])

            # Food
            pygame.draw.rect(gameDisplay, foodClr, [foodX, foodY, blockSize, blockSize])

            pygame.display.update()

            clock.tick(FPS)
        pygame.quit()
        quit()


ob = Snake(600, 600, 60)
ob.snake_run()
