# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:07:27 2020

@author: Dell
"""

import pygame
import numpy as np
import time
from random import randrange




class AStar():
    
    def __init__(self):
        
        
        pygame.init()

        self.width = 600
        self.height = 600
        
        self.gameDisplay = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("A Star")
        self.black = (0, 0, 0)
        self.blue = pygame.Color("#035aa6")
        
        self.gameExit = False
        self.status = True
        
        self.cols = 50
        self.rows = 50
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
        
        self.start = self.grid[0][0]
        self.end = self.grid[self.cols-10][self.rows-6]
        self.start.wall = False
        self.end.wall = False
        
    def getSpotObj(self):
        return self.Spot(self)
            
    
    class Spot():
        def __init__(self,aStar,i,j):
            self.aStar = aStar
            self.i = i
            self.j = j
            self.f = 0
            self.g = 0
            self.h = 0
            self.neighbors = []
            self.previous = None
            self.wall = False
            
            if randrange(1, 10) < 3:
                self.wall = True
            
            
            
            
        def showGrid(self):
            if self.wall:
                pygame.draw.rect(self.aStar.gameDisplay, self.aStar.black, [self.i * self.aStar.w, self.j * self.aStar.h, self.aStar.w, self.aStar.h])
                return
            pygame.draw.rect(self.aStar.gameDisplay, self.aStar.black, [self.i * self.aStar.w, self.j * self.aStar.h, self.aStar.w, self.aStar.h], 1)
            
        def show(self, colr):
            pygame.draw.rect(self.aStar.gameDisplay, colr, [self.i * self.aStar.w, self.j * self.aStar.h, self.aStar.w, self.aStar.h])
            
        def addNeighbors(self, grid):
            i = self.i
            j = self.j
            
            if i < (self.aStar.cols)-1:
                self.neighbors.append(self.aStar.grid[i+1][j])
            if i > 0:
                self.neighbors.append(self.aStar.grid[i-1][j])
            if j < self.aStar.rows-1:
                self.neighbors.append(self.aStar.grid[i][j+1])
            if j > 0:
                self.neighbors.append(self.aStar.grid[i][j-1])
        






    def hueristic(self, a, b):
        #d = np.sqrt( ((a.i-b.i)**2)+((a.j-b.j)**2) )
        d = abs(a.i-b.i) + abs(a.j-b.j)
        
        return d
        
    def main(self):
        
        
        
        print("hello")
        
        
        
        #### Global variables
        
        
        
        
        
        ######### Make Spot objects
        
                    
        
        
            
        
        #print(grid.shape)
        self.openSet.append(self.start)
        
        while not self.gameExit:
            ### Pygame Content
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     self.gameExit = True
            self.gameDisplay.fill((255,255,255))
            
            if self.status:
                if len(self.openSet) > 0:
                    winner = 0
                    for i in range(len(self.openSet)):
                        if self.openSet[i].f < self.openSet[winner].f:
                            winner = i
                            
                    current = self.openSet[winner]
                    
                    if current == self.end:
                        self.status = False
                        print("All Done")
                        #break;
                        
                    self.openSet.remove(current)
                    self.closeSet.append(current)
                    
                    
                    self.neighbors = current.neighbors
                    for i in range(len(self.neighbors)):
                        neighbor = self.neighbors[i]
                        
                        if (not(neighbor in self.closeSet)) and not neighbor.wall: 
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
            
           
                    
            for i in range(len(self.openSet)):
                self.openSet[i].show((0, 255, 0)) #Green
                
            for i in range(len(self.closeSet)):
                self.closeSet[i].show((255, 0, 0)) #Red
                #print("Red")
                
            for i in range(len(self.path)):
                self.path[i].show((0, 0, 255)) # may be blue
                print("Blue")
                  
           
                
            self.path = []
            temp = current
            self.path.append(temp)
            while temp.previous:
                self.path.append(temp.previous)
                temp = temp.previous
                    
           
                
            for i in range(self.cols):
               for j in range(self.rows):
                   self.grid[i][j].showGrid()
                   
            
            pygame.display.update()
        #time.sleep(86400)
        #while not resumed.wait(): # wait until resumed
            #"continue waiting"
            
        pygame.quit()
        quit()


game = AStar()
#spot = game.
print("obj")
game.main()
            




























