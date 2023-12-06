from pygame import Surface
from gamemodes.ai import start_ai
from init import window
from draw_fns import draw_message
from constants import Colors, TITLE_TEXT
from pygame_widgets.button import Button

from gamemodes.pvp import start_pvp
from gamemodes.classic import start_classic

def score(screen: Surface, score: int):
  raise NotImplementedError()

def start(screen: Surface = window):
  width = screen.get_width()
  height = screen.get_height()
  # blit title text centered horizontally and at the top of the screen
  screen.blit(TITLE_TEXT, ((width - TITLE_TEXT.get_width()) / 2, 10))
  
  pvp_button = Button(
    screen,
    ((width - 100) / 2), TITLE_TEXT.get_height() + 20, 100, 48,
    text='PVP',
    fontSize=24,
    margin=5,
    radius=5,
    onClick=lambda: start_pvp()
  )
  
  pvp_button.draw()
  
  classic_button = Button(
    screen,
    ((width - 100) / 2), TITLE_TEXT.get_height() + 100, 100, 48,
    text='Classic',
    fontSize=24,
    margin=5,
    radius=5,
    onClick=lambda: start_classic()
  )
  
  ai_button = Button(
    screen,
    ((width - 100) / 2), TITLE_TEXT.get_height() + 220, 100, 48,
    text='AI Mode',
    fontSize=24,
    margin=5,
    radius=5,
    onClick=lambda: start_ai()
  )
  
  classic_button.draw()
  
  return pvp_button, classic_button, ai_button

option_message = """Press Q (Quit), Esc (Return to start), or R (Replay)"""
  
def player1_lose(screen: Surface = window):
  draw_message(f"""Player 2 (Green) snake wins! {option_message}""", Colors.GREENISH)

def player2_lose(screen: Surface = window):
  draw_message(f"""Player 1 (Blue) snake wins! {option_message} """, Colors.SNAKE)

def both_lose(screen: Surface = window):
  draw_message(f"""Both snakes lose! {option_message}""", Colors.RED)
  