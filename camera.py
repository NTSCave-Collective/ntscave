import pygame
import renderer

def camera(window, gameObjects, state):
    # Move every gameObject on the screen relative to the player position
    window.blit(gameObjects, (1024/2 - state.x,768/2 - state.y))
    # Remove previous gameObjects
    renderer.clear_surface(gameObjects)