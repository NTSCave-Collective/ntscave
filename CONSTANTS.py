import ROOMS
import math
import random

# Initial Screen constants
DEBUG = False

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BACKGROUND_COLOR = [34, 34, 34]
TICK =  60

PIXELS = 64

BOUND = math.ceil(max(SCREEN_HEIGHT, SCREEN_WIDTH)/2 /PIXELS +2)

VSYNC = 0
# Grid constants 
GRID_SPACING = 1000
GRID_COLOR = [0, 0, 0]

TEXT_COLOR = "#7289da"

# Camera constants 
EXPANSION_THRESHOLD = 50

PIXELS = 64

# Player constants
PLAYER_START_X_POSITION =  SCREEN_WIDTH // 2
PLAYER_START_Y_POSITION = SCREEN_HEIGHT // 2
PLAYER_SPEED = 5

ATTACKDISTANCE = PIXELS
BUFFER = 20


def BOOSTLENGTH():
    return random.randint(5,150)
CRITSCALE = 20

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

roomHeight = 12
roomWidth = 12

SURFACE_WIDTH = PIXELS * len(MAP)
SURFACE_HEIGHT = PIXELS * max([len(y) for y in MAP])


# Amount of enemies killed 
WORM_COUNTER = 0
TROJAN_COUNTER = 0
VIRUS_COUNTER = 0