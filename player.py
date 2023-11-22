import pygame
import tiles
import os
import grid
from math import floor
import CONSTANTS

def drawPlayer(window, state):
    # 48px x 24px

    state.attacking = False
    
    animframe = floor((state.frame % 40) / 10)

    if state.attacking:
        if state.downFacing:
            player = pygame.image.load(os.path.join(tiles.player["down_attack"][animframe])).convert_alpha()
        elif state.rightFacing:
            player = pygame.image.load(os.path.join(tiles.player["right_attack"][animframe])).convert_alpha()
        elif state.leftFacing:
            player = pygame.image.load(os.path.join(tiles.player["left_attack"][animframe])).convert_alpha()
        elif state.upFacing:
            # player = pygame.image.load(os.path.join(tiles.player["up_attack"][animframe])).convert_alpha()
            return
    elif state.moving:
        if state.downFacing:
            player = pygame.image.load(os.path.join(tiles.player["down_moving"][animframe])).convert_alpha()
        elif state.rightFacing:
            player = pygame.image.load(os.path.join(tiles.player["right_moving"][animframe])).convert_alpha()
        elif state.leftFacing:
            player = pygame.image.load(os.path.join(tiles.player["left_moving"][animframe])).convert_alpha()
        elif state.upFacing:
            # player = pygame.image.load(os.path.join(tiles.player["up_moving"][animframe])).convert_alpha()
            return
    else:
        if state.downFacing:
            player = pygame.image.load(os.path.join(tiles.player["down"][animframe])).convert_alpha()
        elif state.rightFacing:
            player = pygame.image.load(os.path.join(tiles.player["right"][animframe])).convert_alpha()
        elif state.leftFacing:
            player = pygame.image.load(os.path.join(tiles.player["left"][animframe])).convert_alpha()
        elif state.upFacing:
            # player = pygame.image.load(os.path.join(tiles.player["up"][animframe])).convert_alpha()
            return

    window.blit(player, (state.x - 24, state.y - 48))

def playerEvents(state):
    keys = pygame.key.get_pressed()

    def collision(heading):
        tilePosX = floor(((state.x) / CONSTANTS.PIXELS) % len(CONSTANTS.MAP[0]))
        tilePosY = floor(((state.y) / CONSTANTS.PIXELS) % len(CONSTANTS.MAP))

        try:
            currentTile = CONSTANTS.MAP[tilePosY][tilePosX]
        except:
            return True
        
        playertileX = state.x % CONSTANTS.PIXELS // CONSTANTS.QUARTER
        playertileY = state.y % CONSTANTS.PIXELS // CONSTANTS.QUARTER

        return not (tiles.bounds[currentTile][playertileY][playertileX] and not currentTile in tiles.event_for_bound_blocks)

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

    def attack():
        if keys[pygame.K_SPACE]:
            state.attacking = True

    
    movement()
    attack()
