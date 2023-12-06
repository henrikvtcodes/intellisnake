import pygame
import init as globals
from constants import Colors, Sizes, Fonts
from images import *


# Draws a snake
def draw_snake(snake_size: int, color, snake_list, direction, snake_length):
  if color == Colors.SNAKE:
    body = snake_body_blue
    head = snake_head_blue
    tail = snake_tail_blue
  else:
    body = snake_body_green
    head = snake_head_green
    tail = snake_tail_green

  if direction == 'up':
    head = pygame.transform.rotate(head, 90)
  elif direction == 'down':
    head = pygame.transform.rotate(head, 270)
  elif direction == 'left':
    head = pygame.transform.rotate(head, 180)

  f = 1
  for x in snake_list:
    # pygame.draw.rect(globals.window, color, [x[0], x[1], snake_size, snake_size])
    if f == snake_length:
      globals.window.blit(head, (x[0], x[1]))
    else:
      globals.window.blit(body, (x[0], x[1]))
    f += 1
    

# displays the message for the losing screen
def draw_message(msg: str, color: tuple[int, int, int]):
  mesg = Fonts.STYLE.render(msg, True, color)
  # centers the message
  width = globals.window.get_width()
  height = globals.window.get_height()
  globals.window.blit(mesg, ((width - mesg.get_width()) / 2, (height - mesg.get_height()) / 2))
  
  # displays the score. Not currently used in this gamemode.
# Do we want to call it elsewhere so there is a constant score?
def draw_score(score: int): 
  value = Fonts.SCORE_FONT.render("Your Score: " + str(score), True, Colors.GREENISH)