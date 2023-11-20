import pygame
import renderer
import player

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

    while running:
        renderer.clear_surface(window)
        pygame.event.pump()
        globalEvents = pygame.event.get()
        window.fill([255,255,255])
        for event in globalEvents:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                player.playerMovement(event, state)
        renderer.render_frame(window, state)
        clock.tick(60)  # number of computation steps per second, should be greater equal to FPS-value

class State():
    def __init__(self, x: int = 0, y: int=0):
        self.x = x
        self.y = y













if __name__ == "__main__":
    main()
