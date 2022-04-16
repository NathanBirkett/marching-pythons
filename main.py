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
points = [[False for i in range(WINDOW_WIDTH//increment+1)] for j in range(WINDOW_WIDTH//increment+1)]

def main():
    # print(is_contained(int(input("x:")), int(input("y:"))))
    print(points[8][8])
    draw()
    print(points)
    print(points[8][8])
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
                # pygame.draw.circle(WINDOW, GREEN, (gx(x), gy(y)), 3)
                print(str(int(gx(x)/increment)) + ", " + str(int(gy(y)/increment)))
                if int(gx(x)/increment) == 1 and int(gy(y)/increment) == 8:
                    print(points[8][8])
                points[int(gx(x)/increment)][int(gy(y)/increment)] = True
                if points[8][8] == True:
                    print("is True")
            if points[int(gx(x)/increment)][int(gy(y)/increment)] == True:
                pygame.draw.circle(WINDOW, GREEN, (gx(x), gy(y)), 3)
                
    for x in range(-WINDOW_WIDTH//2, WINDOW_WIDTH//2, increment):
        for y in range(WINDOW_HEIGHT//2, -WINDOW_HEIGHT//2, -increment):
            if check_box(x, y) == [True, False, False, False]:
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

def check_box(_x,_y):
    x = int(gx(_x)/increment)
    y = int(gy(_y)/increment)
    # print(_x, _y)
    # print([points[x][y], points[x+1][y], points[x][y+1], points[x+1][y+1]])
    if [points[x][y], points[x+1][y], points[x][y+1], points[x+1][y+1]] == [True, False, False, False]:
        return [True, False, False, False]
    if [points[x][y], points[x+1][y], points[x][y+1], points[x+1][y+1]] == [False, True, False, False]:
        return [False, True, False, False]
    if [points[x][y], points[x+1][y], points[x][y+1], points[x+1][y+1]] == [True, True, False, False]:
        return [True, True, False, False]
    if [points[x][y], points[x+1][y], points[x][y+1], points[x+1][y+1]] == [False, False, True, False]:
        return [False, False, True, False]
    if [points[x][y], points[x+1][y], points[x][y+1], points[x+1][y+1]] == [True, False, True, False]:
        return [True, False, True, False]
    if [points[x][y], points[x+1][y], points[x][y+1], points[x+1][y+1]] == [False, True, True, False]:
        return [False, True, True, False]
    if [points[x][y], points[x+1][y], points[x][y+1], points[x+1][y+1]] == [True, True, True, False]:
        return [True, True, True, False]
    if [points[x][y], points[x+1][y], points[x][y+1], points[x+1][y+1]] == [False, False, False, True]:
        return [False, False, False, True]
    if [points[x][y], points[x+1][y], points[x][y+1], points[x+1][y+1]] == [True, False, False, True]:
        return [True, False, False, True]
    if [points[x][y], points[x+1][y], points[x][y+1], points[x+1][y+1]] == [False, True, False, True]:
        return [False, True, False, True]
    if [points[x][y], points[x+1][y], points[x][y+1], points[x+1][y+1]] == [True, True, False, True]:
        return [True, True, False, True]
    if [points[x][y], points[x+1][y], points[x][y+1], points[x+1][y+1]] == [False, False, True, True]:
        return [False, False, True, True]
    if [points[x][y], points[x+1][y], points[x][y+1], points[x+1][y+1]] == [True, False, True, True]:
        return [True, False, True, True]
    if [points[x][y], points[x+1][y], points[x][y+1], points[x+1][y+1]] == [False, True, True, True]:
        return [False, True, True, True]

main()