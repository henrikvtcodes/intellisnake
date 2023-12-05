from pygame import Surface
from classic import start_classic
from init import window
from draw_fns import draw_message
from constants import Colors, Fonts, Sizes, TITLE_TEXT
import pygame_widgets as pw
from pygame_widgets.button import Button

from pvp import start_pvp

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
  
  classic_button.draw()
  
  return pvp_button, classic_button
  
def player1_lose(screen: Surface = window):
  draw_message("""Player 2 (Green) snake wins! 
               Press Q (Quit), Esc (Return to start), or R (Replay)""", Colors.GREENISH)

def player2_lose(screen: Surface = window):
  draw_message("""Player 1 (Blue) snake wins! 
               Press Q (Quit), Esc (Return to start), or R (Replay)""", Colors.SNAKE)

def both_lose(screen: Surface = window):
  draw_message("""Both snakes lose! 
               Press Q (Quit), Esc (Return to start), or R (Replay)""", Colors.RED)
  