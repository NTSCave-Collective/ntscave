import pygame
import os

def draw_grid(gameObjects, screen_size, grid_color, grid_spacing):
    width, height = screen_size
    gridMap = [
        [1,1,1,1,1,1,1,1,],
        [1,0,0,0,0,0,0,1,],
        [1,0,0,0,0,0,0,1,0,1,0],
        [1,0,0,0,0,0,0,1,],
        [1,0,0,0,0,0,0,1,],
        [1,0,0,0,0,0,0,1,],
        [1,0,0,0,0,0,0,1,],
        [1,1,1,1,1,1,1,1,],
    ]


    for y in range(len(gridMap)):
        for x in range(len(gridMap[y])):
            match gridMap[y][x]:
                case 0:
                    image = pygame.image.load(os.path.join('data', '../assets/tiles/blackstone.png'))
                    image = pygame.transform.scale(image, (64, 64))
                    gameObjects.blit(image, (0 + 64 * x , 0 + 64 * y))
                case 1:
                    image = pygame.image.load(os.path.join('data', '../assets/tiles/floor.png'))
                    image = pygame.transform.scale(image, (64, 64))
                    gameObjects.blit(image, (0 + 64 * x , 0 + 64 * y))