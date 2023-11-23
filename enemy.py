import pygame
import os
import tiles
import CONSTANTS
from math import floor
import random
import math

global enemy_cache
enemy_cache = {}
pi = math.pi

def get_image(key):
    if not key in enemy_cache:
        # print(f"loading {key}")
        enemy_cache[key] = pygame.image.load(key).convert_alpha()
    return enemy_cache[key]

class Enemy:
    def __init__(self, species, x, y):
        self.x = x
        self.y = y
        self.species = species
        self.vel = {"worm": 2}[self.species]

        self.away = False
        self.awayframe = 0
        self.awayangle = 0
        
        # Define hitbox dimensions
        self.hitbox_width = CONSTANTS.PIXELS
        self.hitbox_height = CONSTANTS.PIXELS

        # Adjust hitbox position relative to enemy position
        self.hitbox_x = self.x - self.hitbox_width / 2
        self.hitbox_y = self.y - self.hitbox_height / 2

        self.leftFacing = False
        self.rightFacing = False
        self.upFacing = False
        self.downFacing = True  # Default facing down

        # Initialize hitbox position based on enemy position
        self.update_hitbox_position()

    def update_hitbox_position(self):
        # Update hitbox position based on enemy position
        self.hitbox_x = self.x - self.hitbox_width / 2
        self.hitbox_y = self.y - self.hitbox_height / 2

    def draw(self, window, state):

        animframe = floor((state.frame % CONSTANTS.TICK) / (CONSTANTS.TICK/4))

        if self.downFacing:
            enemy = pygame.image.load(os.path.join(tiles.name_to_entity[self.species]["down"][animframe])).convert_alpha()
        elif self.rightFacing:
            enemy = pygame.image.load(os.path.join(tiles.name_to_entity[self.species]["right"][animframe])).convert_alpha()
        elif self.leftFacing:
            enemy = pygame.image.load(os.path.join(tiles.name_to_entity[self.species]["left"][animframe])).convert_alpha()
        elif self.upFacing:
            enemy = pygame.image.load(os.path.join(tiles.name_to_entity[self.species]["left"][animframe])).convert_alpha()
        window.blit(enemy, (self.x - CONSTANTS.PIXELS/2, self.y - CONSTANTS.PIXELS/2))
        # Draw hitbox (for debugging purposes)
        pygame.draw.rect(window, (255, 0, 0), (self.hitbox_x, self.hitbox_y, self.hitbox_width, self.hitbox_height), 2)
        self.update_hitbox_position()

    def move(self, state):
        try:
            dx, dy = (state.x-self.x), (state.y - self.y)
            dist = math.hypot(dx, dy)
            angle = math.atan2(dy,dx)

            if dist > 0.3:
                if self.away:
                    self.x += self.vel * round(math.cos(self.awayangle))
                    self.y += self.vel * round(math.sin(self.awayangle))
                    if self.awayframe + CONSTANTS.TICK == state.frame:
                        self.away = False
                elif random.randint(0,CONSTANTS.TICK*4) == 0:
                    self.awayangle = (random.random()-0.5)*pi
                    self.x += self.vel * round(math.cos(self.awayangle))
                    self.y += self.vel * round(math.sin(self.awayangle))
                    self.away = True
                    self.awayframe = state.frame
                else:
                    self.x += self.vel * round(math.cos(angle))
                    self.y += self.vel * round(math.sin(angle))
            
        except ZeroDivisionError:
            pass

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
                    distance = math.hypot((x_pos - state.x), (y_pos - state.y))
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
    num_random_enemies = random.randint(1, state.level+1)
    enemies = spawn_enemies_on_floor(state, num_random_enemies)

    state.enemies = enemies



def is_collision(player_x, player_y, enemy_hitbox_x, enemy_hitbox_y, enemy_hitbox_width, enemy_hitbox_height):
    # Check for collision considering hitbox
    return (
        player_x + CONSTANTS.PIXELS/2 + CONSTANTS.ATTACK_DISTANCE > enemy_hitbox_x and
        player_x - CONSTANTS.PIXELS/2 - CONSTANTS.ATTACK_DISTANCE < enemy_hitbox_x + enemy_hitbox_width and
        player_y + CONSTANTS.PIXELS/2 + CONSTANTS.ATTACK_DISTANCE > enemy_hitbox_y and
        player_y - CONSTANTS.PIXELS/2 - CONSTANTS.ATTACK_DISTANCE < enemy_hitbox_y + enemy_hitbox_height
    )
