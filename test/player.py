import pygame

def player_events(state):
    keys = pygame.key.get_pressed()

    def movement():
        if keys[pygame.K_RIGHT]:
            state.x -= state.vel
        if keys[pygame.K_LEFT]:
            state.x += state.vel
        if keys[pygame.K_DOWN]:
            state.y -= state.vel
        if keys[pygame.K_UP]:
            state.y += state.vel

    movement()
