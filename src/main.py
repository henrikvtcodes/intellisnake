import pygame
from pygame.locals import *
import numpy as np
from snake import Snake, Player

if __name__ == "__main__":
    # Game Initialization
    pygame.init()
    pygame.display.set_caption('IntelliSnake')
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    player = Player()

    gamer = pygame.image.load("pygame.png").convert()

    # Main Loop
    running = True

    frame_time_delta = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("red")

        screen.fill((0, 0, 0))
        screen.blit(gamer, (player.x, player.y))
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        frame_time_delta = clock.tick(60) / 1000

pygame.quit()
