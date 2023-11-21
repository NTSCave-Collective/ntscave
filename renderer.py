import pygame
import player
import grid

def render_frame(window, state):
    pygame.draw.circle(window, (0,0,0), [300, 300], 50)

    grid.draw_grid(window, (1024, 768), (0,0,0), 20)

    player.drawCircle(window, state)
    
    pygame.display.update()



def clear_surface(window):
    window.fill([255,255,255])