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
    clock = pygame.time.Clock()

    running = True

    # Create window with given size
    window_flags = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.SCALED
    window = pygame.display.set_mode(CONSTANTS.SCREEN_SIZE, window_flags, vsync=CONSTANTS.VSYNC)

    # All gameObjects except the bg is added to this surface to be able to move the camera with the player
    gameObjects = pygame.Surface(
        (CONSTANTS.SURFACE_WIDTH, CONSTANTS.SURFACE_HEIGHT), pygame.SRCALPHA, 32)
    gameObjects = gameObjects.convert_alpha()

    num_random_enemies = random.randint(1, 5)
    enemies = enemy.spawn_enemies_on_floor((state.x, state.y), num_random_enemies)

    state.enemies = enemies
    
    
    while running:
        rendering.clear_surface(window)

        pygame.event.pump()

        globalEvents = pygame.event.get()
        for event in globalEvents:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    CONSTANTS.MAP = CONSTANTS.MAP_SKELETONS
                if event.key == pygame.K_y:
                    CONSTANTS.MAP = CONSTANTS.BACKGROUND_IMAGES
                if event.key == pygame.K_f:
                    rendering.toggle_fullscreen(window)
                if event.key == pygame.K_i:
                    CONSTANTS.MAP = ROOMS.generateRoom(state)
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                CONSTANTS.SCREEN_SIZE = event.size
                CONSTANTS.SCREEN_WIDTH = CONSTANTS.SCREEN_SIZE[0]
                CONSTANTS.SCREEN_HEIGHT = CONSTANTS.SCREEN_SIZE[1]
                CONSTANTS.BOUND = math.ceil(max(CONSTANTS.SCREEN_HEIGHT, CONSTANTS.SCREEN_WIDTH)/2)+2
                window = pygame.display.set_mode(CONSTANTS.SCREEN_SIZE, window_flags, vsync=CONSTANTS.VSYNC)

        # Player events
        player.playerEvents(state)

        # All gameObjects get rendered in here
        rendering.render_frame(window, gameObjects, state)

        # Set fps value
        clock.tick(CONSTANTS.TICK)
        state.frame += 1
        # print(clock.get_fps())


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

        self.hp = 100

        self.attacking = False
        self.leftFacing = False
        self.rightFacing = False
        self.upFacing = False
        self.downFacing = True  # Default facing down
        self.enemies = []


if __name__ == "__main__":
    main()
