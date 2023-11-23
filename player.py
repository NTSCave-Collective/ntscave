import pygame
import tiles
import os
from math import floor
import CONSTANTS

global player_cache
player_cache = {}

def get_image(key):
    if not key in player_cache:
        # print(f"loading {key}")
        player_cache[key] = pygame.image.load(os.path.join(key)).convert_alpha()
    return player_cache[key]

def drawPlayer(window, state):
    # 48px x 24px

    state.attacking = False
    
    animframe = floor((state.frame % 60) / 15)

    if state.attacking:
        if state.downFacing:
            pass
        elif state.rightFacing:
            pass
        elif state.leftFacing:
            pass
        elif state.upFacing:
            pass
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

    player = pygame.transform.scale(player, (CONSTANTS.PIXELS, CONSTANTS.PIXELS))
    window.blit(player, (state.x - CONSTANTS.PIXELS/2, state.y - CONSTANTS.PIXELS))

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

    def collisionEvents():
        tilePosX = floor(((state.x) / CONSTANTS.PIXELS) % len(CONSTANTS.MAP[0]))
        tilePosY = floor(((state.y) / CONSTANTS.PIXELS) % len(CONSTANTS.MAP))

        try:
            currentTile = CONSTANTS.MAP[tilePosY][tilePosX]
        except:
            return True
        
        playertileX = state.x % CONSTANTS.PIXELS // CONSTANTS.QUARTER
        playertileY = state.y % CONSTANTS.PIXELS // CONSTANTS.QUARTER

        if tiles.bounds[currentTile][playertileY][playertileX] and currentTile in tiles.event_for_bound_blocks:
            tiles.tileEvents(currentTile, state)

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
        
        # collisionEvents()

    def attack():
        if keys[pygame.K_SPACE]:
            state.attacking = True

    
    movement()
    attack()
