import pygame

def toggle_fullscreen(window):
    pygame.display.toggle_fullscreen()
    return pygame.display.get_surface()