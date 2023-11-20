import pygame
import player

def render_frame(window, State):
    # Drawing current frame
    player.drawCircle(window, State)
    pygame.display.flip()

def clear_surface(window):
    window.fill([255,255,255])