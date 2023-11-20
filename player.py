import pygame

def drawCircle(window):
    circleX = 100
    circleY = 100
    radius = 10
    red = (200,0,0)
    pygame.draw.circle(window, red, (circleX, circleY), radius) # Here <<<
