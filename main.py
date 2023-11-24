import pygame, sys, threading
from button import Button
from time import sleep

pygame.init()

SCREEN = pygame.display.set_mode((1680, 990), pygame.RESIZABLE)
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/intro/BG.jpeg")
pygame.transform.scale(SCREEN, (SCREEN.get_width(), SCREEN.get_height()))

def get_font(size):
    return pygame.font.Font("assets/intro/font.ttf", size)

def options():

    pygame.display.set_caption("Options")

    while True:

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=((SCREEN.get_width() / 2), SCREEN.get_height() / 10))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(SCREEN.get_width() / 10 + 100, SCREEN.get_height() / 10 + 400), 
                            text_input="BACK", font=get_font(20), base_color="White", hovering_color="Green")

        VIDEOSETTINGS_BUTTON = Button(image=None, pos=(SCREEN.get_width() / 10 + 200, SCREEN.get_height() / 10 + 100),
                             text_input="VIDEO SETTINGS", font=get_font(20), base_color="White", hovering_color="Green")
        
        CONTROLS_BUTTON = Button(image=None, pos=(SCREEN.get_width() / 10 + 140, SCREEN.get_height() / 10 + 150),
                                   text_input="CONTROLS", font=get_font(20), base_color="White", hovering_color="Green")
        
        AUDIOSETTINGS_BUTTON = Button(image=None, pos=(SCREEN.get_width() / 10 + 200, SCREEN.get_height() / 10 + 200),
                                   text_input="AUDIO SETTINGS", font=get_font(20), base_color="White", hovering_color="Green")
        
        main_menu_sfx = pygame.mixer.Sound("assets/intro/sounds/main menu.wav")
        main_menu_sfx.play()
        main_menu_sfx.set_volume(0.5)
        
        for button in (VIDEOSETTINGS_BUTTON, OPTIONS_BACK, CONTROLS_BUTTON, AUDIOSETTINGS_BUTTON):
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    main_menu()
                if VIDEOSETTINGS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    video_settings()
                if CONTROLS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    controls()
                if AUDIOSETTINGS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    audio_settings()

        pygame.display.update()

def main_menu_sound():

    pygame.display.set_caption("Main Menu Sound")
    pygame.mixer.init()

    while True:

        MAIN_MENU_SOUND_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        MAIN_MENU_SOUND_TEXT = get_font(20).render("MAIN MENU SOUND", True, "White")
        MAIN_MENU_SOUND_RECT = MAIN_MENU_SOUND_TEXT.get_rect(center=(SCREEN.get_width() / 2, SCREEN.get_height() / 10))
        SCREEN.blit(MAIN_MENU_SOUND_TEXT, MAIN_MENU_SOUND_RECT)

        LOUDEST_BUTTON = Button(image=None, pos=((SCREEN.get_width() / 2), SCREEN.get_height() / 10 + 100),
                                text_input="1", font=get_font(15), base_color="White", hovering_color="Green")
        
        FIRST_BUTTON = Button(image=None, pos=((SCREEN.get_width() / 2), SCREEN.get_height() / 10 + 150),
                                text_input="0.9", font=get_font(15), base_color="White", hovering_color="Green")
        
        SECOND_BUTTON = Button(image=None, pos=((SCREEN.get_width() / 2), SCREEN.get_height() / 10 + 200),
                                text_input="0.8", font=get_font(15), base_color="White", hovering_color="Green")
        
        THIRD_BUTTON = Button(image=None, pos=((SCREEN.get_width() / 2), SCREEN.get_height() / 10 + 250),
                                text_input="0.7", font=get_font(15), base_color="White", hovering_color="Green")
        
        FOURTH_BUTTON = Button(image=None, pos=((SCREEN.get_width() / 2), SCREEN.get_height() / 10 + 300),
                                text_input="0.6", font=get_font(15), base_color="White", hovering_color="Green")
        
        FIFTH_BUTTON = Button(image=None, pos=((SCREEN.get_width() / 2), SCREEN.get_height() / 10 + 350),
                                text_input="0.5", font=get_font(15), base_color="White", hovering_color="Green")
        
        SIXTH_BUTTON = Button(image=None, pos=((SCREEN.get_width() / 2), SCREEN.get_height() / 10 + 400),
                                text_input="0.4", font=get_font(15), base_color="White", hovering_color="Green")
        
        SEVENTH_BUTTON = Button(image=None, pos=((SCREEN.get_width() / 2), SCREEN.get_height() / 10 + 450),
                                text_input="0.3", font=get_font(15), base_color="White", hovering_color="Green")
        
        EIGHTH_BUTTON = Button(image=None, pos=((SCREEN.get_width() / 2), SCREEN.get_height() / 10 + 500),
                                text_input="0.2", font=get_font(15), base_color="White", hovering_color="Green")
        
        NINTH_BUTTON = Button(image=None, pos=((SCREEN.get_width() / 2), SCREEN.get_height() / 10 + 550),
                                text_input="0.1", font=get_font(15), base_color="White", hovering_color="Green")
        
        NO_SOUND = Button(image=None, pos=((SCREEN.get_width() / 2), SCREEN.get_height() / 10 + 600),
                                text_input="0.0", font=get_font(15), base_color="White", hovering_color="Green")
        
        MAIN_MENU_SOUND_BACK = Button(image=None, pos=(SCREEN.get_width() / 10 + 100, SCREEN.get_height() / - 100),
                                      text_input="BACK", font=get_font(15), base_color="White", hovering_color="Green")
        
        for button in (LOUDEST_BUTTON, FIRST_BUTTON, SECOND_BUTTON, THIRD_BUTTON, FOURTH_BUTTON, FIFTH_BUTTON, SIXTH_BUTTON, SEVENTH_BUTTON, EIGHTH_BUTTON, NINTH_BUTTON, NO_SOUND):
            button.changeColor(MAIN_MENU_SOUND_MOUSE_POS)
            button.update(SCREEN)

        main_menu_sfx = pygame.mixer.Sound("assets/intro/sounds/main menu.wav")
        main_menu_sfx.play()
        main_menu_sfx.set_volume(0.5)

        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event == pygame.MOUSEBUTTONDOWN:
                if MAIN_MENU_SOUND_BACK.checkForInput(MAIN_MENU_SOUND_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    audio_settings()
                if LOUDEST_BUTTON.checkForInput(MAIN_MENU_SOUND_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.mixer.Channel(0).set_volume(1.0)
                if FIRST_BUTTON.checkForInput(MAIN_MENU_SOUND_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.mixer.Channel(0).set_volume(0.9)
                if SECOND_BUTTON.checkForInput(MAIN_MENU_SOUND_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.mixer.Channel(0).set_volume(0.8)
                if THIRD_BUTTON.checkForInput(MAIN_MENU_SOUND_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.mixer.Channel(0).set_volume(0.7)
                if FOURTH_BUTTON.checkForInput(MAIN_MENU_SOUND_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.mixer.Channel(0).set_volume(0.6)
                if FIFTH_BUTTON.checkForInput(MAIN_MENU_SOUND_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.mixer.Channel(0).set_volume(0.5)
                if SIXTH_BUTTON.checkForInput(MAIN_MENU_SOUND_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.mixer.Channel(0).set_volume(0.4)
                if SEVENTH_BUTTON.checkForInput(MAIN_MENU_SOUND_RECT):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.mixer.Channel(0).set_volume(0.3)
                if EIGHTH_BUTTON.checkForInput(MAIN_MENU_SOUND_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.mixer.Channel(0).set_volume(0.2)
                if NINTH_BUTTON.checkForInput(MAIN_MENU_SOUND_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.mixer.Channel(0).set_volume(0.1)
                if NO_SOUND.checkForInput(MAIN_MENU_SOUND_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.mixer.Channel(0).set_volume(0.0)
    
        pygame.display.update()

def audio_settings():

    pygame.display.set_caption("Audio Settings")
    pygame.mixer.init()

    while True:
    
        AUD_SET_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.blit(BG, (0, 0))
        
        AUD_SET_TEXT = get_font(20).render("AUDIO SETTINGS", True, "White")
        AUD_SET_RECT = AUD_SET_TEXT.get_rect(center=((SCREEN.get_width() / 2), SCREEN.get_height() / 10))
        SCREEN.blit(AUD_SET_TEXT, AUD_SET_RECT)

        AUD_SET_BACK = Button(image=None, pos=(SCREEN.get_width() / 10 + 100, SCREEN.get_height() / 10 + 400),
                              text_input="BACK", font=get_font(20), base_color="White", hovering_color="Green")

        MAIN_MENU_SFX_BUTTON = Button(image=None, pos=((SCREEN.get_width() / 10 + 200), SCREEN.get_height() / 10 + 100), 
                            text_input="Main Menu Sound", font=get_font(20), base_color="White", hovering_color="Green")
        
        for button in (AUD_SET_BACK, MAIN_MENU_SFX_BUTTON):
            button.changeColor(AUD_SET_MOUSE_POS)
            button.update(SCREEN)

        main_menu_sfx = pygame.mixer.Sound("assets/intro/sounds/main menu.wav")
        main_menu_sfx.play()
        main_menu_sfx.set_volume(0.5)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AUD_SET_BACK.checkForInput(AUD_SET_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    options()
                if MAIN_MENU_SFX_BUTTON.checkForInput(AUD_SET_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    main_menu_sound()

        pygame.display.update()

def controls():

    pygame.display.set_caption("Controls")
    pygame.mixer.init()

    while True:

        CONTROLS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        CONTROLS_TEXT = get_font(20).render("CONTROLS", True, "White")
        CONTROLS_RECT = CONTROLS_TEXT.get_rect(center=((SCREEN.get_width() / 2), SCREEN.get_height() / 10))
        SCREEN.blit(CONTROLS_TEXT, CONTROLS_RECT)

        MOVE_UP_TEXT = get_font(15).render("MOVE UP", True, "White")
        MOVE_UP_RECT = MOVE_UP_TEXT.get_rect(center=((SCREEN.get_width() / 10) + 114,(SCREEN.get_height() / 10 + 100))) 
        SCREEN.blit(MOVE_UP_TEXT, MOVE_UP_RECT)

        MOVE_DOWN_TEXT = get_font(15).render("MOVE DOWN", True, "White")
        MOVE_DOWN_RECT = MOVE_DOWN_TEXT.get_rect(center=((SCREEN.get_width() / 10) + 127,(SCREEN.get_height() / 10 + 150)))
        SCREEN.blit(MOVE_DOWN_TEXT, MOVE_DOWN_RECT)

        MOVE_LEFT_TEXT = get_font(15).render("MOVE LEFT", True, "White")
        MOVE_LEFT_RECT = MOVE_LEFT_TEXT.get_rect(center=((SCREEN.get_width() / 10) + 127,(SCREEN.get_height() / 10 + 200)))
        SCREEN.blit(MOVE_LEFT_TEXT, MOVE_LEFT_RECT)

        MOVE_RIGHT_TEXT = get_font(15).render("MOVE RIGHT", True, "White")
        MOVE_RIGHT_RECT = MOVE_RIGHT_TEXT.get_rect(center=((SCREEN.get_width() / 10) + 135,(SCREEN.get_height() / 10 + 250)))
        SCREEN.blit(MOVE_RIGHT_TEXT, MOVE_RIGHT_RECT)

        HIT_TEXT = get_font(15).render("HIT", True, "White")
        HIT_RECT = HIT_TEXT.get_rect(center=((SCREEN.get_width() / 10) + 82, (SCREEN.get_height() / 10 + 300)))
        SCREEN.blit(HIT_TEXT, HIT_RECT)

        CONTROLS_BACK = Button(image=None, pos=(SCREEN.get_width() / 10 + 100, SCREEN.get_height() / 10 + 400),
                               text_input="BACK", font=get_font(20), base_color="White", hovering_color="Green")
        
        CONTROLS_BACK.changeColor(CONTROLS_MOUSE_POS)
        CONTROLS_BACK.update(SCREEN)

        main_menu_sfx = pygame.mixer.Sound("assets/intro/sounds/main menu.wav")
        main_menu_sfx.play()
        main_menu_sfx.set_volume(0.5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTROLS_BACK.checkForInput(CONTROLS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    options()

        pygame.display.update()

def resolution():

    pygame.display.set_caption("Resolution")
    pygame.mixer.init()

    while True:

        SCREEN.blit(BG, (0, 0))

        RESOLUTION_MOUSE_POS = pygame.mouse.get_pos()

        RESOLUTION_TEXT = get_font(20).render("RESOLUTION", True, "White")
        RESOLUTION_RECT = RESOLUTION_TEXT.get_rect(center=((SCREEN.get_width() / 2), SCREEN.get_height() / 10))
        SCREEN.blit(RESOLUTION_TEXT, RESOLUTION_RECT)

        FULLSCREEN_BUTTON = Button(image=None, pos=(((SCREEN.get_width() / 2)), (SCREEN.get_height() / 10) + 100),
                              text_input="FULLSCREEN", font=get_font(15), base_color="White", hovering_color="Green")
        
        FIRST_BUTTON = Button(image=None, pos=((SCREEN.get_width() / 2), (SCREEN.get_height() / 10) + 150),
                              text_input="7680 X 4320", font=get_font(15), base_color="White", hovering_color="Green")
        
        SECOND_BUTTON = Button(image=None, pos=(((SCREEN.get_width() / 2)), (SCREEN.get_height() / 10) + 200),
                              text_input="3840 X 2160", font=get_font(15), base_color="White", hovering_color="Green")
        
        THIRD_BUTTON = Button(image=None, pos=(((SCREEN.get_width() / 2)), (SCREEN.get_height() / 10) + 250),
                              text_input="2704 X 1520", font=get_font(15), base_color="White", hovering_color="Green")
        
        FOURTH_BUTTON = Button(image=None, pos=(((SCREEN.get_width() / 2)), (SCREEN.get_height() / 10) + 300),
                              text_input="2560 X 1440", font=get_font(15), base_color="White", hovering_color="Green")
        
        FIFTH_BUTTON = Button(image=None, pos=(((SCREEN.get_width() / 2)), (SCREEN.get_height() / 10) + 350),
                              text_input="1920 X 1080", font=get_font(15), base_color="White", hovering_color="Green")
        
        SIXTH_BUTTON = Button(image=None, pos=(((SCREEN.get_width() / 2)), (SCREEN.get_height() / 10) + 400),
                              text_input="1280 X 720", font=get_font(15), base_color="White", hovering_color="Green")
        
        SEVENTH_BUTTON = Button(image=None, pos=(((SCREEN.get_width() / 2)), (SCREEN.get_height() / 10) + 450),
                              text_input="854 X 480", font=get_font(15), base_color="White", hovering_color="Green")
        
        EIGHT_BUTTON = Button(image=None, pos=(((SCREEN.get_width() / 2)), (SCREEN.get_height() / 10) + 500),
                              text_input="640 X 320", font=get_font(15), base_color="White", hovering_color="Green")
        
        RESOLUTION_BACK = Button(image=None, pos=((SCREEN.get_width() / 10 + 100), (SCREEN.get_height() - 100)),
                              text_input="BACK", font=get_font(15), base_color="White", hovering_color="Green")
        
        main_menu_sfx = pygame.mixer.Sound("assets/intro/sounds/main menu.wav")
        main_menu_sfx.play()
        main_menu_sfx.set_volume(0.5)
        
        for button in (FULLSCREEN_BUTTON, FIRST_BUTTON, SECOND_BUTTON, THIRD_BUTTON, FOURTH_BUTTON, FIFTH_BUTTON, SIXTH_BUTTON, SEVENTH_BUTTON, EIGHT_BUTTON, RESOLUTION_BACK):
            button.changeColor(RESOLUTION_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if FULLSCREEN_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.display.set_mode((SCREEN.get_width(), SCREEN.get_height()), pygame.FULLSCREEN)
                if FIRST_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.display.set_mode((7680, 4320), pygame.RESIZABLE)
                if SECOND_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.display.set_mode((3840, 2160), pygame.RESIZABLE)
                if THIRD_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.display.set_mode((2704, 1520), pygame.RESIZABLE)
                if FOURTH_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.display.set_mode((2560, 1440), pygame.RESIZABLE)
                if FIFTH_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
                if SIXTH_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
                if SEVENTH_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.display.set_mode((854, 480), pygame.RESIZABLE)
                if EIGHT_BUTTON.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    pygame.display.set_mode((640, 320), pygame.RESIZABLE)
                if RESOLUTION_BACK.checkForInput(RESOLUTION_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    video_settings()
                
            pygame.display.update()

def video_settings():

    pygame.display.set_caption("Video Settings")
    pygame.mixer.init()

    while True:
    
        VID_SET_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.blit(BG, (0, 0))
        
        VID_SET_TEXT = get_font(20).render("VIDEO SETTINGS", True, "White")
        VID_SET_RECT = VID_SET_TEXT.get_rect(center=((SCREEN.get_width() / 2), SCREEN.get_height() / 10))
        SCREEN.blit(VID_SET_TEXT, VID_SET_RECT)

        VID_SET_BACK = Button(image=None, pos=((SCREEN.get_width() / 10) + 100, (SCREEN.get_height() / 10 + 400)),
                              text_input="BACK", font=get_font(20), base_color="White", hovering_color="Green")
        
        RES_BUTTON = Button(image=None, pos=(SCREEN.get_width() / 10 + 160, SCREEN.get_height() / 10 + 200),
                              text_input="RESOLUTION", font=get_font(20), base_color="White", hovering_color="Green")
        
        VSYNC_BUTTON = Button(image=None, pos=((SCREEN.get_width() - 300), SCREEN.get_height() / 10 + 250),
                              text_input="0", font=get_font(30), base_color="White", hovering_color="Green")

        for button in (VID_SET_BACK, RES_BUTTON, VSYNC_BUTTON):
            button.changeColor(VID_SET_MOUSE_POS)
            button.update(SCREEN)

        VSYNC_TEXT = get_font(20).render("VSYNC", True, "White")
        VSYNC_RECT = VSYNC_TEXT.get_rect(center=(SCREEN.get_width() / 10 + 110, SCREEN.get_width() / 10 + 170))
        SCREEN.blit(VSYNC_TEXT, VSYNC_RECT)

        main_menu_sfx = pygame.mixer.Sound("assets/intro/sounds/main menu.wav")
        main_menu_sfx.play()
        main_menu_sfx.set_volume(0.5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VID_SET_BACK.checkForInput(VID_SET_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    options()
                if RES_BUTTON.checkForInput(VID_SET_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    resolution()
                if VSYNC_BUTTON.checkForInput(VID_SET_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    VSYNC_ON = get_font(30).render("Vsync on!", True, "White")
                    VSYNC_ON_RECT = VSYNC_ON.get_rect(center=((SCREEN.get_width() / 2), (SCREEN.get_height() - 200)))
                    SCREEN.blit(VSYNC_ON, VSYNC_ON_RECT)
                    sleep(1)

            pygame.display.update()

def main_menu():
    
    pygame.display.set_caption("Menu")
    pygame.mixer.init()

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

        main_menu_sfx = pygame.mixer.Sound("assets/intro/sounds/main menu.wav")
        main_menu_sfx.play()
        main_menu_sfx.set_volume(0.5)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/intro/sounds/button click.mp3"))
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

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
                    BUTTON_CLICK = pygame.mixer.Sound("assets/intro/sounds/button click.mp3")
                    BUTTON_CLICK.play()
                    loading_screen()
        
        pygame.display.update()


intro()