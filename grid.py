import pygame
import os
import tiles

def draw_grid(gameObjects, screen_size, grid_color, grid_spacing):
    width, height = screen_size

    global gridMap
    gridMap = [
        ["frontwall_center","frontwall_center","frontwall_center","frontwall_center","frontwall_center","frontwall_center","frontwall_center","frontwall_center",],
        ["frontwall_center","floor","floor","floor","floor","floor","floor","frontwall_center",],
        ["frontwall_center","floor2","floor","floor","floor","floor","floor","frontwall_center","floor","frontwall_center","floor"],
        ["frontwall_center","floor","floor3","floor","floor","floor","floor","frontwall_center",],
        ["frontwall_center","floor","floor","floor","stairs_down","floor","floor","frontwall_center",],
        ["frontwall_center","floor","floor","floor","floor","floor","floor","frontwall_center",],
        ["frontwall_center","floor","floor","floor","floor","floor","floor2","frontwall_center",],
        ["frontwall_center","frontwall_center","frontwall_center","frontwall_center","frontwall_center","frontwall_center","frontwall_center","frontwall_center",],
    ]


    for y in range(len(gridMap)):
        for x in range(len(gridMap[y])):
            image = pygame.image.load(os.path.join(tiles.tiles[gridMap[y][x]]))
            image = pygame.transform.scale(image, (64, 64))
            gameObjects.blit(image, (0 + 64 * x , 0 + 64 * y))
