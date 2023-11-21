import pygame
import renderer
import player
import camera
import grid

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
    gameObjects = pygame.Surface((5000,5000), pygame.SRCALPHA, 32)
    gameObjects = gameObjects.convert_alpha()

    while running:
        renderer.clear_surface(window)

        pygame.event.pump()
        
        globalEvents = pygame.event.get()
        for event in globalEvents:
            if event.type == pygame.QUIT:
                running = False

        # Player events
        player.playerEvents(state)

        print(state.leftFacing, state.rightFacing, state.upFacing, state.downFacing)

        grid.draw_grid(gameObjects, screen_size, (0,0,0), 20)

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
        self.vel = 5
        
        self.attacking = False

        self.leftFacing = False
        self.rightFacing = False
        self.upFacing = False
        self.downFacing = True # Default facing down



if __name__ == "__main__":
    main()