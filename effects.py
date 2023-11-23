import pygame
import os
import CONSTANTS

effect_list = ["health", "speed", "crit", "attack"]
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

effect_to_func = {"health": health(state), "health2": health2()}

class Effect():
    def __init__(self, frame, effect):
        self.start_frame = frame
        self.frame = frame
        self.effect = effect
