import pygame
from constants import Sizes

"""
----- Init File -----
This file handles all initialization and provides handles for important things. 
"""

pygame.init()

window = pygame.display.set_mode((Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT))

score_display = pygame.Surface((Sizes.SCREEN_WIDTH, Sizes.SCORE_DISPLAY_HEIGHT))

game_display = pygame.Surface((Sizes.SCREEN_WIDTH, Sizes.GAME_DISPLAY_HEIGHT))

pygame.display.set_caption("Intellisnake")

clock = pygame.time.Clock()
