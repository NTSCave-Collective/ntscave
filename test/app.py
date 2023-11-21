import pygame
import CONSTANTS
from player import player_events  
import renderer
import camera 
from grid import draw_grid


class State():
    def __init__(self):
        self.x = CONSTANTS.PLAYER_START_X_POSITION
        self.y = CONSTANTS.PLAYER_START_Y_POSITION
        self.vel = CONSTANTS.PLAYER_SPEED

def main():
    pygame.init()
    state = State()
    create_main_surface(state)

def create_main_surface(state):
    clock = pygame.time.Clock()
    running = True
    window_flags = pygame.RESIZABLE | pygame.DOUBLEBUF
    window = pygame.display.set_mode(CONSTANTS.SCREEN_SIZE, window_flags)

    while running:
        clear_surface(window)
        global_events = pygame.event.get()

        for event in global_events:
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

        draw_grid(window, CONSTANTS.SCREEN_SIZE, (state.x, state.y))
        player_events(state)

        ###
        # Hier is nog iets fout
        # Als de bal snel diagonaal rond beweegt zal het op de x of y as vastlopen  
        renderer.render_frame(window, state)
        ###
        pygame.display.flip()
        clock.tick(CONSTANTS.TICK)

def clear_surface(surface):
    surface.fill(CONSTANTS.BACKGROUND_COLOR)

if __name__ == "__main__":
    main()
