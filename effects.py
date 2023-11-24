import pygame
import os
import CONSTANTS
import random
import math

global effect_cache
effect_cache = {}

def get_image(key):
    if not key in effect_cache:
        # print(f"loading {key}")
        effect_cache[key] = pygame.image.load(os.path.join(key)).convert_alpha()
    return effect_cache[key]

effect_list = ["health", "speed", "crit", "attack", "distance"]
effect_weights = (6, 3, 2, 1, 1)

effects = {
    "health": "assets/effect/heart.png",
    "healthboost": "assets/effect/heart2.png",
    "speed": "assets/effect/speed.png",
    "speedboost": "assets/effect/speed_perm.png",
    "crit": "assets/effect/crit.png",
    "critboost": "assets/effect/crit_perm.png",
    "attack": "assets/effect/attack.png",
    "attackboost": "assets/effect/attack_perm.png",
    "distance": "assets/effect/distance.png",
    "distanceboost": "assets/effect/distance_perm.png"
}

def health(state, e):
    state.hearts += 1

def healthboost(state, e):
    state.hearts += 2

def speed(state, e):
    state.vel += 0.1

def speedboost(state, e):
    if not e.used:
        state.vel += 1
    if state.frame == e.end_frame:
        state.vel -= 1

def crit(state, e):
    state.crit += state.crit/CONSTANTS.CRITSCALE

def critboost(state, e):
    if not e.used:
        state.crit += state.crit/(CONSTANTS.CRITSCALE/2)
    if state.frame == e.end_frame:
        state.crit -= state.crit/(CONSTANTS.CRITSCALE/2)

def attack(state, e):
    state.attack += 0.1

def attackboost(state, e):
    if not e.used:
        state.attack += 1
    if state.frame == e.end_frame:
        state.attack -= 1

def distance(state, e):
    CONSTANTS.ATTACKDISTANCE += CONSTANTS.PIXELS/8

def distanceboost(state, e):
    if not e.used:
        CONSTANTS.ATTACKDISTANCE += CONSTANTS.PIXELS
    if state.frame == e.end_frame:
        CONSTANTS.ATTACKDISTANCE -= CONSTANTS.PIXELS

framelength = {
    "health": 1,
    "healthboost": 1,
    "speed": 1,
    "speedboost": CONSTANTS.TICK*CONSTANTS.BOOSTLENGTH(),
    "crit": 1,
    "critboost": CONSTANTS.TICK*CONSTANTS.BOOSTLENGTH(),
    "attack": 1,
    "attackboost": CONSTANTS.TICK*CONSTANTS.BOOSTLENGTH(),
    "distance": 1,
    "distanceboost": CONSTANTS.TICK*CONSTANTS.BOOSTLENGTH(),
}

def effectEvent(state):
    for e in state.activeEffects:   
        if e.used:
            continue
        if e.effect == "health":
            health(state, e)
        elif e.effect == "healthboost":
            healthboost(state, e)
        elif e.effect == "speed":
            speed(state, e)
        elif e.effect == "speedboost":
            speedboost(state, e)
        elif e.effect == "crit":
            crit(state, e)
        elif e.effect == "critboost":
            critboost(state, e)
        elif e.effect == "attack":
            attack(state, e)
        elif e.effect == "attackboost":
            attackboost(state, e)
        elif e.effect == "distance":
            distance(state, e)
        elif e.effect == "distanceboost":
            distanceboost(state, e)
        e.used = True
    state.activeEffects = list(filter(lambda e: state.frame == e.end_frame, state.activeEffects))

class Effect():
    def __init__(self, x, y, frame, effect):
        self.x = x
        self.y = y
        self.hitbox_width = CONSTANTS.PIXELS/2
        self.hitbox_height = CONSTANTS.PIXELS/2
        self.hitbox_x = self.x - self.hitbox_width / 2
        self.hitbox_y = self.y - self.hitbox_height / 2
        self.used = False
        self.effect = effect
    
    def draw(self, window, state):
        if math.hypot(state.x-self.x, state.y-self.y) > (CONSTANTS.BOUND+1)*64:
            return
            
        animframe = math.floor((state.frame % CONSTANTS.TICK) / (CONSTANTS.TICK/4))

        effect = get_image(effects[self.effect]).convert_alpha()
        window.blit(effect, (self.x - CONSTANTS.PIXELS/2, self.y - CONSTANTS.PIXELS/2))
        # Draw hitbox (for debugging purposes)
        if CONSTANTS.DEBUG:
            pygame.draw.rect(window, (255, 0, 0), (self.hitbox_x, self.hitbox_y, self.hitbox_width, self.hitbox_height), 2)

def drop_effect(x,y, state):
    if random.randint(0,4) == 0 or True:
        e = random.choices(effect_list, weights=effect_weights, k=1)[0]
        e = random.choices([e, e+"boost"], weights=(1,10), k=1)[0]
        effect = Effect(x,y, state.frame, e)
        state.effects.append(effect)