import pygame
import sys
from button import Button
import player
import CONSTANTS
import random
import enemy
import rendering
global running
import ROOMS
import math

pygame.init()

window_flags = pygame.RESIZABLE | pygame.DOUBLEBUF
SCREEN = pygame.display.set_mode(CONSTANTS.SCREEN_SIZE, window_flags, vsync=CONSTANTS.VSYNC)
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def main(window, window_flags):
    # Initialize Pygame
    pygame.init()
    create_main_surface(state, window, window_flags)

def create_main_surface(state, window, window_flags):
    # Tuple representing width and height in pixels
    state.clock = pygame.time.Clock()

    running = True

    # Create window with given size
    # window_flags = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.SCALED
    # window = pygame.display.set_mode(CONSTANTS.SCREEN_SIZE, window_flags, vsync=CONSTANTS.VSYNC)

    # All gameObjects except the bg is added to this surface to be able to move the camera with the player
    gameObjects = pygame.Surface((CONSTANTS.SURFACE_WIDTH, CONSTANTS.SURFACE_HEIGHT), pygame.SRCALPHA, 32).convert_alpha()    
    
    while running:
        if state.newLevelWidth == True:
            gameObjects = pygame.Surface(
                (CONSTANTS.SURFACE_WIDTH, CONSTANTS.SURFACE_HEIGHT), pygame.SRCALPHA, 32)
            gameObjects = gameObjects.convert_alpha()
            state.newLevelWidth = False
        

        rendering.clear_surface(window)

        pygame.event.pump()

        globalEvents = pygame.event.get()
        for event in globalEvents:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u and CONSTANTS.DEBUG:
                    ROOMS.swap_map(state, CONSTANTS.MAP_SKELETONS)
                if event.key == pygame.K_y and CONSTANTS.DEBUG:
                    ROOMS.swap_map(state, CONSTANTS.BACKGROUND_IMAGES)
                if event.key == pygame.K_i and CONSTANTS.DEBUG:
                    ROOMS.swap_map(state, "random")
                if event.key == pygame.K_f:
                    CONSTANTS.VSYNC = 0
                    rendering.toggle_fullscreen()
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                CONSTANTS.SCREEN_SIZE = event.size
                CONSTANTS.SCREEN_WIDTH = CONSTANTS.SCREEN_SIZE[0]
                CONSTANTS.SCREEN_HEIGHT = CONSTANTS.SCREEN_SIZE[1]
                CONSTANTS.SURFACE_WIDTH = CONSTANTS.SCREEN_SIZE[0]
                CONSTANTS.SURFACE_HEIGHT = CONSTANTS.SCREEN_SIZE[1]
                CONSTANTS.BOUND = math.ceil(max(CONSTANTS.SCREEN_HEIGHT, CONSTANTS.SCREEN_WIDTH)/2 /CONSTANTS.PIXELS +2) *CONSTANTS.PIXELS
                window = pygame.display.set_mode(CONSTANTS.SCREEN_SIZE, window_flags, vsync=CONSTANTS.VSYNC)

        # Player events
        if state.newLevel == False:
            player.playerEvents(state)

        # All gameObjects get rendered in here
        rendering.render_frame(window, gameObjects, state)

        # Set fps value
        state.clock.tick(CONSTANTS.TICK)
        state.frame += 1
        if not CONSTANTS.DEBUG:
            print(state.clock.get_fps())

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

        self.last_hit = CONSTANTS.TICK
        self.hearts = 5
        
        self.attack = 1
        self.attacking = False
        self.attackframe = None
        self.hit_grace = None
        self.crit = 0.1

        self.leftFacing = False
        self.rightFacing = False
        self.upFacing = False
        self.downFacing = True  # Default facing down

        self.enemies = list()
        self.animations = list()
        self.effects = list()
        self.activeEffects = list()

        self.newLevel = False
        self.newLevel_frame = None
        self.newLevelWidth = False

        # Define hitbox dimensions
        self.hitbox_width = CONSTANTS.PIXELS/2
        self.hitbox_height = CONSTANTS.PIXELS
        self.hitbox_x = self.x - self.hitbox_width / 2
        self.hitbox_y = self.y - self.hitbox_height

        # Initialize hitbox position based on enemy position
        self.update_hitbox_position()

    def update_hitbox_position(self):
        # Update hitbox position based on enemy position
        self.hitbox_x = self.x - self.hitbox_width / 2
        self.hitbox_y = self.y - self.hitbox_height

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(840, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(840, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def options():

    pygame.display.set_caption("Options")

    while True:

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(840, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(300, 550), 
                            text_input="BACK", font=get_font(20), base_color="White", hovering_color="Green")

        VIDEOSETTINGS_BUTTON = Button(image=None, pos=(390, 250),
                             text_input="VIDEO SETTINGS", font=get_font(20), base_color="White", hovering_color="Green")
        
        CONTROLS_BUTTON = Button(image=None, pos=(330, 300),
                                   text_input="CONTROLS", font=get_font(20), base_color="White", hovering_color="Green")
        
        AUDIOSETTINGS_BUTTON = Button(image=None, pos=(390, 350),
                                   text_input="AUDIO SETTINGS", font=get_font(20), base_color="White", hovering_color="Green")
        
        for button in (VIDEOSETTINGS_BUTTON, OPTIONS_BACK, CONTROLS_BUTTON, AUDIOSETTINGS_BUTTON):
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if VIDEOSETTINGS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    video_settings()
                if CONTROLS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    controls()
                if AUDIOSETTINGS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    audio_settings()

        pygame.display.update()

def audio_settings():

    pygame.display.set_caption("Audio Settings")

    while True:
    
        AUD_SET_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill("Black")
        
        AUD_SET_TEXT = get_font(20).render("AUDIO SETTINGS", True, "White")
        AUD_SET_RECT = AUD_SET_TEXT.get_rect(center=(840, 100))
        SCREEN.blit(AUD_SET_TEXT, AUD_SET_RECT)

        AUD_SET_BACK = Button(image=None, pos=(300, 800),
                              text_input="BACK", font=get_font(20), base_color="White", hovering_color="Green")
        
        AUD_SET_BACK.changeColor(AUD_SET_MOUSE_POS)
        AUD_SET_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AUD_SET_BACK.checkForInput(AUD_SET_MOUSE_POS):
                    options()

        pygame.display.update()

def controls():

    pygame.display.set_caption("Controls")

    while True:

        CONTROLS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        CONTROLS_TEXT = get_font(20).render("CONTROLS", True, "White")
        CONTROLS_RECT = CONTROLS_TEXT.get_rect(center=(840, 100))
        SCREEN.blit(CONTROLS_TEXT, CONTROLS_RECT)

        CONTROLS_BACK = Button(image=None, pos=(300, 800),
                               text_input="BACK", font=get_font(20), base_color="White", hovering_color="Green")
        
        CONTROLS_BACK.changeColor(CONTROLS_MOUSE_POS)
        CONTROLS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTROLS_BACK.checkForInput(CONTROLS_MOUSE_POS):
                    options()

        pygame.display.update()

def video_settings():

    pygame.display.set_caption("Video Settings")

    while True:
    
        VID_SET_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill("Black")
        
        VID_SET_TEXT = get_font(20).render("VIDEO SETTINGS", True, "White")
        VID_SET_RECT = VID_SET_TEXT.get_rect(center=(840, 100))
        SCREEN.blit(VID_SET_TEXT, VID_SET_RECT)

        VID_SET_BACK = Button(image=None, pos=(300, 800),
                              text_input="BACK", font=get_font(20), base_color="White", hovering_color="Green")
        
        VID_SET_BACK.changeColor(VID_SET_MOUSE_POS)
        VID_SET_BACK.update(SCREEN)

        VSYNC_TEXT = get_font(20).render("VSYNC", True, "White")
        VSYNC_RECT = VSYNC_TEXT.get_rect(center=(310, 250))
        SCREEN.blit(VSYNC_TEXT, VSYNC_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VID_SET_BACK.checkForInput(VID_SET_MOUSE_POS):
                    options()

        pygame.display.update()

def main_menu():
    
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(840, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(840, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(840, 400),
                             text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(840, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main(SCREEN, window_flags)
                    # play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

state = State()
enemy.generate_enemies(state)
main_menu()