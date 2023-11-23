import pygame
import os
import tiles
import CONSTANTS
from math import floor
import random
import math

class Enemy:
    def __init__(self, species, x, y):
        self.x = x
        self.y = y
        self.species = species
        
        self.leftFacing = False
        self.rightFacing = False
        self.upFacing = False
        self.downFacing = True  # Default facing down

    def draw(self, window, state):

        animframe = floor((state.frame % CONSTANTS.TICK) / (CONSTANTS.TICK/4))

        if self.downFacing:
            enemy = pygame.image.load(os.path.join(tiles.name_to_entity[self.species]["down"][animframe])).convert_alpha()
        elif self.rightFacing:
            enemy = pygame.image.load(os.path.join(tiles.playetiles.name_to_entity[self.species]["right"][animframe])).convert_alpha()
        elif self.leftFacing:
            enemy = pygame.image.load(os.path.join(tiles.name_to_entity[self.species]["left"][animframe])).convert_alpha()
        elif self.upFacing:
            enemy = pygame.image.load(os.path.join(tiles.name_to_entity[self.species]["left"][animframe])).convert_alpha()
        enemy = pygame.transform.scale(enemy, (CONSTANTS.PIXELS, CONSTANTS.PIXELS))
        window.blit(enemy, (self.x - 32, self.y - 64))

        #pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))

def spawn_enemies_on_floor(state, num_random_enemies):
    max_dist = 6*64
    enemies = []

    for _ in range(num_random_enemies):
        valid_tile = False
        attempts = 0
        while not valid_tile and attempts <= 5:
            rand_y = random.randint(state.y-max_dist, state.y+max_dist) // 64
            if rand_y < 0:
                continue
            rand_x = random.randint(state.x-max_dist, state.x+max_dist) // 64
            if rand_x < 0:
                continue
            attempts += 1
            try:
                if "floor" in str(CONSTANTS.MAP[rand_y][rand_x]):
                    x_pos = rand_x*CONSTANTS.PIXELS + CONSTANTS.PIXELS/2
                    y_pos = rand_y*CONSTANTS.PIXELS + CONSTANTS.PIXELS/2
                    species = random.choice(tiles.species_list)

                    # Calculate distance between potential enemy spawn point and player
                    distance = math.sqrt((x_pos - state.x)**2 + (y_pos - state.y)**2)
                    # Only allow spawning if the distance is greater than 2 tiles
                    if distance >= 2.5 * CONSTANTS.PIXELS:
                        valid_enemy = Enemy(species, x_pos, y_pos)
                        enemies.append(valid_enemy)
                        valid_tile = True
            except IndexError:
                pass

    return enemies

def draw_enemies(game_objects, state):
    for enemy in state.enemies:
        enemy.draw(game_objects, state)

def draw_grid_with_enemies(game_objects, screen_size, grid_color, grid_spacing, enemies, state):
    width, height = screen_size

    for y in range(len(CONSTANTS.MAP)):
        for x in range(len(CONSTANTS.MAP[y])):
            try:
                image = pygame.image.load(os.path.join(tiles.tiles[CONSTANTS.MAP[y][x]]))
                image = pygame.transform.scale(image, (CONSTANTS.PIXELS, CONSTANTS.PIXELS))
                game_objects.blit(image, (CONSTANTS.PIXELS * x, CONSTANTS.PIXELS * y))
            except:
                pass

    draw_enemies(game_objects, enemies, state)

def generate_enemies(state):
    num_random_enemies = random.randint(1, 5)
    enemies = spawn_enemies_on_floor(state, num_random_enemies)

    state.enemies = enemies
