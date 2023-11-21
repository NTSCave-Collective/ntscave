import pygame
import os
import tiles

def draw_grid(gameObjects, screen_size, grid_color, grid_spacing):
    width, height = screen_size
    gridMap = [
        ["wallcorner_topleft","frontwall_center","frontwall_center","frontwall_center","frontwall_center","frontwall_center","frontwall_center","wallcorner_topright"],
        ["wall_left","floor","floor","floor","floor","floor","floor","wall_right"],
        ["wall_left","floor2","floor","floor","floor","floor","floor","wall_right","frontwall_left","frontwall_center","frontwall_right"],
        ["wall_left","floor3","floor3","floor","floor","floor","floor","wall_right"],
        ["wall_left","floor3","floor2","floor3","stairs_down","floor","floor3","wall_right"],
        ["wall_left","floor3","floor2","floor3","floor","floor","floor3","wall_right"],
        ["wall_left","floor3","floor","spike","spike1","spike2","spike3","wall_right"],
        ["wallcorner_bottomleft","wall_bottom","wall_bottom","wall_bottom","wall_bottom","wall_bottom","wall_bottom","wallcorner_bottomright"],
    ]


    for y in range(len(gridMap)):
        for x in range(len(gridMap[y])):
            image = pygame.image.load(os.path.join(tiles.tiles[gridMap[y][x]]))
            image = pygame.transform.scale(image, (64, 64))
            gameObjects.blit(image, (0 + 64 * x , 0 + 64 * y))