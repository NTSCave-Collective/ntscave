import pygame
import tiles
import os
import grid
from math import floor
import CONSTANTS

def drawCircle(window, state):
    pygame.draw.circle(window, CONSTANTS.COLOR_BALL, [state.x, state.y], CONSTANTS.RADIUS_BALL)
    state.attacking = False

    if state.downFacing:
        player = pygame.image.load(os.path.join(tiles.player["down"])).convert_alpha()
    elif state.rightFacing:
        player = pygame.image.load(os.path.join(tiles.player["right"])).convert_alpha()
    elif state.leftFacing:
        player = pygame.image.load(os.path.join(tiles.player["left"])).convert_alpha()
    elif state.upFacing:
        pygame.draw.circle(window, CONSTANTS.COLOR_BALL, [state.x, state.y], CONSTANTS.RADIUS_BALL)
        return

    window.blit(player, (state.x-24, state.y-24))

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
        if keys[pygame.K_LEFT]:
            if collision("left"):
                state.x -= state.vel
            state.rightFacing = False
            state.leftFacing = True
            if not keys[pygame.K_UP]:
                state.upFacing = False
            if not keys[pygame.K_DOWN]:
                state.downFacing = False

        if keys[pygame.K_RIGHT]:
            if collision("right"):
                state.x += state.vel
            state.rightFacing = True
            state.leftFacing = False
            if not keys[pygame.K_UP]:
                state.upFacing = False
            if not keys[pygame.K_DOWN]:
                state.downFacing = False

        if keys[pygame.K_UP]:
            if collision("up"):
                state.y -= state.vel
            state.upFacing = True
            state.downFacing = False
            if not keys[pygame.K_LEFT]:
                state.leftFacing = False
            if not keys[pygame.K_RIGHT]:
                state.rightFacing = False

        if keys[pygame.K_DOWN]:
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
