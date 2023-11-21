# Initial Screen constants
SCREEN_SIZE = (1024, 768)
BACKGROUND_COLOR = [34, 34, 34]
TICK = 60
SURFACE_SCREEN = 5000

# Grid constants 
GRID_SPACING = 1000
GRID_COLOR = [0, 0, 0]

# Camera constants 
EXPANSION_THRESHOLD = 50

# Player constants
PLAYER_START_X_POSITION =  SCREEN_SIZE[0] // 2
PLAYER_START_Y_POSITION = SCREEN_SIZE[1] // 2
PLAYER_SPEED = 2

# Ball constants
COLOR_BALL = [0, 0, 0]
RADIUS_BALL = 10


# Background images
BACKGROUND_IMAGES = [
        ["wallcorner_topleft","frontwall_center","frontwall_center","frontwall_center","frontwall_center","frontwall_center","frontwall_center","wallcorner_topright"],
        ["wall_left","floor","floor","floor","floor","floor","floor","wall_right"],
        ["wall_left","floor2","floor","floor","floor","floor","floor","wall_right","frontwall_left","frontwall_center","frontwall_right"],
        ["wall_left","floor3","floor3","floor","floor","floor","floor","wall_right"],
        ["wall_left","floor3","floor2","floor3","stairs_down","floor","floor3","wall_right"],
        ["wall_left","floor3","floor2","floor3","floor","floor","floor3","wall_right"],
        ["wall_left","floor3","floor","spike","spike1","spike2","spike3","wall_right"],
        ["wallcorner_bottomleft","wall_bottom","wall_bottom","wall_bottom","wall_bottom","wall_bottom","wall_bottom","wallcorner_bottomright"],
    ]


PIXELS = 64