import pygame
import pygame_widgets
from pygame.locals import *
from classic import classic_mode
from pvp import pvp_mode
from init import GameStateContainer, clock
from constants import GameWindowStates, GameModes, GameEndStates, SNAKE_SPEED, Colors
import screens

# the part that we actually run.
if __name__ == "__main__":
  while GameStateContainer.window_state != GameWindowStates.EXIT:
    
    events = pygame.event.get()

    if GameStateContainer.window_state == GameWindowStates.START:
      widgets = screens.start()
      
      for widget in widgets:
        widget.listen(events)
        
    elif GameStateContainer.window_state == GameWindowStates.PLAYING:
      if GameStateContainer.game_mode == GameModes.CLASSIC:
        classic_mode()
      elif GameStateContainer.game_mode == GameModes.PVP:
        pvp_mode()
    elif GameStateContainer.window_state == GameWindowStates.END:
      if GameStateContainer.end_state == GameEndStates.BOTH_LOSE:
        # Render screen for both lose
        screens.both_lose()
      elif GameStateContainer.end_state == GameEndStates.P1_LOSE:
        # Render screen for Player 1 loss
        screens.player1_lose()
      elif GameStateContainer.end_state == GameEndStates.P2_LOSE:
        # Render screen for Player 2 loss
        screens.player2_lose()
    
        
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
    pygame_widgets.update(events)
    pygame.display.update()
    clock.tick(SNAKE_SPEED)
  
  pygame.quit()
  quit(0)
