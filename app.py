import pygame
import renderer
import time

global running

def main():
    # Initialize Pygame
    pygame.init()
    create_main_surface()



def create_main_surface():
    # Tuple representing width and height in pixels
    screen_size = (1024, 768)
    clock = pygame.time.Clock()
    
    running = True

    # Create window with given size
    window = pygame.display.set_mode(screen_size)
    window.fill([255,255,255])
    
    while running:
        pygame.event.pump()
        windowEvent = pygame.event.get()
        for event in windowEvent:
            if event.type == pygame.QUIT:
                running = False
        renderer.render_frame(window)
        clock.tick(60)  # number of computation steps per second, should be greater equal to FPS-value

if __name__ == "__main__":
    main()
