import pygame
import player
import grid
import camera
import CONSTANTS

def render_frame(window, gameObjects, state):
    grid.draw_grid(gameObjects, CONSTANTS.SCREEN_SIZE, CONSTANTS.BACKGROUND_COLOR, CONSTANTS.RADIUS_BALL)
    player.drawPlayer(gameObjects, state)

    # Move all gameObjects based on the player position 
    camera.camera(window, gameObjects, state)
    
    pygame.display.update()



def clear_surface(window):
    window.fill(CONSTANTS.BACKGROUND_COLOR)