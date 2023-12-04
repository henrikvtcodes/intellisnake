import pygame
from pygame.locals import *
import numpy as np
from snake import Snake, Player
import time
import random
from constants import Fonts, Colors, Sizes, SNAKE_SPEED, DIRECTION_VALUES
from classic import *
from pvp import *
import init as globals

# the part that we actually run.
if __name__ == "__main__":
  globals.window.blit(globals.score_display, (Sizes.SCORE_DISPLAY_HEIGHT, 0))
  pygame.display.update()
  pvp_mode(game_display=globals.game_display)
