import pygame
import player
import CONSTANTS
import random
import enemy 
import rendering
global running
import ROOMS
import math


def main():
    # Initialize Pygame
    pygame.init()
    state = State()
    create_main_surface(state)


def create_main_surface(state):
    # Tuple representing width and height in pixels
    state.clock = pygame.time.Clock()

    running = True

    # Create window with given size
    window_flags = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.SCALED
    window = pygame.display.set_mode(CONSTANTS.SCREEN_SIZE, window_flags, vsync=CONSTANTS.VSYNC)

    # All gameObjects except the bg is added to this surface to be able to move the camera with the player
    gameObjects = pygame.Surface(
        (CONSTANTS.SURFACE_WIDTH, CONSTANTS.SURFACE_HEIGHT), pygame.SRCALPHA, 32)
    gameObjects = gameObjects.convert_alpha()

    enemy.generate_enemies(state)
    
    
    while running:
        if state.newLevelWidth == True:
            gameObjects = pygame.Surface(
                (CONSTANTS.SURFACE_WIDTH, CONSTANTS.SURFACE_HEIGHT), pygame.SRCALPHA, 32)
            gameObjects = gameObjects.convert_alpha()
            state.newLevelWidth = False
        

        rendering.clear_surface(window)

        pygame.event.pump()

        globalEvents = pygame.event.get()
        for event in globalEvents:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    ROOMS.swap_map(state, CONSTANTS.MAP_SKELETONS)
                if event.key == pygame.K_y:
                    ROOMS.swap_map(state, CONSTANTS.BACKGROUND_IMAGES)
                if event.key == pygame.K_i:
                    ROOMS.swap_map(state, "random")
                if event.key == pygame.K_f:
                    rendering.toggle_fullscreen(window)
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                CONSTANTS.SCREEN_SIZE = event.size
                CONSTANTS.SCREEN_WIDTH = CONSTANTS.SCREEN_SIZE[0]
                CONSTANTS.SCREEN_HEIGHT = CONSTANTS.SCREEN_SIZE[1]
                CONSTANTS.BOUND = math.ceil(max(CONSTANTS.SCREEN_HEIGHT, CONSTANTS.SCREEN_WIDTH)/2 /CONSTANTS.PIXELS +2) *CONSTANTS.PIXELS
                window = pygame.display.set_mode(CONSTANTS.SCREEN_SIZE, window_flags, vsync=CONSTANTS.VSYNC)

        # Player events
        if state.newLevel == False:
            player.playerEvents(state)

        # All gameObjects get rendered in here
        rendering.render_frame(window, gameObjects, state)

        # Set fps value
        state.clock.tick(CONSTANTS.TICK)
        state.frame += 1
        #print(state.clock.get_fps())


class State():
    def __init__(self):
        map = CONSTANTS.MAP
        # print(map)
        validTile = False
        while not validTile:
            randY = random.randint(0, len(map))
            randX = random.randint(0, len(map[0]))
            try:
                if "floor" in map[randY][randX]:
                    self.x = randX * CONSTANTS.PIXELS + 32
                    self.y = randY * CONSTANTS.PIXELS + 32
                    validTile = True
            except:
                pass
        self.vel = CONSTANTS.PLAYER_SPEED
        self.frame = 0

        self.level = 1

        self.last_hit = CONSTANTS.TICK
        self.hearts = 3

        self.attacking = False
        self.attackframe = None

        self.leftFacing = False
        self.rightFacing = False
        self.upFacing = False
        self.downFacing = True  # Default facing down
        self.enemies = list()
        self.animations = list()

        self.newLevel = False
        self.newLevel_frame = None
        self.newLevelWidth = False

if __name__ == "__main__":
    main()