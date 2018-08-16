# Imports first, define variables to access methods
import pygame
import sys
from pygame.locals import *
from config import *

# map.renderMap()
# Start up pygame, must come before any other code using pygame
pygame.init()

# Start window
DISPLAYSURF = pygame.display.set_mode((400, 400), 0, 32)

pygame.display.set_caption('jobyEm')

# Runtime Loop


def drawMap():

    testMap = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 1, 1, 1, 1, 1, 1, 1, 1, 0,
               0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
               0, 1, 1, 1, 0, 0, 1, 1, 1, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]

    GRIDSIZE = 10
    LENGTH = len(testMap)

    WIDTH = int(LENGTH / GRIDSIZE)
    HEIGHT = int(LENGTH / GRIDSIZE)

    BGXY = [(0 - GRIDSIZE), 0]

    for i in testMap:

        # Top Left XY Coordinates
        if BGXY[0] == (LENGTH - GRIDSIZE):
            BGXY[0] = 0 - GRIDSIZE  # Reset X coordinates to 0
            # Adjust Y Coordinates to next row
            BGXY[1] = BGXY[1] + GRIDSIZE
        BGXY[0] = BGXY[0] + GRIDSIZE

        # Bottom Right XY Coordinates

        if i == 0:
            print('Grass')
            print(BGXY)
        pygame.draw.rect(DISPLAYSURF, RED,
                         (BGXY[0], BGXY[1], GRIDSIZE, GRIDSIZE))

        if i == 1:
            print('Wall')
            print(BGXY)
            pygame.draw.rect(DISPLAYSURF, WHITE,
                             (BGXY[0], BGXY[1], GRIDSIZE, GRIDSIZE))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    drawMap()
