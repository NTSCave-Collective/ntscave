import ROOMS
import math

# Initial Screen constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BACKGROUND_COLOR = [34, 34, 34]
TICK =  60

PIXELS = 64

roomHeight = 10
roomWidth = 10

BOUND = math.ceil(max(SCREEN_HEIGHT, SCREEN_WIDTH)/2 /PIXELS +2) *PIXELS

SURFACE_WIDTH = PIXELS * roomWidth
SURFACE_HEIGHT = PIXELS * roomHeight

VSYNC = 0
# Grid constants 
GRID_SPACING = 1000
GRID_COLOR = [0, 0, 0]

# Camera constants 
EXPANSION_THRESHOLD = 50

# Player constants
PLAYER_START_X_POSITION =  SCREEN_WIDTH // 2
PLAYER_START_Y_POSITION = SCREEN_HEIGHT // 2
PLAYER_SPEED = 5

PIXELS = 64


# Background images
BACKGROUND_IMAGES = [
        ["wallcorner_topleft","frontwall_center","frontwall_center","frontwall_center","frontwall_center","frontwall_center","frontwall_center","wallcorner_topright"],
        ["wall_left","floor","floor","floor","floor","floor","floor","wall_right"],
        ["wall_left","floor2","floor","floor","floor","floor","floor","wall_right","frontwall_left","frontwall_center","frontwall_right"],
        ["wall_left","floor3", "floor","floor","floor","floor","floor","wall_right"],
        ["wall_left","floor3","floor2","floor3","stairs_down","floor","floor3","wall_right"],
        ["wall_left","floor3","floor2","floor3","floor","floor","floor3","wall_right"],
        ["wall_left","floor3","floor","spike","spike1","spike2","spike3","wall_right"],
        ["wallcorner_bottomleft","wall_bottom","wall_bottom","wall_bottom","wall_bottom","wall_bottom","wall_bottom","wallcorner_bottomright"],
]

MAP_SKELETONS = [
    [None, "frontwall_center", None],
    [None, "wallcorner_topleft", None],
    ["wallcorner_topleft", "wallcorner_left", None],
    ["wall_left", "floor", "floor"],
    ["wall_left", "frontwall_center", None],
    ["wall_left", "frontwall_center", None],
]

MAP = BACKGROUND_IMAGES