import pygame
import player

def render_frame(window):
    # Drawing current frame
    player.drawCircle(window)
    
    pygame.display.flip()
