import pygame
import os
import CONSTANTS
import random

global effect_cache
effect_cache = {}

def get_image(key):
    if not key in effect_cache:
        # print(f"loading {key}")
        effect_cache[key] = pygame.image.load(os.path.join(key)).convert_alpha()
    return effect_cache[key]

effect_list = ["health", "speed", "crit", "attack"]
effect_weights = (4,3,2,1)
effects = {
    "health": "assets/effect/heart.png",
    "health2": "assets/effect/heart2.png",
    "speed": "assets/effect/speed.png",
    "speedboost": "assets/effect/speedboost.png",
    "crit": "assets/effect/crit.png",
    "critboost": "assets/effect/critboost.png",
    "attack": "assets/effect/attack.png",
    "attackboost": "assets/effect/attackboost.png"
}

def health(state):
    state.hearts += 1

def health2(state):
    state.hearts += 2

def speed(state):
    state.vel += 0.1

def speedboost(state):
    pass

def crit(state):
    state.crit += state.crit/CONSTANTS.CRITSCALE

def critboost(state):
    pass

def attack(state):
    state.attack += 0.1

def attackboost(state):
    pass

effect_list = ["health", "speed", "crit", "attack"]

effects = {
    "health": "assets/effect/heart.png",
    "health2": "assets/effect/heart2.png",
    "speed": "assets/effect/speed.png",
    "speedboost": "assets/effect/speedboost.png",
    "crit": "assets/effect/crit.png",
    "critboost": "assets/effect/critboost.png",
    "attack": "assets/effect/attack.png",
    "attackboost": "assets/effect/attackboost.png",
    "distance": "assets/effect/distance.png",
    "distanceboost": "assets/effect/distanceboost.png"
}

framelength = {
    "health": 1,
    "health2": 1,
    "speed": 1,
    "speedboost": CONSTANTS.TICK*CONSTANTS.BOOSTLENGTH,
    "crit": 1,
    "critboost": CONSTANTS.TICK*CONSTANTS.BOOSTLENGTH,
    "attack": 1,
    "attackboost": CONSTANTS.TICK*CONSTANTS.BOOSTLENGTH,
    "distance": 1,
    "distanceboost": CONSTANTS.TICK*CONSTANTS.BOOSTLENGTH,
}

def effectEvents(state):
    pass
    for e in state.effects:
        if e.used:
            continue
        if e.effect == "health":
            health(state)
        elif e.effect == "health2":
            health2(state)
        elif e.effect == "speed":
            speed(state)
        elif e.effect == "speedboost":
            speedboost(state)
        elif e.effect == "crit":
            crit(state)
        elif e.effect == "critboost":
            critboost(state)
        elif e.effect == "attack":
            attack(state)
        elif e.effect == "attackboost":
            attackboost(state)
        elif e.effect == "distance":
            distance(state)
        elif e.effect == "distanceboost":
            distanceboost(state)
        e.used = True

class Effect():
    def __init__(self, x, y, frame, effect):
        self.x = x
        self.y = y
        self.used = False
        self.effect = effect
        #self.start_frame = frame
        #self.end_frame = framelength[effect]

def drop_effect(x,y, state):
    if random.randint(0,4) == 0:
        e = random.choices(effect_list, weights=effect_weights, k=1)[0]
        if e in ["speed", "crit", "attack"]:
            e = random.choices([e, e+"_speed"], weights=(2,1), k=1)[0]
        effect = Effect(x,y, state.frame, e)
        state.effects.append(effect)