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
                window = pygame.display.set_mode(CONSTANTS.SCREEN_SIZE, window_flags)


        # Player events
        player.playerEvents(state)


        # All gameObjects get rendered in here
        renderer.render_frame(window, gameObjects, state)
        
        # Set fps value
        clock.tick(CONSTANTS.TICK)
        state.frame += 1

class State():
    def __init__(self, x: int = 100, y: int=100):
        self.x = x
        self.y = y
        self.vel = 5
        self.frame = 0
        
        self.attacking = False

        self.leftFacing = False
        self.rightFacing = False
        self.upFacing = False
        self.downFacing = True # Default facing down



if __name__ == "__main__":
    main()