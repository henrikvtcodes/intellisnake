import pygame
import init as globals
from constants import Colors, Sizes, Fonts

# Draws a snake
def draw_snake(snake_size: int, color, snake_list):
  for x in snake_list:
    pygame.draw.rect(globals.window, color, [x[0], x[1], snake_size, snake_size])

# displays the message for the losing screen
def draw_message(msg: str, color: tuple[int, int, int]):
  mesg = Fonts.STYLE.render(msg, True, color)
  globals.window.blit(mesg, [Sizes.SCREEN_WIDTH / 6, Sizes.SCREEN_HEIGHT / 3])
  
  # displays the score. Not currently used in this gamemode.
# Do we want to call it elsewhere so there is a constant score?
def draw_score(score: int): 
  value = Fonts.SCORE_FONT.render("Your Score: " + str(score), True, Colors.GREENISH)