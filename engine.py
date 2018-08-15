# Imports first, define variables to access methods
import pygame
import sys
from pygame.locals import *
from config import *

# Start up pygame, must come before any other code using pygame
pygame.init()

# Start window
DISPLAYSURF = pygame.display.set_mode((400, 400), 0, 32)

pygame.display.set_caption('jobyEm')

# Runtime Loop


def drawMap():

    pygame.draw.rect(DISPLAYSURF, RED, (0, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, WHITE, (20, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, RED, (40, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, WHITE, (60, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, RED, (80, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, WHITE, (100, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, RED, (120, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, WHITE, (140, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, RED, (160, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, WHITE, (180, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, RED, (200, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, WHITE, (220, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, RED, (240, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, WHITE, (260, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, RED, (280, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, WHITE, (300, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, RED, (320, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, WHITE, (340, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, RED, (360, 0, 20, 20))
    pygame.draw.rect(DISPLAYSURF, WHITE, (380, 0, 20, 20))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    drawMap()
