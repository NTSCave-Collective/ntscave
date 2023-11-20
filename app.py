import pygame
import renderer
import player

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

    while running:
        pygame.event.pump()
        globalEvents = pygame.event.get()
        window.fill([255,255,255])
        for event in globalEvents:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                player.playerMovement(event)
        renderer.render_frame(window)
        clock.tick(60)  # number of computation steps per second, should be greater equal to FPS-value

if __name__ == "__main__":
    main()
