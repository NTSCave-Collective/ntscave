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
    textsize = round(CONSTANTS.PIXELS/3)

    hudtext = [
        get_font(textsize).render(f"FPS: {state.fps:.2f}", True, CONSTANTS.TEXT_COLOR),
        get_font(textsize).render(f"LVL: {state.level}", True, CONSTANTS.TEXT_COLOR),
        
        get_font(textsize).render(f"RAN: {CONSTANTS.ATTACKDISTANCE/64:.1f}", True, CONSTANTS.TEXT_COLOR),
        get_font(textsize).render(f"CRI: {state.crit*100:.1f}%", True, CONSTANTS.TEXT_COLOR),
        get_font(textsize).render(f"ATT: {state.attack:.1f}", True, CONSTANTS.TEXT_COLOR),
        get_font(textsize).render(f"VEL: {state.vel:.1f}", True, CONSTANTS.TEXT_COLOR),

        get_font(textsize).render(f"X: {state.x//CONSTANTS.PIXELS}", True, CONSTANTS.TEXT_COLOR),
        get_font(textsize).render(f"Y: {state.y//CONSTANTS.PIXELS}", True, CONSTANTS.TEXT_COLOR),
    ]
    
    for i in range(0, len(hudtext)):
        window.blit(hudtext[i], (0, window.get_height()-textsize*(i+1)))

    if state.hearts < 10:
        for i in range(1, int(state.hearts*2+1)):
            if not (i % 2) :
                hud = get_image(tiles.hud["heart_full"])
                window.blit(hud, ((i/2-1)*CONSTANTS.PIXELS, 0))
            elif i == int(state.hearts*2):
                hud = get_image(tiles.hud["heart_half"])
                window.blit(hud, ((i/2-0.5)*CONSTANTS.PIXELS, 0))
    else:
        hud = get_image(tiles.hud["heart_full"])
        window.blit(hud, (0, 0))
        hearttext = get_font(CONSTANTS.PIXELS).render(f"x {state.hearts}", True, CONSTANTS.TEXT_COLOR)
        window.blit(hearttext, (CONSTANTS.PIXELS, 0))


    for e in range(0, len(state.activeEffects)):
            hud = get_image(effects.effects[state.activeEffects[e].effect])
            window.blit(hud, ( window.get_width() - CONSTANTS.PIXELS , CONSTANTS.PIXELS*e))
