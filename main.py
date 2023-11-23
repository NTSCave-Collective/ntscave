import pygame, sys, threading
from button import Button
import player
import CONSTANTS
import random
import enemy
import rendering
global running
import ROOMS
import math
from time import sleep

pygame.init()

window_flags = pygame.RESIZABLE | pygame.DOUBLEBUF
SCREEN = pygame.display.set_mode(CONSTANTS.SCREEN_SIZE, window_flags, vsync=CONSTANTS.VSYNC)
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/intro/BG.jpeg")
pygame.transform.scale(BG, (1689, 990))

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
                if event.key == pygame.K_u:
                    ROOMS.swap_map(state, CONSTANTS.MAP_SKELETONS)
                if event.key == pygame.K_y:
                    ROOMS.swap_map(state, CONSTANTS.BACKGROUND_IMAGES)
                if event.key == pygame.K_i:
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
        # print(state.clock.get_fps())

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
        self.hearts = 7.5

        self.attacking = False
        self.attackframe = None

        self.leftFacing = False
        self.rightFacing = False
        self.upFacing = False
        self.downFacing = True  # Default facing down
        self.enemies = list()
        self.animations = list()

        self.newLevel = False
        self.newLevel_frame = None
        self.newLevelWidth = False

def get_font(size):
    return pygame.font.Font("assets/intro/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        PLAY_TEXT = get_font(20).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=((SCREEN.get_width() / 2), 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=((SCREEN.get_width() / 2), 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        
        CREATE_BUTTON = Button(image=None, pos=((SCREEN.get_width() / 10), (SCREEN.get_height() / 10 + 150)))

        for button in (PLAY_BACK, CREATE_BUTTON):
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

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
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=((SCREEN.get_width() / 2), 100))
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
        AUD_SET_RECT = AUD_SET_TEXT.get_rect(center=((SCREEN.get_width() / 2), 100))
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
        CONTROLS_RECT = CONTROLS_TEXT.get_rect(center=((SCREEN.get_width() / 2), 100))
        SCREEN.blit(CONTROLS_TEXT, CONTROLS_RECT)

        MOVE_UP_TEXT = get_font(15).render("MOVE UP", True, "White")
        MOVE_UP_RECT = MOVE_UP_TEXT.get_rect(center=((SCREEN.get_width() / 10) + 90,(SCREEN.get_height() / 10 + 100))) 
        SCREEN.blit(MOVE_UP_TEXT, MOVE_UP_RECT)

        MOVE_DOWN_TEXT = get_font(15).render("MOVE DOWN", True, "White")
        MOVE_DOWN_RECT = MOVE_DOWN_TEXT.get_rect(center=((SCREEN.get_width() / 10) + 105,(SCREEN.get_height() / 10 + 150)))
        SCREEN.blit(MOVE_DOWN_TEXT, MOVE_DOWN_RECT)

        MOVE_LEFT_TEXT = get_font(15).render("MOVE LEFT", True, "White")
        MOVE_LEFT_RECT = MOVE_LEFT_TEXT.get_rect(center=((SCREEN.get_width() / 10) + 105,(SCREEN.get_height() / 10 + 200)))
        SCREEN.blit(MOVE_LEFT_TEXT, MOVE_LEFT_RECT)

        MOVE_RIGHT_TEXT = get_font(15).render("MOVE RIGHT", True, "White")
        MOVE_RIGHT_RECT = MOVE_RIGHT_TEXT.get_rect(center=((SCREEN.get_width() / 10) + 113,(SCREEN.get_height() / 10 + 250)))
        SCREEN.blit(MOVE_RIGHT_TEXT, MOVE_RIGHT_RECT)

        HIT_TEXT = get_font(15).render("HIT", True, "White")
        HIT_RECT = HIT_TEXT.get_rect(center=((SCREEN.get_width() / 10) + 60, (SCREEN.get_height() / 10 + 300)))
        SCREEN.blit(HIT_TEXT, HIT_RECT)

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

def resolution():

    pygame.display.set_caption("Resolution")

    while True:

        SCREEN.fill("Black")

        RESOLUTION_MOUSE_POS = pygame.mouse.get_pos()

        RESOLUTION_TEXT = get_font(20).render("RESOLUTION", True, "White")
        RESOLUTION_RECT = RESOLUTION_TEXT.get_rect(center=((SCREEN.get_width() / 2), 100))
        SCREEN.blit(RESOLUTION_TEXT, RESOLUTION_RECT)

        FULLSCREEN_BUTTON = Button(image=None, pos=(((SCREEN.get_width() / 10) + 5), (SCREEN.get_height() / 10) + 100),
                              text_input="FULLSCREEN", font=get_font(15), base_color="White", hovering_color="Green")
        
        FIRST_BUTTON = Button(image=None, pos=((SCREEN.get_width() / 10) + 13, (SCREEN.get_height() / 10) + 150),
                              text_input="7680 X 4320", font=get_font(15), base_color="White", hovering_color="Green")
        
        SECOND_BUTTON = Button(image=None, pos=(((SCREEN.get_width() / 10) + 10), (SCREEN.get_height() / 10) + 200),
                              text_input="3840 X 2160", font=get_font(15), base_color="White", hovering_color="Green")
        
        THIRD_BUTTON = Button(image=None, pos=(((SCREEN.get_width() / 10) + 10), (SCREEN.get_height() / 10) + 250),
                              text_input="2704 X 1520", font=get_font(15), base_color="White", hovering_color="Green")
        
        FOURTH_BUTTON = Button(image=None, pos=(((SCREEN.get_width() / 10) + 10), (SCREEN.get_height() / 10) + 300),
                              text_input="2560 X 1440", font=get_font(15), base_color="White", hovering_color="Green")
        
        FIFTH_BUTTON = Button(image=None, pos=(((SCREEN.get_width() / 10) + 8), (SCREEN.get_height() / 10) + 350),
                              text_input="1920 X 1080", font=get_font(15), base_color="White", hovering_color="Green")
        
        SIXTH_BUTTON = Button(image=None, pos=(((SCREEN.get_width() / 10)), (SCREEN.get_height() / 10) + 400),
                              text_input="1280 X 720", font=get_font(15), base_color="White", hovering_color="Green")
        
        SEVENTH_BUTTON = Button(image=None, pos=(((SCREEN.get_width() / 10) - 5), (SCREEN.get_height() / 10) + 450),
                              text_input="854 X 480", font=get_font(15), base_color="White", hovering_color="Green")
        
        EIGHT_BUTTON = Button(image=None, pos=(((SCREEN.get_width() / 10) - 5), (SCREEN.get_height() / 10) + 500),
                              text_input="640 X 320", font=get_font(15), base_color="White", hovering_color="Green")
        
        RESOLUTION_BACK = Button(image=None, pos=((SCREEN.get_width() / 10 - 13), (SCREEN.get_height() - 100)),
                              text_input="BACK", font=get_font(15), base_color="White", hovering_color="Green")
        
        for button in (FULLSCREEN_BUTTON, FIRST_BUTTON, SECOND_BUTTON, THIRD_BUTTON, FOURTH_BUTTON, FIFTH_BUTTON, SIXTH_BUTTON, SEVENTH_BUTTON, EIGHT_BUTTON, RESOLUTION_BACK):
            button.changeColor(RESOLUTION_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if FULLSCREEN_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.display.set_mode(((SCREEN.get_width() / 2), (SCREEN.get_height() /2)), pygame.FULLSCREEN)
                if FIRST_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.display.set_mode((7680, 4320), pygame.RESIZABLE)
                if SECOND_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.display.set_mode((3840, 2160), pygame.RESIZABLE)
                if THIRD_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.display.set_mode((2704, 1520), pygame.RESIZABLE)
                if FOURTH_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.display.set_mode((2560, 1440), pygame.RESIZABLE)
                if FIFTH_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
                if SIXTH_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
                if SEVENTH_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.display.set_mode((854, 480), pygame.RESIZABLE)
                if EIGHT_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.display.set_mode((640, 320), pygame.RESIZABLE)
                if RESOLUTION_BACK.checkForInput(RESOLUTION_MOUSE_POS):
                    video_settings()
                
            pygame.display.update()

def video_settings():

    pygame.display.set_caption("Video Settings")

    while True:
    
        VID_SET_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill("Black")
        
        VID_SET_TEXT = get_font(20).render("VIDEO SETTINGS", True, "White")
        VID_SET_RECT = VID_SET_TEXT.get_rect(center=((SCREEN.get_width() / 2), 100))
        SCREEN.blit(VID_SET_TEXT, VID_SET_RECT)

        VID_SET_BACK = Button(image=None, pos=(300, 800),
                              text_input="BACK", font=get_font(20), base_color="White", hovering_color="Green")
        
        RES_BUTTON = Button(image=None, pos=(360, 250),
                              text_input="RESOLUTION", font=get_font(20), base_color="White", hovering_color="Green")
        
        VSYNC_BUTTON = Button(image=None, pos=((SCREEN.get_width() - 400), 300),
                              text_input="0", font=get_font(30), base_color="White", hovering_color="Green")

        for button in (VID_SET_BACK, RES_BUTTON, VSYNC_BUTTON):
            button.changeColor(VID_SET_MOUSE_POS)
            button.update(SCREEN)

        VSYNC_TEXT = get_font(20).render("VSYNC", True, "White")
        VSYNC_RECT = VSYNC_TEXT.get_rect(center=(310, 300))
        SCREEN.blit(VSYNC_TEXT, VSYNC_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VID_SET_BACK.checkForInput(VID_SET_MOUSE_POS):
                    options()
                if RES_BUTTON.checkForInput(VID_SET_MOUSE_POS):
                    resolution()
                if VSYNC_BUTTON.checkForInput(VID_SET_MOUSE_POS):
                    VSYNC_ON = get_font(30).render("Vsync on!", True, "White")
                    VSYNC_ON_RECT = VSYNC_ON.get_rect(center=((SCREEN.get_width() / 2), (SCREEN.get_height() - 200)))
                    SCREEN.blit(VSYNC_ON, VSYNC_ON_RECT)
                    sleep(1)

            pygame.display.update()

def main_menu():
    
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=((SCREEN.get_width() / 2), 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/intro/Play Rect.png"), pos=((SCREEN.get_width() / 2), 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/intro/Options Rect.png"), pos=((SCREEN.get_width() / 2), 400),
                             text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        QUIT_BUTTON = Button(image=pygame.image.load("assets/intro/Quit Rect.png"), pos=((SCREEN.get_width() / 2), 550),
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

def loading_screen():
    pygame.display.set_caption("Loading Screen")

    # Loading BG
    LOADING_BG = pygame.image.load("assets/intro/Loading Bar Background.png")
    LOADING_BG_RECT = LOADING_BG.get_rect(center=((SCREEN.get_width() / 2), 800))

    loading_finished = False

    WIDTH = 10

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        SCREEN.fill("#483C32")

        TEXT = get_font(10).render("MADE BY", True, "White")
        TEXT_RECT = TEXT.get_rect(center=(300, 250))
        SCREEN.blit(TEXT, TEXT_RECT)

        BRAND_LOGO = pygame.image.load("assets/intro/okapjfinish.png")
        SCREEN.blit(BRAND_LOGO, (350, 200))

        LOADING_TEXT = get_font(30).render("LOADING...", True, "White")
        LOADING_TEXT_RECT = LOADING_TEXT.get_rect(center=((300, 800)))
        SCREEN.blit(LOADING_TEXT, LOADING_TEXT_RECT)
        SCREEN.blit(LOADING_BG, LOADING_BG_RECT)

        pygame.draw.rect(SCREEN, "#e84464", ((SCREEN.get_width() / 2 - 365), 735, WIDTH, 130))
            
        while WIDTH < 730:
            WIDTH += 1
            pygame.draw.rect(SCREEN, "#e84464", ((SCREEN.get_width() / 2 - 365), 735, WIDTH, 130))
            sleep(0.0005)
            pygame.display.update()
        
        if WIDTH == 730:
            loading_finished = True
        
        if loading_finished:
            main_menu()

        pygame.display.update()

        

def intro():

    pygame.display.set_caption("Intro")

    while True:

        SCREEN.blit(BG, (0, 0))

        INTRO_MOUSE_POS = pygame.mouse.get_pos()
        
        NEXT_BUTTON = Button(image=None, pos=((SCREEN.get_width() / 2), (SCREEN.get_height() /  2)),
                             text_input="Press HERE to proceed", font=get_font(20), base_color="White", hovering_color="Green")

        NEXT_BUTTON.changeColor(INTRO_MOUSE_POS)
        NEXT_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEXT_BUTTON.checkForInput(INTRO_MOUSE_POS):
                    loading_screen()
        
        pygame.display.update()


intro()
