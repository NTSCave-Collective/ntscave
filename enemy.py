import pygame
import os
import tiles
import CONSTANTS
from math import floor
import random
import math

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20  # Adjust the size as needed
        self.color = (255, 0, 0)  # Red color for the enemy

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))

def spawn_enemies_on_floor(player_position, num_random_enemies):
    enemies = []
    map_data = CONSTANTS.MAP

    for _ in range(num_random_enemies):
        valid_tile = False

        while not valid_tile:
            rand_y = random.randint(0, len(map_data) - 1)
            rand_x = random.randint(0, len(map_data[0]) - 1)

            try:
                if "floor" in map_data[rand_y][rand_x]:
                    x_pos = rand_x * CONSTANTS.PIXELS + 32
                    y_pos = rand_y * CONSTANTS.PIXELS + 32

                    # Calculate distance between potential enemy spawn point and player
                    distance = math.sqrt((x_pos - player_position[0])**2 + (y_pos - player_position[1])**2)

                    # Only allow spawning if the distance is greater than 2 tiles
                    if distance > 2 * CONSTANTS.PIXELS:
                        valid_enemy = Enemy(x_pos, y_pos)
                        enemies.append(valid_enemy)
                        valid_tile = True
            except IndexError:
                pass

    print(enemies)
    return enemies
def draw_enemies(game_objects, enemies):
    for enemy in enemies:
        enemy.draw(game_objects)

def draw_grid_with_enemies(game_objects, screen_size, grid_color, grid_spacing, enemies):
    width, height = screen_size
    global grid_map
    grid_map = CONSTANTS.MAP

    for y in range(len(grid_map)):
        for x in range(len(grid_map[y])):
            try:
                image = pygame.image.load(os.path.join(tiles.tiles[grid_map[y][x]]))
                image = pygame.transform.scale(image, (CONSTANTS.PIXELS, CONSTANTS.PIXELS))
                game_objects.blit(image, (CONSTANTS.PIXELS * x, CONSTANTS.PIXELS * y))
            except:
                pass

    draw_enemies(game_objects, enemies)


