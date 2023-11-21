import pygame
import renderer
import CONSTANTS

def camera(window, gameObjects, state):
    # Move every gameObject on the screen relative to the player position
    window.blit(gameObjects, (CONSTANTS.SCREEN_WIDTH/2 - state.x, CONSTANTS.SCREEN_HEIGHT/2 - state.y))
    # Remove previous gameObjects
    renderer.clear_surface(gameObjects)


def toggle_fullscreen(window):
    pygame.display.toggle_fullscreen()
    return pygame.display.get_surface()