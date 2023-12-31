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
        enemy_cache[key] = pygame.image.load(os.path.join(key)).convert_alpha()
    return enemy_cache[key]

class Enemy:
    def __init__(self, species, x, y):
        self.x = x
        self.y = y
        self.species = species
        self.vel = {"worm": 2, "trojan": 3.6, "virus": 1}[self.species]
        self.damage = {"worm": 0.5, "trojan": 0.5, "virus": 1}[self.species]
        self.health = {"worm": 1, "trojan": 3, "virus": 2}[self.species]
        self.away = False
        self.awayframe = 0
        self.awayangle = 0

        self.hit = False
        self.hitframe = -CONSTANTS.TICK
        
        # Define hitbox dimensions
        self.hitbox_width = CONSTANTS.PIXELS*3/4
        self.hitbox_height = CONSTANTS.PIXELS*3/4

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
        if math.hypot(state.x-self.x, state.y-self.y) > (CONSTANTS.BOUND+1)*64:
            return
            
        animframe = floor((state.frame % CONSTANTS.TICK) / (CONSTANTS.TICK/4))

        if self.hit and (self.hitframe + CONSTANTS.TICK) < state.frame:
            self.hit = False
            animframe = floor((self.hitframe % CONSTANTS.TICK) / (CONSTANTS.TICK/4))

        if self.downFacing:
            enemy = get_image(tiles.name_to_entity[self.species]["down"][animframe]).convert_alpha()
        elif self.rightFacing:
            enemy = get_image(tiles.name_to_entity[self.species]["right"][animframe]).convert_alpha()
        elif self.leftFacing:
            enemy = get_image(tiles.name_to_entity[self.species]["left"][animframe]).convert_alpha()
        elif self.upFacing:
            enemy = get_image(tiles.name_to_entity[self.species]["left"][animframe]).convert_alpha()

        if self.hit:
            # zero out RGB values
            enemy.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
            # add in new RGB values
            enemy.fill((255, 0, 0)[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)


        window.blit(enemy, (self.x - CONSTANTS.PIXELS/2, self.y - CONSTANTS.PIXELS/2))
        # Draw hitbox (for debugging purposes)
        if CONSTANTS.DEBUG:
            pygame.draw.rect(window, (255, 0, 0), (self.hitbox_x, self.hitbox_y, self.hitbox_width, self.hitbox_height), 2)
        self.update_hitbox_position()

    def collision(self):
        tilePosY = floor(((self.y) / CONSTANTS.PIXELS) % len(CONSTANTS.MAP))
        tilePosX = floor(((self.x) / CONSTANTS.PIXELS) % len(CONSTANTS.MAP[tilePosY]))

        try:
            currentTile = CONSTANTS.MAP[tilePosY][tilePosX]
        except:
            return True
        
        playertileX = floor((self.x % CONSTANTS.PIXELS) // (CONSTANTS.PIXELS/4))
        playertileY = floor((self.y % CONSTANTS.PIXELS) // (CONSTANTS.PIXELS/4))

        return not (tiles.bounds[currentTile][playertileY][playertileX] and not currentTile in tiles.event_for_bound_blocks)

    def move(self, state):
        if math.hypot(state.x-self.x, state.y-self.y) > CONSTANTS.PIXELS*15:
            return
        try:
            dx, dy = (state.x-self.x), (state.y - self.y)
            angle = math.atan2(dy,dx)
            if math.hypot(dx, dy) > CONSTANTS.PIXELS/2 or self.hit:

                if self.hit:
                    mx = -round(self.vel * math.cos(self.hitangle))/2
                    my = -round(self.vel * math.sin(self.hitangle))/2
                elif self.away:
                    mx = round(self.vel * math.cos(self.awayangle))
                    my = round(self.vel * math.sin(self.awayangle))
                    if self.awayframe + CONSTANTS.TICK == state.frame:
                        self.away = False
                elif random.randint(0, CONSTANTS.TICK*10) == 0:
                    self.awayangle = (random.random()-0.5)*pi
                    mx = round(self.vel * math.cos(self.awayangle))
                    my = round(self.vel * math.sin(self.awayangle))
                    self.away = True
                    self.awayframe = state.frame
                else:
                    mx = round(self.vel * math.cos(angle))
                    my = round(self.vel * math.sin(angle))
                
                self.x += mx
                if not self.collision():
                    self.x -= mx

                self.y += my
                if not self.collision():
                    self.y -= my
                
            for enemy in state.enemies:
                if is_enemy_collision(
                        state.hitbox_x, state.hitbox_y, state.hitbox_width, state.hitbox_height,
                        enemy.hitbox_x, enemy.hitbox_y, enemy.hitbox_width, enemy.hitbox_height
                ):
                    # Deal damage to player
                    if state.last_hit + CONSTANTS.TICK < state.frame:
                        state.last_hit = state.frame + CONSTANTS.TICK
                        state.hearts -= enemy.damage
                        if CONSTANTS.DEBUG:
                            print(enemy.damage, state.hearts)

        except ZeroDivisionError:
            pass

def spawn_enemies_on_floor(state, num_random_enemies):
    enemies = []

    for _ in range(num_random_enemies):
        valid_tile = False
        attempts = 0
        while not valid_tile and attempts <= 10:
            rand_y = random.randint(0, len(CONSTANTS.MAP)-1)
            if rand_y < 0:
                continue
            rand_x = random.randint(0, len(CONSTANTS.MAP[rand_y])-1)
            if rand_x < 0:
                continue
            attempts += 1
            try:
                if str(CONSTANTS.MAP[rand_y][rand_x]) in ["floor", "floor2", "floor3", "spike"]:
                    x_pos = (rand_x + random.random())*CONSTANTS.PIXELS
                    y_pos = (rand_y + random.random())*CONSTANTS.PIXELS
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
    num_random_enemies = random.randint(2, round(state.level*1.1)+2)
    enemies = spawn_enemies_on_floor(state, num_random_enemies)

    state.enemies = enemies



def is_collision(player_x, player_y, enemy_hitbox_x, enemy_hitbox_y, enemy_hitbox_width, enemy_hitbox_height):
    # Check for collision considering hitbox
    return (
        player_x + CONSTANTS.ATTACKDISTANCE > enemy_hitbox_x and
        player_x - CONSTANTS.ATTACKDISTANCE < enemy_hitbox_x + enemy_hitbox_width and
        player_y + CONSTANTS.ATTACKDISTANCE > enemy_hitbox_y and
        player_y - CONSTANTS.ATTACKDISTANCE < enemy_hitbox_y + enemy_hitbox_height
    )

def is_enemy_collision(player_hitbox_x, player_hitbox_y, player_hitbox_width, player_hitbox_height, enemy_hitbox_x, enemy_hitbox_y, enemy_hitbox_width, enemy_hitbox_height):
    return (
        player_hitbox_x < enemy_hitbox_x + enemy_hitbox_width and
        player_hitbox_x + player_hitbox_width > enemy_hitbox_x and
        player_hitbox_y < enemy_hitbox_y + enemy_hitbox_height and
        player_hitbox_y + player_hitbox_height > enemy_hitbox_y
    )