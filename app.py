import pygame

global running

def main():
    # Initialize Pygame
    pygame.init()
    create_main_surface()



def create_main_surface():
    # Tuple representing width and height in pixels
    screen_size = (1024, 768)
    
    running = True

    while running:
        pygame.event.pump()
        # Create window with given size
        pygame.display.set_mode(screen_size)
        windowEvent = pygame.event.get()
        for event in windowEvent:
            if event.type == pygame.QUIT:
                running = False


main()


