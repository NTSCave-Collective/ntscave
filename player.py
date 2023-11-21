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
        tilePosX = floor(((state.x + tiles.colission_offsets[heading]) / CONSTANTS.PIXELS) % len(CONSTANTS.BACKGROUND_IMAGES[0]))
        tilePosY = floor(((state.y + tiles.colission_offsets[heading]) / CONSTANTS.PIXELS) % len(CONSTANTS.BACKGROUND_IMAGES))
        try:
            currentTile = CONSTANTS.BACKGROUND_IMAGES[tilePosY][tilePosX]
        except:
            return True

        print(currentTile)

        if currentTile in tiles.collision[heading]:
            return False

        return True

    def movement():
        state.moving = False
        if keys[pygame.K_LEFT]:
            state.moving = True
            if collision("left"):
                state.x -= state.vel
            state.rightFacing = False
            state.leftFacing = True
            if not keys[pygame.K_UP]:
                state.upFacing = False
            if not keys[pygame.K_DOWN]:
                state.downFacing = False

        if keys[pygame.K_RIGHT]:
            state.moving = True
            if collision("right"):
                state.x += state.vel
            state.rightFacing = True
            state.leftFacing = False
            if not keys[pygame.K_UP]:
                state.upFacing = False
            if not keys[pygame.K_DOWN]:
                state.downFacing = False

        if keys[pygame.K_UP]:
            state.moving = True
            if collision("up"):
                state.y -= state.vel
            state.upFacing = True
            state.downFacing = False
            if not keys[pygame.K_LEFT]:
                state.leftFacing = False
            if not keys[pygame.K_RIGHT]:
                state.rightFacing = False

        if keys[pygame.K_DOWN]:
            state.moving = True
            if collision("down"):
                state.y += state.vel
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
