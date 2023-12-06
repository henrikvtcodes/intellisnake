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

# Global title text object
TITLE_TEXT = Fonts.SCORE_FONT.render("Intellisnake", True, Colors.WHITE)


class Sizes():
    """ This class contains all the dimensions for the game."""
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    """ Screen Sizes (width,height): (640, 480), (800, 600), (1024, 768), (1280, 720)"""
    
    SCORE_DISPLAY_HEIGHT = SCREEN_HEIGHT // 10
    GAME_DISPLAY_HEIGHT = SCREEN_HEIGHT - SCORE_DISPLAY_HEIGHT

    # Attempt at autoscaling
    SNAKE_BLOCK = math.gcd(SCREEN_WIDTH, SCREEN_HEIGHT) / 10
    # SNAKE_BLOCK = 10

SNAKE_SPEED = 15

DIRECTION_VALUES = ['left', 'right', 'up', 'down']

class GameWindowStates(Enum):
    """ Represents the different screens that take up the entire main window. """
    START = 0
    PLAYING = 1
    END = 2
    EXIT = 3

class GameEndStates(Enum):
    """ This enum is used to determine which end screen to render when the game window state is END."""
    PLAYING = -1
    BOTH_LOSE = 0
    P1_LOSE = 1
    P2_LOSE = 2
    P1_WIN = 3
    P2_WIN = 4
    

class GameModes(Enum):
    """ When the game window state is PLAYING, this enum is used to determine which game mode to run. """
    NOT_SELECTED = -1
    CLASSIC = 0
    PVP = 1
    AI = 2
