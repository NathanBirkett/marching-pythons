from time import sleep
import math
import pygame, sys, random
from pygame.locals import *
pygame.init()

BACKGROUND = (255, 255, 255)
RED = (255, 30, 70)
BLUE = (10, 20, 200)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 512
increment = WINDOW_WIDTH//16
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
points = [[False]*(WINDOW_WIDTH//increment)]*(WINDOW_WIDTH//increment)

def main():
    # print(is_contained(int(input("x:")), int(input("y:"))))
    draw()
    print(points)
    looping = True
    while looping :
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

def draw():
    WINDOW.fill(BACKGROUND)
    pygame.draw.line(WINDOW, BLACK, (WINDOW_WIDTH/2, 0), (WINDOW_WIDTH/2, WINDOW_HEIGHT), 2)
    pygame.draw.line(WINDOW, BLACK, (0, WINDOW_HEIGHT/2), (WINDOW_WIDTH, WINDOW_HEIGHT/2), 2)
    for x in range(-WINDOW_WIDTH//2, WINDOW_WIDTH//2+1, increment):
        for y in range(WINDOW_HEIGHT//2, -WINDOW_HEIGHT//2-1, -increment):
            pygame.draw.rect(WINDOW, RED, pygame.Rect(gx(x), gy(y), increment, increment), 1)
            if is_contained(x, y):
                pygame.draw.circle(WINDOW, GREEN, (gx(x), gy(y)), 3)
                points[int(gy(y)//increment)][int(gx(x)//increment)] = True
                
            if is_contained(x, y) and not is_contained(x+increment, y) and not is_contained(x, y-increment) and not is_contained(x+increment, y-increment):
                pygame.draw.line(WINDOW, BLUE, (gx(x), gy(y)+increment/2), (gx(x)+increment/2, gy(y)), 2)
                    
            if not is_contained(x, y) and is_contained(x+increment, y) and not is_contained(x, y-increment) and not is_contained(x+increment, y-increment):
                pygame.draw.line(WINDOW, BLUE, (gx(x)+increment/2, gy(y)), (gx(x)+increment, gy(y)+increment/2), 2)
                    
            if is_contained(x, y) and is_contained(x+increment, y) and not is_contained(x, y-increment) and not is_contained(x+increment, y-increment):
                pygame.draw.line(WINDOW, BLUE, (gx(x), gy(y)+increment/2), (gx(x)+increment, gy(y)+increment/2), 2)
                    
            if not is_contained(x, y) and not is_contained(x+increment, y) and is_contained(x, y-increment) and not is_contained(x+increment, y-increment):
                pygame.draw.line(WINDOW, BLUE, (gx(x), gy(y)+increment/2), (gx(x)+increment/2, gy(y)+increment), 2)
                    
            if is_contained(x, y) and not is_contained(x+increment, y) and is_contained(x, y-increment) and not is_contained(x+increment, y-increment):
                pygame.draw.line(WINDOW, BLUE, (gx(x)+increment/2, gy(y)), (gx(x)+increment/2, gy(y)+increment), 2)
                    
                # if not is_contained(x, y) and is_contained(x+increment, y) and is_contained(x, y-increment) and not is_contained(x+increment, y-increment) and not is_contained(x+increment/2, y-increment/2):
                #     pygame.draw.line(WINDOW, BLUE, (gx(x)+increment/2, gy(y)), (gx(x)+increment, gy(y)+increment/2), 2)
                #     pygame.draw.line(WINDOW, BLUE, (gx(x), gy(y)+increment/2), (gx(x)+increment/2, gy(y)+increment), 2)
                    
            if is_contained(x, y) and is_contained(x+increment, y) and is_contained(x, y-increment) and not is_contained(x+increment, y-increment):
                pygame.draw.line(WINDOW, BLUE, (gx(x)+increment/2, gy(y)+increment), (gx(x)+increment, gy(y)+increment/2), 2)
                    
            if not is_contained(x, y) and not is_contained(x+increment, y) and not is_contained(x, y-increment) and is_contained(x+increment, y-increment):
                pygame.draw.line(WINDOW, BLUE, (gx(x)+increment/2, gy(y)+increment), (gx(x)+increment, gy(y)+increment/2), 2)
                    
                
                # if is_contained(x, y) and not is_contained(x+increment, y) and not is_contained(x, y-increment) and is_contained(x+increment, y-increment):
                #     pygame.draw.line(WINDOW, BLUE, (gx(x), gy(y)+increment/2), (gx(x)+increment/2, gy(y)), 2)
                    
            if not is_contained(x, y) and is_contained(x+increment, y) and not is_contained(x, y-increment) and is_contained(x+increment, y-increment):
                pygame.draw.line(WINDOW, BLUE, (gx(x)+increment/2, gy(y)), (gx(x)+increment/2, gy(y)+increment), 2)
                
            if is_contained(x, y) and is_contained(x+increment, y) and not is_contained(x, y-increment) and is_contained(x+increment, y-increment):                
                pygame.draw.line(WINDOW, BLUE, (gx(x), gy(y)+increment/2), (gx(x)+increment/2, gy(y)+increment), 2)
                
            if not is_contained(x, y) and not is_contained(x+increment, y) and is_contained(x, y-increment) and is_contained(x+increment, y-increment):
                pygame.draw.line(WINDOW, BLUE, (gx(x), gy(y)+increment/2), (gx(x)+increment, gy(y)+increment/2), 2)
                
            if is_contained(x, y) and not is_contained(x+increment, y) and is_contained(x, y-increment) and is_contained(x+increment, y-increment):                
                pygame.draw.line(WINDOW, BLUE, (gx(x)+increment/2, gy(y)), (gx(x)+increment, gy(y)+increment/2), 2)
                
            if not is_contained(x, y) and is_contained(x+increment, y) and is_contained(x, y-increment) and is_contained(x+increment, y-increment):
                pygame.draw.line(WINDOW, BLUE, (gx(x), gy(y)+increment/2), (gx(x)+increment/2, gy(y)), 2)
                
    print("done")
    pygame.display.update()
    
def gx(x):
    return WINDOW_WIDTH/2+x

def gy(y):
    return WINDOW_HEIGHT/2-y

def is_contained(x,y):
    return math.cos(x) + 10*math.cos(x/10) - y <= 0

main()