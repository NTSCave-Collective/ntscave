import pygame

def drawCircle(window, state):
    circleX = 100
    circleY = 100
    radius = 10
    red = (200,0,0)
    pygame.draw.circle(window, red, [state.x, state.y], radius)

def playerMovement(event, state):
    if event.key == pygame.K_LEFT:
        state.x -= 1
    if event.key == pygame.K_RIGHT:
        state.x += 1
    if event.key == pygame.K_UP:
        state.y -= 1
    if event.key == pygame.K_DOWN:
        state.y += 1
