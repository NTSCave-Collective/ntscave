import pygame
import player

def render_frame(window, state):
    # Drawing current frame
    player.drawCircle(window, state)
    # if state.down:
    #     state.y += 1
    # if state.up:
    #     state.y -= 1
    # if state.left:
    #     state.x -= 1
    # if state.right:
    #     state.x += 1
    pygame.display.flip()

def clear_surface(window):
    window.fill([255,255,255])