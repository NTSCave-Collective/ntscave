import pygame

def drawCircle(window, state):
    radius = 10
    red = (200,0,0)
    pygame.draw.circle(window, red, [state.x, state.y], radius)

def playerMovement(state):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        state.x -= state.vel
    if keys[pygame.K_RIGHT]:
        state.x += state.vel
    if keys[pygame.K_UP]:
        state.y -= state.vel
    if keys[pygame.K_DOWN]:
        state.y += state.vel
