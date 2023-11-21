import pygame
import tiles
import os

def drawCircle(window, state):
    radius = 10
    red = (200,0,0)
    pygame.draw.circle(window, red, [state.x, state.y], radius)
    state.attacking = False

    if state.downFacing:
        player = pygame.image.load(os.path.join(tiles.player["down"])).convert_alpha()
    elif state.rightFacing:
        player = pygame.image.load(os.path.join(tiles.player["right"])).convert_alpha()
    elif state.leftFacing:
        player = pygame.image.load(os.path.join(tiles.player["left"])).convert_alpha()
    elif state.upFacing:
        pygame.draw.circle(window, red, [state.x, state.y], radius)
        return

    window.blit(player, (state.x-24, state.y-24))

def playerEvents(state):
    keys = pygame.key.get_pressed()

    def movement():
        if keys[pygame.K_LEFT]:
            state.x -= state.vel
            state.rightFacing = False
            state.leftFacing = True
            if not keys[pygame.K_UP]:
                state.upFacing = False
            if not keys[pygame.K_DOWN]:
                state.downFacing = False

        if keys[pygame.K_RIGHT]:
            state.x += state.vel
            state.rightFacing = True
            state.leftFacing = False
            if not keys[pygame.K_UP]:
                state.upFacing = False
            if not keys[pygame.K_DOWN]:
                state.downFacing = False

        if keys[pygame.K_UP]:
            state.y -= state.vel
            state.upFacing = True
            state.downFacing = False
            if not keys[pygame.K_LEFT]:
                state.leftFacing = False
            if not keys[pygame.K_RIGHT]:
                state.rightFacing = False

        if keys[pygame.K_DOWN]:
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
