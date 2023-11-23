import pygame
import os
import tiles
import CONSTANTS
from math import floor, ceil
import player
import CONSTANTS
import enemy
import animation
import hud
import os
import effects

global image_cache
image_cache = {}

def get_image(key):
    if not key in image_cache:
        image_cache[key] = pygame.image.load(os.path.join(key)).convert_alpha()
        # image_cache[key] = pygame.image.load(os.path.join(tiles.tiles[key]))
    return image_cache[key]

def render_frame(window, gameObjects, state):
    animation.tileAnimations(state)
    draw_grid(gameObjects, state)

    # Draw enemies on the board
    if state.newLevel == False:
        [enemy.move(state) for enemy in state.enemies]
    draw_enemies(gameObjects, state)

    if state.newLevel == False:
        if state.attacking:
            player.attack(gameObjects, state)
        player.drawPlayer(gameObjects, state)
    else:
        player.newLevel(gameObjects, state)
    
    effects.effectEvent(state)
    draw_effects(gameObjects, state)

    # Move all gameObjects based on the player position 
    camera(window, gameObjects, state)

    hud.draw_hud(window, state)
    
    pygame.display.update()

def clear_surface(window):
    window.fill(CONSTANTS.BACKGROUND_COLOR)

def draw_grid(gameObjects, state):
    """
    leftBound = max(0, floor(((state.x - CONSTANTS.SCREEN_SIZE[0])/2 / CONSTANTS.PIXELS)))
    rightBound = min(len(CONSTANTS.MAP[0]), floor(((state.x)/2 - CONSTANTS.SCREEN_SIZE[0] / CONSTANTS.PIXELS)))

    topBound = max(0, floor(((state.y - CONSTANTS.SCREEN_SIZE[1])/2 / CONSTANTS.PIXELS)))
    bottomBound = min(len(CONSTANTS.MAP), floor(((state.y) - CONSTANTS.SCREEN_SIZE[1]/2 / CONSTANTS.PIXELS)))
    """
    leftBound = max(0, floor(state.x/CONSTANTS.PIXELS) - CONSTANTS.BOUND)
    topBound = max(0, floor(state.y/CONSTANTS.PIXELS) - CONSTANTS.BOUND)
    bottomBound = min(len(CONSTANTS.MAP), floor(state.y/CONSTANTS.PIXELS) + CONSTANTS.BOUND)
    rightBound = min(max([len(y) for y in CONSTANTS.MAP]), floor(state.x/CONSTANTS.PIXELS) + CONSTANTS.BOUND)

    for y in range(topBound, bottomBound):
        for x in range(leftBound, rightBound):
            try:
                image = get_image(tiles.tiles[CONSTANTS.MAP[y][x]])
                gameObjects.blit(image, (CONSTANTS.PIXELS * x , CONSTANTS.PIXELS * y))
            except:
                pass


def camera(window, gameObjects, state):
    # Move every gameObject on the screen relative to the player position
    window.blit(gameObjects, (CONSTANTS.SCREEN_WIDTH/2 - state.x, CONSTANTS.SCREEN_HEIGHT/2 - state.y))
    # Remove previous gameObjects
    clear_surface(gameObjects)


def toggle_fullscreen():
    pygame.display.toggle_fullscreen()

def draw_enemies(game_objects, state):
    for enemy in state.enemies:
        enemy.draw(game_objects, state)

def draw_effects(game_objects, state):
    for e in state.effects:
        e.draw(game_objects, state)