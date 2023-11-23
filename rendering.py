import pygame
import os
import tiles
import CONSTANTS
from math import floor, ceil
import player
import CONSTANTS
import enemy
import animation
global image_cache
image_cache = {}

def render_frame(window, gameObjects, state):
    animation.tileAnimations(state)
    draw_grid(gameObjects, state)

    # Draw enemies on the board
    draw_enemies(gameObjects, state)

    if state.newLevel == False:
        if state.attacking:
            player.attack(gameObjects, state)
        player.drawPlayer(gameObjects, state)
    else:
        player.newLevel(gameObjects, state)

    # Move all gameObjects based on the player position 
    camera(window, gameObjects, state)
    
    pygame.display.update()

def clear_surface(window):
    window.fill(CONSTANTS.BACKGROUND_COLOR)

def get_image(key):
    if not key in image_cache:
        image_cache[key] = pygame.image.load(tiles.tiles[key])
        # image_cache[key] = pygame.image.load(os.path.join(tiles.tiles[key]))
    return image_cache[key]

def draw_grid(gameObjects, state):
    """
    leftBound = max(0, floor(((state.x - CONSTANTS.SCREEN_SIZE[0])/2 / CONSTANTS.PIXELS)))
    rightBound = min(len(CONSTANTS.MAP[0]), floor(((state.x)/2 - CONSTANTS.SCREEN_SIZE[0] / CONSTANTS.PIXELS)))

    topBound = max(0, floor(((state.y - CONSTANTS.SCREEN_SIZE[1])/2 / CONSTANTS.PIXELS)))
    bottomBound = min(len(CONSTANTS.MAP), floor(((state.y) - CONSTANTS.SCREEN_SIZE[1]/2 / CONSTANTS.PIXELS)))
    """



    for y in range(len(CONSTANTS.MAP)):
        for x in range(len(CONSTANTS.MAP[y])):
            actualX = CONSTANTS.PIXELS * x
            actualY = CONSTANTS.PIXELS * y

            if ((state.x - CONSTANTS.BOUND) < actualX < (state.x + CONSTANTS.BOUND)) and ((state.y - CONSTANTS.BOUND) < actualY < (state.y + CONSTANTS.BOUND)):
                image = get_image(CONSTANTS.MAP[y][x])
                gameObjects.blit(image, (CONSTANTS.PIXELS * x , CONSTANTS.PIXELS * y))


def camera(window, gameObjects, state):
    # Move every gameObject on the screen relative to the player position
    window.blit(gameObjects, (CONSTANTS.SCREEN_WIDTH/2 - state.x, CONSTANTS.SCREEN_HEIGHT/2 - state.y))
    # Remove previous gameObjects
    clear_surface(gameObjects)


def toggle_fullscreen(window):
    pygame.display.toggle_fullscreen()
    return pygame.display.get_surface()

def draw_enemies(game_objects, state):
    for enemy in state.enemies:
        enemy.draw(game_objects, state)