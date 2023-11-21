import pygame
import CONSTANTS

def render_frame(window, state):
    draw_circle(window, state)

def draw_circle(window, state):
    # Calculate the camera offset to keep the ball in the center
    camera_x = CONSTANTS.SCREEN_SIZE[0] // 2 - state.x
    camera_y = CONSTANTS.SCREEN_SIZE[1] // 2 - state.y
    pygame.draw.circle(window, CONSTANTS.COLOR_BALL, [CONSTANTS.PLAYER_START_X_POSITION, CONSTANTS.PLAYER_START_X_POSITION], CONSTANTS.RADIUS_BALL)