from typing import Literal
import pygame
import math
from enum import Enum
import pygame_widgets

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
    SCORE_FONT = pygame.font.SysFont("comicsansms", 36)

TITLE_TEXT = Fonts.SCORE_FONT.render("Intellisnake", True, Colors.WHITE)

class Sizes():
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    
    SCORE_DISPLAY_HEIGHT = SCREEN_HEIGHT // 10
    GAME_DISPLAY_HEIGHT = SCREEN_HEIGHT - SCORE_DISPLAY_HEIGHT

    # Attempt at autoscaling
    # SNAKE_BLOCK = math.gcd(SCREEN_WIDTH, SCREEN_HEIGHT) / 10
    SNAKE_BLOCK = 10

SNAKE_SPEED = 15

DIRECTION_VALUES = ['left', 'right', 'up', 'down']

class GameWindowStates(Enum):
    START = 0
    PLAYING = 1
    END = 2
    EXIT = 3

class GameEndStates(Enum):
    PLAYING = -1
    BOTH_LOSE = 0
    P1_LOSE = 1
    P2_LOSE = 2
    P1_WIN = 3
    P2_WIN = 4
    

class GameModes(Enum):
    NOT_SELECTED = -1
    CLASSIC = 0
    PVP = 1
    AI = 2
