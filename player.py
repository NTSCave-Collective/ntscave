import pygame
import tiles
import os
from math import floor
import CONSTANTS
import ROOMS
from enemy import is_collision


global player_cache
player_cache = {}

def get_image(key):
    if not key in player_cache:
        # print(f"loading {key}")
        player_cache[key] = pygame.image.load(os.path.join(key)).convert_alpha()
    return player_cache[key]

def drawPlayer(window, state):
    animframe = floor((state.frame % CONSTANTS.TICK) / (CONSTANTS.TICK/4))

    if state.moving:
        if state.downFacing:
            player = get_image(tiles.player["down_moving"][animframe])
        elif state.rightFacing:
            player = get_image(tiles.player["right_moving"][animframe])
        elif state.leftFacing:
            player = get_image(tiles.player["left_moving"][animframe])
        elif state.upFacing:
            player = get_image(tiles.player["up_moving"][animframe])
    else:
        if state.downFacing:
            player = get_image(tiles.player["down"][animframe])
        elif state.rightFacing:
            player = get_image(tiles.player["right"][animframe])
        elif state.leftFacing:
            player = get_image(tiles.player["left"][animframe])
        elif state.upFacing:
            player = get_image(tiles.player["up"][animframe])

    window.blit(player, (state.x - CONSTANTS.PIXELS/2, state.y - CONSTANTS.PIXELS))

def newLevel(window, state):
    if state.frame < state.newLevel_frame + CONSTANTS.TICK*2:
        animframe = floor((state.frame % CONSTANTS.TICK) / (CONSTANTS.TICK/4))
    elif state.frame < state.newLevel_frame + CONSTANTS.TICK*4:
        animframe = floor(((state.frame*2) % (CONSTANTS.TICK)) / (CONSTANTS.TICK/4))
    elif state.frame < state.newLevel_frame + CONSTANTS.TICK*6:
        animframe = floor(((state.frame*4) % (CONSTANTS.TICK)) / (CONSTANTS.TICK/4))
    else:
        animframe = 3
        
    player = get_image(tiles.player["spin"][animframe])

    window.blit(player, (state.x - CONSTANTS.PIXELS/2, state.y - CONSTANTS.PIXELS))
    
    if state.frame == state.newLevel_frame + CONSTANTS.TICK*6:
        state.newLevel = False
        state.newLevel_frame = None
        ROOMS.swap_map(state, "random")

def attack(window, state):
    state.attackframe += 1

    x_move = 0
    y_move = 0
    animframe = floor((state.attackframe % CONSTANTS.TICK) / (CONSTANTS.TICK/4))
    if state.downFacing:
        slash = get_image(tiles.slash["down"][animframe])
        y_move += CONSTANTS.PIXELS/2
    elif state.rightFacing:
        slash = get_image(tiles.slash["right"][animframe])
        x_move += CONSTANTS.PIXELS/2
    elif state.leftFacing:
        slash = get_image(tiles.slash["left"][animframe])
        x_move -= CONSTANTS.PIXELS/2
    elif state.upFacing:
        slash = get_image(tiles.slash["up"][animframe])
        y_move -= CONSTANTS.PIXELS/2
    
    if state.attackframe < CONSTANTS.ATTACK_DURATION:
        handle_player_attack(state)

        
    window.blit(slash, (state.x - CONSTANTS.PIXELS/2 + x_move, state.y - CONSTANTS.PIXELS + y_move))

    if state.attackframe == CONSTANTS.TICK -1:
        state.attacking = False
        state.attackframe = None

def handle_player_attack(state):
    if state.attacking:
        for enemy in state.enemies:
            if is_collision(state.x, state.y, enemy.x, enemy.y, state):
                state.enemies.remove(enemy)

def playerEvents(state):
    keys = pygame.key.get_pressed()

    def collision(heading):
        tilePosY = floor(((state.y) / CONSTANTS.PIXELS) % len(CONSTANTS.MAP))
        tilePosX = floor(((state.x) / CONSTANTS.PIXELS) % len(CONSTANTS.MAP[tilePosY]))

        try:
            currentTile = CONSTANTS.MAP[tilePosY][tilePosX]
        except:
            return True
        
        playertileX = floor((state.x % CONSTANTS.PIXELS) // (CONSTANTS.PIXELS/4))
        playertileY = floor((state.y % CONSTANTS.PIXELS) // (CONSTANTS.PIXELS/4))

        return not (tiles.bounds[currentTile][playertileY][playertileX] and not currentTile in tiles.event_for_bound_blocks)

    def collisionEvents(state):
        tilePosX = floor(((state.x) / CONSTANTS.PIXELS) % len(CONSTANTS.MAP[0]))
        tilePosY = floor(((state.y) / CONSTANTS.PIXELS) % len(CONSTANTS.MAP))

        try:
            currentTile = CONSTANTS.MAP[tilePosY][tilePosX]
        except:
            return True
        
        playertileX = floor((state.x % CONSTANTS.PIXELS) // (CONSTANTS.PIXELS/4))
        playertileY = floor((state.y % CONSTANTS.PIXELS) // (CONSTANTS.PIXELS/4))

        if tiles.bounds[currentTile][playertileY][playertileX] and currentTile in tiles.event_for_bound_blocks:
            tiles.tileEvents(tilePosX, tilePosY, currentTile, state)

    def movement():
        state.moving = False

        if keys[pygame.K_LEFT]:
            state.moving = True
            state.x -= state.vel
            if not collision("left"):
                state.x += state.vel
            state.rightFacing = False
            state.leftFacing = True
            if not keys[pygame.K_UP]:
                state.upFacing = False
            if not keys[pygame.K_DOWN]:
                state.downFacing = False

        if keys[pygame.K_RIGHT]:
            state.moving = True
            state.x += state.vel
            if not collision("right"):
                state.x -= state.vel
            state.rightFacing = True
            state.leftFacing = False
            if not keys[pygame.K_UP]:
                state.upFacing = False
            if not keys[pygame.K_DOWN]:
                state.downFacing = False

        if keys[pygame.K_UP]:
            state.moving = True
            state.y -= state.vel
            if not collision("up"):
                state.y += state.vel
            state.upFacing = True
            state.downFacing = False
            if not keys[pygame.K_LEFT]:
                state.leftFacing = False
            if not keys[pygame.K_RIGHT]:
                state.rightFacing = False

        if keys[pygame.K_DOWN]:
            state.moving = True
            state.y += state.vel
            if not collision("down"):
                state.y -= state.vel
            state.upFacing = False
            state.downFacing = True
            if not keys[pygame.K_LEFT]:
                state.leftFacing = False
            if not keys[pygame.K_RIGHT]:
                state.rightFacing = False

        if keys[pygame.K_SPACE]:
            state.attacking = True
            if state.attackframe == None:
                state.attackframe = 0
        
        collisionEvents(state)

    
    movement()
    
