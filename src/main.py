import pygame
from pygame.locals import *
import numpy as np
from snake import Snake, Player
import time
import random
from constants import Fonts, Colors, Sizes, SNAKE_SPEED, DIRECTION_VALUES
from classic import *
from pvp import *

pygame.init()

# sets display size 
dis = pygame.display.set_mode((Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT))

# shows the screen
pygame.display.update()
pygame.display.set_caption("Intellisnake")

# makes the clock and sets the game
# speed
clock = pygame.time.Clock()

# fonts used for score and the lose
# menu
font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont("comicsansms", 35)

# the part that we actually run.
if __name__ == "__main__":
  pvp_mode()
