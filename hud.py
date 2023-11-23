import pygame
import os
import tiles
import CONSTANTS
from math import floor

global hud_cache
hud_cache = {}

def get_image(key):
    if not key in hud_cache:
        hud_cache[key] = pygame.image.load(os.path.join(key)).convert_alpha()
    return hud_cache[key]

def draw_hud(window, state):
    for i in range(1, int(state.hearts*2+1)):
        if not (i % 2) :
            hud = get_image(tiles.hud["heart_full"])
            window.blit(hud, ((i/2-1)*CONSTANTS.PIXELS, 0))
        elif i == int(state.hearts*2):
            hud = get_image(tiles.hud["heart_half"])
            window.blit(hud, ((i/2-0.5)*CONSTANTS.PIXELS, 0))
