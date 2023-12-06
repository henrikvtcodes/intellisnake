import pygame
from enum import Enum

pygame.init()


class Colors():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    
    BACKGROUND = (255, 112, 205)
    BACKGROUND_SQUARES = (255, 135, 213)
    SNAKE = (90, 196, 255)
    PURPLY = (200, 0, 200)
    GREENISH = (52, 235, 134)
    PEACHY = (255, 154, 107)
    YELLOWY = (255, 251, 130)
    

    
class Fonts():
    STYLE = pygame.font.SysFont(None, 30)
    SCORE_FONT = pygame.font.SysFont("comicsansms", 36)

# Global title text object
TITLE_TEXT = Fonts.SCORE_FONT.render("Intellisnake", True, Colors.WHITE)

class Sizes():
    """ This class contains all the dimensions for the game."""
    SCREEN_WIDTH = 1000
    """ DO NOT CHANGE SCREEN WIDTH, GAME WILL BREAK. """
    SCREEN_HEIGHT = 600
    """ DO NOT CHANGE SCREEN HEIGHT, GAME WILL BREAK. """
    
    SCORE_DISPLAY_HEIGHT = SCREEN_HEIGHT // 10
    GAME_DISPLAY_HEIGHT = SCREEN_HEIGHT - SCORE_DISPLAY_HEIGHT

    # Attempt at autoscaling
    # SNAKE_BLOCK = math.gcd(SCREEN_WIDTH, SCREEN_HEIGHT) / 10
    SNAKE_BLOCK = 40

SNAKE_SPEED = 7

class SnakeDirections(Enum):
    """ This enum is used to determine which direction the snake is moving in. """
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"

MAX_SCORE = (Sizes.SCREEN_HEIGHT // Sizes.SNAKE_BLOCK) * (Sizes.SCREEN_WIDTH // Sizes.SNAKE_BLOCK)

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


for i in SnakeDirections:
    print(i)