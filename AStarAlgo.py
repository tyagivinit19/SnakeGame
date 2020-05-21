import pygame
import numpy as np
import time
from random import randrange

pygame.init()

gameExit = False
width = 600
height = 600

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("A Star")
black = (0, 0, 0)
blue = pygame.Color("#035aa6")
status = True



class Spot():
    def __init__(self,i,j):
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
            pygame.draw.rect(gameDisplay, black, [self.i * w, self.j * h, w, h])
            return
        pygame.draw.rect(gameDisplay, black, [self.i * w, self.j * h, w, h], 1)
        
    def show(self, colr):
        pygame.draw.rect(gameDisplay, colr, [self.i * w, self.j * h, w, h])
        
    def addNeighbors(self, grid):
        i = self.i
        j = self.j
        
        if i < cols-1:
            self.neighbors.append(grid[i+1][j])
        if i > 0:
            self.neighbors.append(grid[i-1][j])
        if j < rows-1:
            self.neighbors.append(grid[i][j+1])
        if j > 0:
            self.neighbors.append(grid[i][j-1])


def hueristic(a, b):
    #d = np.sqrt( ((a.i-b.i)**2)+((a.j-b.j)**2) )
    d = abs(a.i-b.i) + abs(a.j-b.j)
    
    return d
        
print("hello")



#### Global variables

cols = 25
rows = 25
grid = [[] for _ in range(cols)]
w = width / cols
h = height / rows
path = []



######### Make Spot objects
for i in range(cols):
        for j in range(rows):
            grid[i].append(Spot(i, j))
            
            
########### Add Neighbors
for i in range(cols):
        for j in range(rows):
            grid[i][j].addNeighbors(grid)
            

openSet = []
closeSet = []

start = grid[0][0]
end = grid[cols-10][rows-6]
start.wall = False
end.wall = False
    

#print(grid.shape)
openSet.append(start)

while not gameExit:
    ### Pygame Content
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    gameDisplay.fill((255,255,255))
    
    if status:
        if len(openSet) > 0:
            winner = 0
            for i in range(len(openSet)):
                if openSet[i].f < openSet[winner].f:
                    winner = i
                    
            current = openSet[winner]
            
            if current == end:
                status = False
                print("All Done")
                #break;
                
            openSet.remove(current)
            closeSet.append(current)
            
            
            neighbors = current.neighbors
            for i in range(len(neighbors)):
                neighbor = neighbors[i]
                
                if (not(neighbor in closeSet)) and not neighbor.wall: 
                    tempG = current.g + 1
                    
                    if neighbor in openSet:
                        if tempG < neighbor.g:
                            neighbor.g = tempG
                            
                    else:
                        neighbor.g = tempG
                        openSet.append(neighbor)
                    
                    
                    neighbor.h = hueristic(neighbor, end)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.previous = current
                    
            
        else:
            print("No Solution")
            status = False
    
   
            
    for i in range(len(openSet)):
        openSet[i].show((0, 255, 0)) #Green
        
    for i in range(len(closeSet)):
        closeSet[i].show((255, 0, 0)) #Red
        
    
        
    for i in range(len(path)):
        path[i].show((0, 0, 255)) # may be blue
        
    path = []
    temp = current
    path.append(temp)
    while temp.previous:
        path.append(temp.previous)
        temp = temp.previous
            
        
    for i in range(cols):
       for j in range(rows):
           grid[i][j].showGrid()
           
    
    pygame.display.update()
#time.sleep(86400)
#while not resumed.wait(): # wait until resumed
    #"continue waiting"
    
pygame.quit()
quit()



























