import pygame
import renderer
import player
import camera
import grid
import CONSTANTS

global running

def main():
    # Initialize Pygame
    pygame.init()
    print(CONSTANTS.SCALE)
    state = State()
    create_main_surface(state)

def create_main_surface(state):
    # Tuple representing width and height in pixels
    clock = pygame.time.Clock()
    
    running = True

    # Create window with given size
    window_flags = pygame.RESIZABLE | pygame.DOUBLEBUF
    window = pygame.display.set_mode(CONSTANTS.SCREEN_SIZE, window_flags)

    # All gameObjects except the bg is added to this surface to be able to move the camera with the player
    gameObjects = pygame.Surface((CONSTANTS.SURFACE_SCREEN, CONSTANTS.SURFACE_SCREEN), pygame.SRCALPHA, 32)
    gameObjects = gameObjects.convert_alpha()

    while running:
        renderer.clear_surface(window)

        pygame.event.pump()
        
        globalEvents = pygame.event.get()
        for event in globalEvents:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    camera.toggle_fullscreen(window)
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.VIDEORESIZE:
                CONSTANTS.SCREEN_SIZE = event.size
                CONSTANTS.SCREEN_WIDTH = event.SCREEN_SIZE[0]
                CONSTANTS.SCREEN_HEIGHT = event.SCREEN_SIZE[1]
                window = pygame.display.set_mode(CONSTANTS.SCREEN_SIZE, window_flags)


        # Player events
        player.playerEvents(state)


        # All gameObjects get rendered in here
        renderer.render_frame(window, gameObjects, state)
        
        # Set fps value
        clock.tick(CONSTANTS.TICK)
        state.frame += 1

class State():
    def __init__(self, x: int = 150, y: int=150):
        self.x = x
        self.y = y
        self.vel = 5
        self.frame = 0
        
        self.attacking = False

        self.leftFacing = False
        self.rightFacing = False
        self.upFacing = False
        self.downFacing = True # Default facing down


no_bounding = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

full_bounding = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]

center = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
]

top = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]

half_top = [
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

left = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 0, 0]
]

half_left = [
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0]
]

right = [
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
]

half_right = [
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
]

bottom = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 1, 1, 1]
]

half_bottom = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 1, 1, 1]
]

topleft_fill = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]

half_topleft_fill = [
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0]
]

bottomleft_fill = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1]
]

half_bottomleft_fill = [
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 1]
]

topright_fill = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]

half_topright_fill = [
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]
]

bottomright_fill = [
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1]
]

half_bottomright_fill = [
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1]
]

topleft_cut = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
]

half_topleft_cut = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1]
]

bottomleft_cut = [
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

half_bottomleft_cut = [
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

topright_cut = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 0, 0]
]

half_topright_cut = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 0]
]

bottomright_cut = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

half_bottomright_cut = [
    [1, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

def camera(window, gameObjects, state):
    # Move every gameObject on the screen relative to the player position
    window.blit(gameObjects, (CONSTANTS.SCREEN_WIDTH/2 - state.x, CONSTANTS.SCREEN_HEIGHT/2 - state.y))
    # Remove previous gameObjects
    renderer.clear_surface(gameObjects)


def toggle_fullscreen(window):
    pygame.display.toggle_fullscreen()
    return pygame.display.get_surface(
    )


# Initial Screen constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BACKGROUND_COLOR = [34, 34, 34]
TICK = 60
SURFACE_SCREEN = 5000

# Grid constants 
GRID_SPACING = 1000
GRID_COLOR = [0, 0, 0]

# Camera constants 
EXPANSION_THRESHOLD = 50

# Player constants
PLAYER_START_X_POSITION =  SCREEN_WIDTH // 2
PLAYER_START_Y_POSITION = SCREEN_HEIGHT // 2
PLAYER_SPEED = 2

# Ball constants
COLOR_BALL = [0, 0, 0]
RADIUS_BALL = 10


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



PLAYER_PNG_SIZE = 48
PIXELS = 64
QUARTER = PIXELS//4
SCALE = round(PIXELS / 64)
PLAYER_SCALE = PLAYER_PNG_SIZE*SCALE


def draw_grid(gameObjects, screen_size, grid_color, grid_spacing):
    width, height = screen_size
    global gridMap
    gridMap = CONSTANTS.MAP


    for y in range(len(gridMap)):
        for x in range(len(gridMap[y])):
            try:
                image = pygame.image.load(os.path.join(tiles.tiles[gridMap[y][x]]))
                image = pygame.transform.scale(image, (CONSTANTS.PIXELS, CONSTANTS.PIXELS))
                gameObjects.blit(image, (CONSTANTS.PIXELS * x , CONSTANTS.PIXELS * y))
            except:
                pass



def drawPlayer(window, state):
    # 48px x 24px

    state.attacking = False
    
    animframe = floor((state.frame % 40) / 10)

    if state.attacking:
        if state.downFacing:
            player = pygame.image.load(os.path.join(tiles.player["down_attack"][animframe])).convert_alpha()
        elif state.rightFacing:
            player = pygame.image.load(os.path.join(tiles.player["right_attack"][animframe])).convert_alpha()
        elif state.leftFacing:
            player = pygame.image.load(os.path.join(tiles.player["left_attack"][animframe])).convert_alpha()
        elif state.upFacing:
            # player = pygame.image.load(os.path.join(tiles.player["up_attack"][animframe])).convert_alpha()
            return
    elif state.moving:
        if state.downFacing:
            player = pygame.image.load(os.path.join(tiles.player["down_moving"][animframe])).convert_alpha()
        elif state.rightFacing:
            player = pygame.image.load(os.path.join(tiles.player["right_moving"][animframe])).convert_alpha()
        elif state.leftFacing:
            player = pygame.image.load(os.path.join(tiles.player["left_moving"][animframe])).convert_alpha()
        elif state.upFacing:
            # player = pygame.image.load(os.path.join(tiles.player["up_moving"][animframe])).convert_alpha()
            return
    else:
        if state.downFacing:
            player = pygame.image.load(os.path.join(tiles.player["down"][animframe])).convert_alpha()
        elif state.rightFacing:
            player = pygame.image.load(os.path.join(tiles.player["right"][animframe])).convert_alpha()
        elif state.leftFacing:
            player = pygame.image.load(os.path.join(tiles.player["left"][animframe])).convert_alpha()
        elif state.upFacing:
            # player = pygame.image.load(os.path.join(tiles.player["up"][animframe])).convert_alpha()
            return

    window.blit(player, (state.x - 24, state.y - 48))

def playerEvents(state):
    keys = pygame.key.get_pressed()

    def collision(heading):
        tilePosX = floor(((state.x) / CONSTANTS.PIXELS) % len(CONSTANTS.MAP[0]))
        tilePosY = floor(((state.y) / CONSTANTS.PIXELS) % len(CONSTANTS.MAP))

        try:
            currentTile = CONSTANTS.MAP[tilePosY][tilePosX]
        except:
            return True
        
        playertileX = state.x % CONSTANTS.PIXELS // CONSTANTS.QUARTER
        playertileY = state.y % CONSTANTS.PIXELS // CONSTANTS.QUARTER

        print(currentTile)
        print(playertileX)
        print(playertileY)

        return not (tiles.bounds[currentTile][playertileY][playertileX] and not currentTile in tiles.event_for_bound_blocks)

    def movement():
        state.moving = False
        if keys[pygame.K_LEFT]:
            state.moving = True
            state.x -= state.vel
            if not collision("left"):
                state.x += state.vel
            state.rightFacing = False
            state.leftFacing = True
            if not keys[pygame.K_UP]:
                state.upFacing = False
            if not keys[pygame.K_DOWN]:
                state.downFacing = False

        if keys[pygame.K_RIGHT]:
            state.moving = True
            state.x += state.vel
            if not collision("right"):
                state.x -= state.vel
            state.rightFacing = True
            state.leftFacing = False
            if not keys[pygame.K_UP]:
                state.upFacing = False
            if not keys[pygame.K_DOWN]:
                state.downFacing = False

        if keys[pygame.K_UP]:
            state.moving = True
            state.y -= state.vel
            if not collision("up"):
                state.y += state.vel
            state.upFacing = True
            state.downFacing = False
            if not keys[pygame.K_LEFT]:
                state.leftFacing = False
            if not keys[pygame.K_RIGHT]:
                state.rightFacing = False

        if keys[pygame.K_DOWN]:
            state.moving = True
            state.y += state.vel
            if not collision("down"):
                state.y -= state.vel
            state.upFacing = False
            state.downFacing = True
            if not keys[pygame.K_LEFT]:
                state.leftFacing = False
            if not keys[pygame.K_RIGHT]:
                state.rightFacing = False

    def attack():
        if keys[pygame.K_SPACE]:
            state.attacking = True

    
    movement()
    attack()


def render_frame(window, gameObjects, state):
    grid.draw_grid(gameObjects, CONSTANTS.SCREEN_SIZE, CONSTANTS.BACKGROUND_COLOR, CONSTANTS.RADIUS_BALL)
    player.drawPlayer(gameObjects, state)

    # Move all gameObjects based on the player position 
    camera.camera(window, gameObjects, state)
    
    pygame.display.update()



def clear_surface(window):
    window.fill(CONSTANTS.BACKGROUND_COLOR)

import CONSTANTS
import BOUNDINGS

tiles = {
    "floor": "assets/tiles/floor.png",
    "floor2": "assets/tiles/floor2.png",
    "floor3": "assets/tiles/floor3.png",
    "floor_topleft": "assets/tiles/floor_topleft.png",

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
    
    "stairs_down": "assets/tiles/stairs_down.png",

    "spike": "assets/tiles/spike0.png",
    "spike1": "assets/tiles/spike1.png",
    "spike2": "assets/tiles/spike2.png",
    "spike3": "assets/tiles/spike3.png"
}

player = {
    "down": ["assets/player/down.png", "assets/player/down2.png", "assets/player/down3.png", "assets/player/down4.png"],
    "left": ["assets/player/left.png", "assets/player/left.png", "assets/player/left.png", "assets/player/left.png"],
    "right": ["assets/player/right.png", "assets/player/right.png", "assets/player/right.png", "assets/player/right.png"],
    "up": ["assets/player/down.png", "assets/player/down2.png", "assets/player/down3.png", "assets/player/down4.png"],

    "down_moving": ["assets/player/down.png", "assets/player/down_moving2.png", "assets/player/down_moving3.png", "assets/player/down_moving4.png"],
    "left_moving": ["assets/player/left.png", "assets/player/left.png", "assets/player/left.png", "assets/player/left.png"],
    "right_moving": ["assets/player/right.png", "assets/player/right.png", "assets/player/right.png", "assets/player/right.png"],
    "up_moving": ["assets/player/down.png", "assets/player/down2.png", "assets/player/down3.png", "assets/player/down4.png"],

    "down_attack": ["assets/player/down.png", "assets/player/down2.png", "assets/player/down3.png", "assets/player/down4.png"],
    "left_attack": ["assets/player/left.png", "assets/player/left.png", "assets/player/left.png", "assets/player/left.png"],
    "right_attack": ["assets/player/right.png", "assets/player/right.png", "assets/player/right.png", "assets/player/right.png"],
    "up_attack": ["assets/player/down.png", "assets/player/down2.png", "assets/player/down3.png", "assets/player/down4.png"]
}

collision = {
    "left": ["wall_left", "wallcorner_bottomleft", "wallcorner_topleft", "wallcorner_left"],
    "right": ["wall_right", "wallcorner_topright", "wallcorner_bottomright", "wallcorner_right"],
    "up": ["frontwall_left","frontwall_center", "frontwall_right", "wallcorner_topleft", "wallcorner_topright"],
    "down": ["wall_bottom", "wallcorner_bottomleft", "wallcorner_bottomright"],
    "center": ["spike", "spike1", "spike2", "spike3", "stairs_down"]
}

event_for_bound_blocks = ["spike", "spike1", "spike2", "spike3", "stairs_down"]

bounds = {
    None: BOUNDINGS.no_bounding,
    
    "floor": BOUNDINGS.no_bounding,
    "floor2": BOUNDINGS.no_bounding,
    "floor3": BOUNDINGS.no_bounding,

    "frontwall_center": BOUNDINGS.top,
    "frontwall_left": BOUNDINGS.top,
    "frontwall_right": BOUNDINGS.top,

    "wall_left": BOUNDINGS.left,
    "wall_right": BOUNDINGS.right,
    "wall_bottom": BOUNDINGS.bottom,

    "wallcorner_left": BOUNDINGS.left,
    "wallcorner_right": BOUNDINGS.right,
    "wallcorner_topleft": BOUNDINGS.topleft_fill,
    "wallcorner_topright": BOUNDINGS.topright_fill,
    "wallcorner_bottomleft": BOUNDINGS.bottomleft_fill,
    "wallcorner_bottomright": BOUNDINGS.bottomright_fill,
    
    "stairs_down": BOUNDINGS.center,

    "spike": BOUNDINGS.center,
    "spike1": BOUNDINGS.center,
    "spike2": BOUNDINGS.center,
    "spike3": BOUNDINGS.center,
}





if __name__ == "__main__":
    main()