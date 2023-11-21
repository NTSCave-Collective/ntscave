import pygame
import CONSTANTS
import os

def draw_grid(window, screen_size, player_position):
    width, height = screen_size
    player_x, player_y = player_position

    offset_x = (player_x % CONSTANTS.GRID_SPACING) - CONSTANTS.GRID_SPACING
    offset_y = (player_y % CONSTANTS.GRID_SPACING) - CONSTANTS.GRID_SPACING

    expansion_left = max(0, CONSTANTS.EXPANSION_THRESHOLD - player_x)
    expansion_right = max(0, CONSTANTS.EXPANSION_THRESHOLD - (width - player_x))
    expansion_top = max(0, CONSTANTS.EXPANSION_THRESHOLD - player_y)
    expansion_bottom = max(0, CONSTANTS.EXPANSION_THRESHOLD - (height - player_y))

    for x in range(offset_x - expansion_left, width + expansion_right, CONSTANTS.GRID_SPACING):
        pygame.draw.line(window, CONSTANTS.GRID_COLOR, (x, 0), (x, height))
    for y in range(offset_y - expansion_top, height + expansion_bottom, CONSTANTS.GRID_SPACING):
        pygame.draw.line(window, CONSTANTS.GRID_COLOR, (0, y), (width, y))

    image = pygame.image.load(os.path.join('data', '../assets/tiles/blackstone.png'))

    for x in range(offset_x - expansion_left, width + expansion_right, CONSTANTS.GRID_SPACING):
        for y in range(offset_y - expansion_top, height + expansion_bottom, CONSTANTS.GRID_SPACING):
            window.blit(image, (x + CONSTANTS.GRID_SPACING // 2 - image.get_width() // 2, y + CONSTANTS.GRID_SPACING // 2 - image.get_height() // 2)) 
