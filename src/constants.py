import pygame
import math

pygame.init()


class Colors():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    
    BACKGROUND = (255, 112, 205)
    SNAKE = (90, 196, 255)
    FOOD = (200, 0, 200)
    GREENISH = (52, 235, 134)
    
class Fonts():
    STYLE = pygame.font.SysFont(None, 30)
    SCORE_FONT = pygame.font.SysFont("comicsansms", 35)


class Sizes():
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 400
    
    SCORE_DISPLAY_HEIGHT = SCREEN_HEIGHT // 10
    GAME_DISPLAY_HEIGHT = SCREEN_HEIGHT - SCORE_DISPLAY_HEIGHT

    # Attempt at autoscaling
    # SNAKE_BLOCK = math.gcd(SCREEN_WIDTH, SCREEN_HEIGHT) / 10
    SNAKE_BLOCK = 10

SNAKE_SPEED = 15

DIRECTION_VALUES = ['left', 'right', 'up', 'down']
