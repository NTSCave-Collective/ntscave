import pygame
import os
import tiles
import CONSTANTS
from math import floor
import effects

global hud_cache
hud_cache = {}

def get_image(key):
    if not key in hud_cache:
        hud_cache[key] = pygame.image.load(os.path.join(key)).convert_alpha()
    return hud_cache[key]

global font_cache
font_cache = {}
def get_font(size):
    if not size in font_cache:
        font_cache[size] = pygame.font.Font("assets/intro/font.ttf", size)
    return font_cache[size]

def draw_hud(window, state):
    FPS = get_font(round(CONSTANTS.PIXELS/2)).render(f"FPS: {state.clock.get_fps():.2f}", True, "#b68f40")
    window.blit(FPS, (0, window.get_height()-CONSTANTS.PIXELS/2))
    level = get_font(round(CONSTANTS.PIXELS/2)).render(f"LVL: {state.level}", True, "#b68f40")
    window.blit(level, (0, window.get_height()-(CONSTANTS.PIXELS/2)*2))
    
    for i in range(1, int(state.hearts*2+1)):
        if not (i % 2) :
            hud = get_image(tiles.hud["heart_full"])
            window.blit(hud, ((i/2-1)*CONSTANTS.PIXELS, 0))
        elif i == int(state.hearts*2):
            hud = get_image(tiles.hud["heart_half"])
            window.blit(hud, ((i/2-0.5)*CONSTANTS.PIXELS, 0))

    for e in range(0, len(state.activeEffects)):
            hud = get_image(effects.effects[state.activeEffects[e].effect])
            window.blit(hud, ( window.get_width() - CONSTANTS.PIXELS , CONSTANTS.PIXELS*e))
