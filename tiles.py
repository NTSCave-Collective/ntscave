tiles = {
    "floor": "assets/tiles/floor.png",
    "floor2": "assets/tiles/floor2.png",
    "floor3": "assets/tiles/floor3.png",

    "frontwall_center": "assets/tiles/frontwall_center.png",
    "frontwall_left": "assets/tiles/frontwall_left.png",
    "frontwall_right": "assets/tiles/frontwall_right.png",

    "wall_left": "assets/tiles/wall_left.png",
    "wall_right": "assets/tiles/wall_right.png",
    "wall_bottom": "assets/tiles/wall_bottom.png",

    "wallcorner_topleft": "assets/tiles/wallcorner_topleft.png",
    "wallcorner_topright": "assets/tiles/wallcorner_topright.png",
    "wallcorner_bottomleft": "assets/tiles/wallcorner_bottomleft.png",
    "wallcorner_bottomright": "assets/tiles/wallcorner_bottomright.png",
    
    "stairs_down": "assets/tiles/stairs_down.png",

    "spike": "assets/tiles/spike0.png",
    "spike1": "assets/tiles/spike1.png",
    "spike2": "assets/tiles/spike2.png",
    "spike3": "assets/tiles/spike3.png"
}

player = {
    "down": "assets/player/down.png",
    "left": "assets/player/left.png",
    "right": "assets/player/right.png"
}

collision = {
    "left": ["wall_left", "wallcorner_bottomleft", "wallcorner_topleft"],
    "right": ["wall_right", "wallcorner_topright", "wallcorner_bottomright"],
    "up": ["frontwall_left","frontwall_center", "frontwall_right", "wallcorner_topleft", "wallcorner_topright"],
    "down": ["wall_bottom", "wallcorner_bottomleft", "wallcorner_bottomright"],
    "center": ["spike", "spike1", "spike2", "spike3", "stairs_down"]
}

colission_offsets = {"left": 24, "right": -24, "down": -16, "up": 0}