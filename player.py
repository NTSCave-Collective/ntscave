import pygame

global pos
pos = [100, 100]

def drawCircle(window):
    circleX = 100
    circleY = 100
    radius = 10
    red = (200,0,0)
    pygame.draw.circle(window, red, pos, radius)

def playerMovement(event):
    print(pygame.key.get_pressed)
    if event.key == pygame.K_LEFT:
        pos[0] -= 1
    if event.key == pygame.K_RIGHT:
        pos[0] += 1
    if event.key == pygame.K_UP:
        pos[1] -= 1
    if event.key == pygame.K_DOWN:
        pos[1] += 1