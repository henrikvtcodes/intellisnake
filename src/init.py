import pygame
from constants import Sizes, GameWindowStates, GameModes, GameEndStates

"""
----- Init File -----
This file handles all initialization and provides handles for important things. 
All other code must reference the handles provided here to access the main window, subsurfaces, game state, and clock.
"""

pygame.init()

window = pygame.display.set_mode((Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT))

# Subsurfaces for the game display and the score display
score_display = pygame.Surface((Sizes.SCREEN_WIDTH, Sizes.SCORE_DISPLAY_HEIGHT))

game_display = pygame.Surface((Sizes.SCREEN_WIDTH, Sizes.GAME_DISPLAY_HEIGHT))

pygame.display.set_caption("Intellisnake")

pygame.display.update()


class GameStateContainer():
    """ This is a global class that can be referenced anywhere to make all requisite information available."""
    window_state: GameWindowStates = GameWindowStates.START
    game_mode: GameModes = GameModes.NOT_SELECTED
    end_state: GameEndStates = GameEndStates.PLAYING

clock = pygame.time.Clock()
