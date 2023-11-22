import pygame
import os
import tiles
import CONSTANTS
from math import floor, ceil
import player
import CONSTANTS
import enemy

def render_frame(window, gameObjects, state):
    draw_grid(gameObjects, CONSTANTS.SCREEN_SIZE, state)

    player.drawPlayer(gameObjects, state)

    # Draw enemies on the board
    draw_enemies(gameObjects, state)

    # Move all gameObjects based on the player position 
    camera(window, gameObjects, state)
    
    pygame.display.update()

def clear_surface(window):
    window.fill(CONSTANTS.BACKGROUND_COLOR)

def draw_grid(gameObjects, screen_size, state):
    width, height = screen_size

    leftBound = max(0, floor(((state.x - CONSTANTS.SCREEN_SIZE[0]) / CONSTANTS.PIXELS)))
    rightBound = min(len(CONSTANTS.MAP[0]), floor(((state.x) - CONSTANTS.SCREEN_SIZE[0] / CONSTANTS.PIXELS)))

    topBound = max(0, floor(((state.y - CONSTANTS.SCREEN_SIZE[1]) / CONSTANTS.PIXELS)))
    bottomBound = min(len(CONSTANTS.MAP), floor(((state.y) - CONSTANTS.SCREEN_SIZE[1] / CONSTANTS.PIXELS)))

    for y in range(topBound, bottomBound):
        for x in range(leftBound, rightBound):
            try:
                image = pygame.image.load(os.path.join(tiles.tiles[CONSTANTS.MAP[y][x]]))
                image = pygame.transform.scale(image, (CONSTANTS.PIXELS, CONSTANTS.PIXELS))
                gameObjects.blit(image, (CONSTANTS.PIXELS * x , CONSTANTS.PIXELS * y))
            except:
                pass

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
        enemy.draw(game_objects, state.frame)

def draw_grid_with_enemies(game_objects, screen_size, grid_color, grid_spacing, enemies, state):
    width, height = screen_size

    for y in range(len(grid_map)):
        for x in range(len(grid_map[y])):
            try:
                image = pygame.image.load(os.path.join(tiles.tiles[grid_map[y][x]]))
                image = pygame.transform.scale(image, (CONSTANTS.PIXELS, CONSTANTS.PIXELS))
                game_objects.blit(image, (CONSTANTS.PIXELS * x, CONSTANTS.PIXELS * y))
            except:
                pass

    draw_enemies(game_objects, enemies, state)