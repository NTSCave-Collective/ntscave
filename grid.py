import pygame
import os
import tiles
import CONSTANTS

def draw_grid(gameObjects, screen_size):
    width, height = screen_size
    gridMap = CONSTANTS.MAP

    for y in range(len(gridMap)):
        for x in range(len(gridMap[y])):
            try:
                image = pygame.image.load(os.path.join(tiles.tiles[gridMap[y][x]]))
                image = pygame.transform.scale(image, (CONSTANTS.PIXELS, CONSTANTS.PIXELS))
                gameObjects.blit(image, (CONSTANTS.PIXELS * x , CONSTANTS.PIXELS * y))
            except:
                pass
