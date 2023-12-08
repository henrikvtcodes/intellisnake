import pygame
import pygame_widgets
import logging
from pygame.locals import *
from gamemodes.ai import ai_mode
from gamemodes.classic import classic_mode
from gamemodes.pvp import pvp_mode
from init import GameStateContainer, clock, window
from constants import (
    GameWindowStates,
    GameModes,
    GameEndStates,
    SNAKE_SPEED,
    Colors,
    Loggers,
)
import screens
from ai_algo_legend import generate_next_move

logging.getLogger(Loggers.ALGORITHM.value).setLevel(logging.DEBUG)
logging.getLogger(Loggers.GAME.value).setLevel(logging.DEBUG)

# the part that we actually run.
if __name__ == "__main__":
    pygame.init()

    while GameStateContainer.window_state != GameWindowStates.EXIT:
        events = pygame.event.get()

        if GameStateContainer.window_state == GameWindowStates.START:
            # Render the start screen, and get the widgets that are on it so we can call their listen methods
            widgets = screens.start()

            # Make sure that the buttons on the start screen work properly
            for widget in widgets:
                widget.listen(events)

            # Only start screen uses widgets so we only need to update pygame_widgets when we render the start screen

            pygame_widgets.update(events)

            """ Sleep for 100ms to prevent race condition bug. 
            Thank you Clayton for finding this bug, and stopping my (Henrik) descent into .
            """
            # if first_run:
            # time.sleep(1)

        elif GameStateContainer.window_state == GameWindowStates.PLAYING:
            # If the window state is playing, then start the respective game
            if GameStateContainer.game_mode == GameModes.CLASSIC:
                # TODO: Refactor classic mode to use the state system, as well as Kelsyn's general bugfixes
                classic_mode()
            elif GameStateContainer.game_mode == GameModes.PVP:
                pvp_mode()
            elif GameStateContainer.game_mode == GameModes.AI:
                ai_mode()
        elif GameStateContainer.window_state == GameWindowStates.END:
            window.fill(Colors.BLACK)
            """ If the window state is END, we want to render end screens.
      Worth noting here that as implemented in pvp.py, the window state gets changed to end and we update the game end state, but we don't update the game mode. This allows end screens to know whether to render two scores or one (not yet implemented)
      """
            if GameStateContainer.end_state == GameEndStates.BOTH_LOSE:
                # Render screen for both lose
                screens.both_lose()
            elif GameStateContainer.end_state == GameEndStates.P1_LOSE:
                # Render screen for Player 1 loss
                screens.player1_lose()
            elif GameStateContainer.end_state == GameEndStates.P2_LOSE:
                # Render screen for Player 2 loss
                screens.player2_lose()
            elif GameStateContainer.end_state == GameEndStates.CLASSIC_LOSE:
                screens.classic_lose()
            elif GameStateContainer.end_state == GameEndStates.CLASSIC_WIN:
                screens.classic_win()

            # End Screen Controls
            for event in events:
                if event.type == QUIT:
                    GameStateContainer.window_state = GameWindowStates.EXIT
                    pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        GameStateContainer.window_state = GameWindowStates.START
                        GameStateContainer.game_mode = GameModes.NOT_SELECTED
                        print("RETURNING TO START SCREEN")
                        GameStateContainer.escape_pressed = True
                        first_run = True
                    elif event.key == pygame.K_r:
                        GameStateContainer.window_state = GameWindowStates.PLAYING
                        GameStateContainer.end_state = GameEndStates.PLAYING
                    elif event.key == pygame.K_q:
                        GameStateContainer.window_state = GameWindowStates.EXIT
                        GameStateContainer.game_mode = GameModes.NOT_SELECTED

        # Only main loop events here
        for event in events:
            if event.type == QUIT:
                GameStateContainer.window_state = GameWindowStates.EXIT
                pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    GameStateContainer.window_state = GameWindowStates.EXIT
                if GameStateContainer.window_state == GameWindowStates.START:
                    if event.key == pygame.K_c:
                        GameStateContainer.window_state = GameWindowStates.PLAYING
                        GameStateContainer.game_mode = GameModes.CLASSIC
                    if event.key == pygame.K_p:
                        GameStateContainer.window_state = GameWindowStates.PLAYING
                        GameStateContainer.game_mode = GameModes.PVP

        # Run updates
        pygame.display.update()  # For future perf improvements, we can call this selectively to update only the parts of the screen that have changed
        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit(0)
