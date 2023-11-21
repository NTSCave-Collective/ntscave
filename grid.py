import pygame
import os
import tiles
import CONSTANTS

def draw_grid(gameObjects, screen_size, grid_color, grid_spacing):
    width, height = screen_size
    global gridMap
    gridMap = CONSTANTS.BACKGROUND_IMAGES


    for y in range(len(gridMap)):
        for x in range(len(gridMap[y])):
            image = pygame.image.load(os.path.join(tiles.tiles[gridMap[y][x]]))
            image = pygame.transform.scale(image, (CONSTANTS.PIXELS, CONSTANTS.PIXELS))
            gameObjects.blit(image, (CONSTANTS.PIXELS * x , CONSTANTS.PIXELS * y))
