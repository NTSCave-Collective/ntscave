import CONSTANTS
import BOUNDINGS
import pygame
import os
import animation

tiles = {
    None: "assets/tiles/none.png",
    "floor": "assets/tiles/floor.png",
    "floor2": "assets/tiles/floor2.png",
    "floor3": "assets/tiles/floor3.png",

    "frontwall_center": "assets/tiles/frontwall_center.png",
    "frontwall_left": "assets/tiles/frontwall_left.png",
    "frontwall_right": "assets/tiles/frontwall_right.png",

    "wall_left": "assets/tiles/wall_left.png",
    "wall_right": "assets/tiles/wall_right.png",
    "wall_bottom": "assets/tiles/wall_bottom.png",

    "wallcorner_left": "assets/tiles/wallcorner_left.png",
    "wallcorner_right": "assets/tiles/wallcorner_right.png",
    "wallcorner_topleft": "assets/tiles/wallcorner_topleft.png",
    "wallcorner_topright": "assets/tiles/wallcorner_topright.png",
    "wallcorner_bottomleft": "assets/tiles/wallcorner_bottomleft.png",
    "wallcorner_bottomright": "assets/tiles/wallcorner_bottomright.png",

    "singlewall_bottom_connected": "assets/tiles/singlewall_bottom_connected.png",
    "singlewall_right_connected": "assets/tiles/singlewall_right_connected.png",
    "singlewall_left_connected": "assets/tiles/singlewall_left_connected.png",
    "singlewall_top_connected": "assets/tiles/singlewall_top_connected.png",

    "void_connection_topleft": "assets/tiles/void_connection_topleft.png",

    "wall_single": "assets/tiles/wall_single.png",
    
    "stairs_down": "assets/tiles/stairs_down.png",

    "spike": "assets/tiles/spike0.png",
    "spike1": "assets/tiles/spike1.png",
    "spike2": "assets/tiles/spike2.png",
    "spike3": "assets/tiles/spike3.png",
    "spike_blocked": "assets/tiles/spike3.png"
}


player = {
    "down": ["assets/player/down.png", "assets/player/down2.png", "assets/player/down3.png", "assets/player/down4.png"],
    "left": ["assets/player/left.png", "assets/player/left2.png", "assets/player/left3.png", "assets/player/left4.png"],
    "right": ["assets/player/right.png", "assets/player/right2.png", "assets/player/right3.png", "assets/player/right4.png"],
    "up": ["assets/player/up.png", "assets/player/up2.png", "assets/player/up3.png", "assets/player/up4.png"],

    "down_moving": ["assets/player/down_moving.png", "assets/player/down_moving2.png", "assets/player/down_moving3.png", "assets/player/down_moving4.png"],
    "left_moving": ["assets/player/left_moving.png", "assets/player/left_moving2.png", "assets/player/left_moving3.png", "assets/player/left_moving4.png"],
    "right_moving": ["assets/player/right_moving.png", "assets/player/right_moving2.png", "assets/player/right_moving3.png", "assets/player/right_moving4.png"],
    "up_moving": ["assets/player/up_moving.png", "assets/player/up_moving2.png", "assets/player/up_moving3.png", "assets/player/up_moving4.png"],

    "spin": ["assets/player/down_moving.png", "assets/player/right_moving2.png", "assets/player/up_moving3.png", "assets/player/left_moving4.png"]
}

worm = {
    "left": ["assets/enemy/worm_left1.png", "assets/enemy/worm_left2.png", "assets/enemy/worm_left3.png", "assets/enemy/worm_left2.png"],
    "up": ["assets/enemy/worm_left1.png", "assets/enemy/worm_left2.png", "assets/enemy/worm_left3.png", "assets/enemy/worm_left2.png"],
    "right": ["assets/enemy/worm_right1.png", "assets/enemy/worm_right2.png", "assets/enemy/worm_right3.png", "assets/enemy/worm_right2.png"],
    "down": ["assets/enemy/worm_right1.png", "assets/enemy/worm_right2.png", "assets/enemy/worm_right3.png", "assets/enemy/worm_right2.png"]
}

trojan = {
    "left": ["assets/enemy/trojan_left1.png", "assets/enemy/trojan_left2.png", "assets/enemy/trojan_left1.png", "assets/enemy/trojan_left2.png"],
    "up": ["assets/enemy/trojan_left1.png", "assets/enemy/trojan_left2.png", "assets/enemy/trojan_left1.png", "assets/enemy/trojan_left2.png"],
    "right": ["assets/enemy/trojan_right1.png", "assets/enemy/trojan_right2.png", "assets/enemy/trojan_right1.png", "assets/enemy/trojan_right2.png"],
    "down": ["assets/enemy/trojan_right1.png", "assets/enemy/trojan_right2.png", "assets/enemy/trojan_right1.png", "assets/enemy/trojan_right2.png"]
}

slash = {
    "left": ["assets/slash/left.png", "assets/slash/left2.png", "assets/slash/left3.png", "assets/empty.png"],
    "right": ["assets/slash/right.png", "assets/slash/right2.png", "assets/slash/right3.png", "assets/empty.png"],
    "up": ["assets/slash/up.png", "assets/slash/up2.png", "assets/slash/up3.png", "assets/empty.png"],
    "down": ["assets/slash/down.png", "assets/slash/down2.png", "assets/slash/down3.png", "assets/empty.png"]
}

hud = {
    "heart_full": "assets/player/heart_full.png",
    "heart_half": "assets/player/heart_half.png",
}

spike = ["spike1", "spike2"] + ["spike3"] * 55 + ["spike2", "spike", "spike"]

species_list = ["worm", "trojan"]
name_to_entity = {"worm": worm, "trojan": trojan, "spike": spike}

event_for_bound_blocks = ["spike", "spike1", "spike2", "spike3", "stairs_down"]

bounds = {
    None: BOUNDINGS.no_bounding,
    
    "floor": BOUNDINGS.no_bounding,
    "floor2": BOUNDINGS.no_bounding,
    "floor3": BOUNDINGS.no_bounding,

    "frontwall_center": BOUNDINGS.full_bounding,
    "frontwall_left": BOUNDINGS.full_bounding,
    "frontwall_right": BOUNDINGS.full_bounding,

    "wall_left": BOUNDINGS.left,
    "wall_right": BOUNDINGS.right,
    "wall_bottom": BOUNDINGS.bottom,

    "wallcorner_left": BOUNDINGS.left,
    "wallcorner_right": BOUNDINGS.right,
    "wallcorner_topleft": BOUNDINGS.topleft_fill,
    "wallcorner_topright": BOUNDINGS.topright_fill,
    "wallcorner_bottomleft": BOUNDINGS.bottomleft_fill,
    "wallcorner_bottomright": BOUNDINGS.bottomright_fill,

    "singlewall_bottom_connected": BOUNDINGS.full_bounding,
    "singlewall_right_connected": BOUNDINGS.full_bounding,
    "singlewall_left_connected": BOUNDINGS.full_bounding,
    "singlewall_top_connected": BOUNDINGS.full_bounding,
    "wall_single": BOUNDINGS.full_bounding,

    "void_connection_topleft": BOUNDINGS.bottomright_cut,
    
    "stairs_down": BOUNDINGS.center,

    "spike": BOUNDINGS.center,
    "spike1": BOUNDINGS.center,
    "spike2": BOUNDINGS.center,
    "spike3": BOUNDINGS.center,
}

def next_level(state):
    state.level += 1
    CONSTANTS.roomHeight += 2
    CONSTANTS.roomWidth += 2
    if CONSTANTS.roomHeight > 150 or CONSTANTS.roomWidth > 150:
        CONSTANTS.TICK = 30
    CONSTANTS.SURFACE_WIDTH = CONSTANTS.PIXELS * CONSTANTS.roomWidth
    CONSTANTS.SURFACE_HEIGHT = CONSTANTS.PIXELS * CONSTANTS.roomHeight
    state.newLevel_frame = state.frame
    state.newLevel = True
    state.newLevelWidth = True

def spike_damage(state):
    if state.last_hit < state.frame:
        state.last_hit = state.frame + CONSTANTS.TICK*2
        state.hearts -= 1

def tileEvents(x, y, tile, state):
    pre_anim = [(anim.x, anim.y) for anim in state.animations]
    if tile == "stairs_down":
        next_level(state)

    elif tile == "spike":
        state.animations.append(animation.Animation(x, y, state.frame, tile))
        
    elif tile == "spike2":
        spike_damage(state)