import pygame
import player

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
        myWindow = pygame.display.set_mode(screen_size)
        myWindow.fill([255,255,255])
        windowEvent = pygame.event.get()
        player.drawCircle(myWindow)
        for event in windowEvent:
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

if __name__ == "__main__":
    main()
