from time import sleep
import math
import pygame, sys, random
from pygame.locals import *
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
RED = (255, 30, 70)
BLUE = (10, 20, 200)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
 
# Game Setup
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 512
increment = WINDOW_WIDTH//512
# str = input("equation: ")
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
 
# The main function that controls the game
def main () :
  looping = True

  # The main game loop
  while looping :
    print("hi")
  print("hello")
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
    
    # Processing
    # 25px
 
    # Render elements of the game
    print("hi")
    WINDOW.fill(BACKGROUND)
    pygame.draw.line(WINDOW, BLACK, (WINDOW_WIDTH/2, 0), (WINDOW_WIDTH/2, WINDOW_HEIGHT), 2)
    pygame.draw.line(WINDOW, BLACK, (0, WINDOW_HEIGHT/2), (WINDOW_WIDTH, WINDOW_HEIGHT/2), 2)
    for x in range(-1*WINDOW_WIDTH//2, WINDOW_WIDTH//2+1, increment):
        for y in range(-1*WINDOW_HEIGHT//2, WINDOW_HEIGHT//2+1, increment):
            # print(str(x) + ", " + str(y))
            # pygame.draw.rect(WINDOW, RED, pygame.Rect(gx(x), gy(y), increment, increment), 1)
            # if is_contained(x, -y):
            #     pygame.draw.circle(WINDOW, GREEN, (gx(x), gx(y)), 1)
            
            
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
                
    pygame.display.update()
    
def gx(x):
    return WINDOW_WIDTH/2+x

def gy(y):
    return WINDOW_HEIGHT/2-y

def is_contained(x,y):
    return 10*math.sin(x) + 50*math.sin(x/60) + x/2 - y <= 0
 
main()
