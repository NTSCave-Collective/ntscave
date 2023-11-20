import pygame
import renderer
import player
import camera

global running

def main():
    # Initialize Pygame
    pygame.init()
    state = State()
    create_main_surface(state)

def create_main_surface(state):
    # Tuple representing width and height in pixels
    screen_size = (1024, 768)
    clock = pygame.time.Clock()
    
    running = True

    # Create window with given size
    window = pygame.display.set_mode(screen_size)

    # All gameObjects except the bg is added to this surface to be able to move the camera with the player
    gameObjects = pygame.Surface(screen_size, pygame.SRCALPHA, 32)
    gameObjects = gameObjects.convert_alpha()

    while running:
        renderer.clear_surface(window)
        
        globalEvents = pygame.event.get()
        for event in globalEvents:
            if event.type == pygame.QUIT:
                running = False

        # Player events
        player.playerMovement(state)

        # Move all gameObjects based on the player position 
        camera.camera(window, gameObjects, state)

        # All gameObjects get rendered in here
        renderer.render_frame(gameObjects, state)
        
        # Set fps value
        clock.tick(60)

class State():
    def __init__(self, x: int = 100, y: int=100):
        self.x = x
        self.y = y
        self.vel = 1


if __name__ == "__main__":
    main()