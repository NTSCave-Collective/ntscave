import pygame
import player
import grid
import camera

def render_frame(window, gameObjects, state):
    pygame.draw.circle(gameObjects, (0,0,0), [300, 300], 50)

    grid.draw_grid(gameObjects, (1024, 768), (0,0,0), 20)

    player.drawCircle(gameObjects, state)

    # Move all gameObjects based on the player position 
    camera.camera(window, gameObjects, state)
    
    pygame.display.update()



def clear_surface(window):
    window.fill([255,255,255])