import tiles
from math import floor
import CONSTANTS

class Animation():
    def __init__(self, x, y, frame, tile):
        self.x = x
        self.y = y
        self.start_frame = frame
        self.frame = frame
        self.tile = tile

def tileAnimations(state):
    for anim in state.animations:

        newTile = tiles.name_to_entity[anim.tile]
        animframe = floor(((anim.frame - anim.start_frame) % CONSTANTS.TICK) / (CONSTANTS.TICK/len(newTile)))

        anim.frame += 1
        
        CONSTANTS.MAP[anim.y][anim.x] = newTile[animframe]
        if anim.frame == (anim.start_frame + CONSTANTS.TICK -1):
            anim.frame = None

    state.animations = list(filter(lambda a: a.frame != None, state.animations))
    