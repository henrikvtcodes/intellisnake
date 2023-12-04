import pygame
from pygame.locals import *
import numpy as np
from snake import Snake, Player
import time
import random
from constants import Fonts, Colors, Sizes, SNAKE_SPEED, DIRECTION_VALUES



# Displays the score. Not currently used in this gamemode.
# Do we want to call it elsewhere so there is a constant score?
def your_score(score: int): 
  value = Fonts.SCORE_FONT.render("Your Score: " + str(score), True, Colors.GREENISH)
  dis.blit(value, [0, 0])

# Draws a snake
def draw_snake(snake_size: int, color, snake_list):
  for x in snake_list:
    pygame.draw.rect(dis, color, [x[0], x[1], snake_size, snake_size])

# displays the message for the losing screen
def message(msg: str, color: tuple[int, int, int]):
  mesg = Fonts.STYLE.render(msg, True, color)
  dis.blit(mesg, [Sizes.SCREEN_WIDTH / 6, Sizes.SCREEN_HEIGHT / 3])

# loop for playing pvp mode
def pvp_mode():
  game_over = False
  game_close = False
  blue_lose = False
  green_lose = False
  both_lose = False
  
  # Generates starting position of both 
  # snakes.
  snake_x1 = Sizes.SCREEN_WIDTH / 2
  snake_y1 = Sizes.SCREEN_HEIGHT / 2
  snake_x2 = Sizes.SCREEN_WIDTH / 2 - 2 * Sizes.SNAKE_BLOCK
  snake_y2 = Sizes.SCREEN_HEIGHT / 2

  snake_x1 -= snake_x1 % Sizes.SNAKE_BLOCK
  snake_y1 -= snake_y1 % Sizes.SNAKE_BLOCK
  snake_x2 -= snake_x2 % Sizes.SNAKE_BLOCK
  snake_y2 -= snake_y2 % Sizes.SNAKE_BLOCK

  # This is what decides how far the snakes 
  # move.
  x1_change = 0
  y1_change = 0
  x2_change = 0
  y2_change = 0

  snake_list_1 = []
  snake_length_1 = 1
  snake_list_2 = []
  snake_length_2 = 1

  # generates a starting apple position.
  food_x = random.randint(0, Sizes.SCREEN_WIDTH)
  food_y = random.randint(0, Sizes.SCREEN_HEIGHT)
  food_x = food_x - food_x % Sizes.SNAKE_BLOCK
  food_y = food_y - food_y % Sizes.SNAKE_BLOCK

  # continues as long as the game isn't over.
  # yeah.
  while not game_over:

    # after receiving the lose condition
    # this occurs, prompting whether or not
    # the player wants to go again.
    # We could add a high score save thing 
    # and/or a main menu option to choose a
    # new gamemode.
    while game_close == True:
      dis.fill(Colors.FOOD)
      if both_lose:
        if snake_length_1 > snake_length_2:
          message("Blue was longer, blue wins! Press Q-Quit or C-Play again", Colors.SNAKE)
        elif snake_length_2 > snake_length_1:
          message("Green was longer, green wins! Press Q-Quit or C-Play again", Colors.GREENISH)
        else:
          message("You both lose! Press Q-Quit or C-Play again", Colors.RED)
      elif blue_lose == True:
        message("Green snake wins! Press Q-Quit or C-Play again", Colors.GREENISH)
      elif green_lose == True:
        message("Blue snake wins! Press Q-Quit or C-Play again", Colors.SNAKE)
      else:
        dis.fill(Colors.BLACK)
        message("Something went wrong! Press Q-Quit or C-Play again", Colors.RED)
      
      pygame.display.update()

      #waits for the user to pick an option
      for event in pygame.event.get():

        if event.type == pygame.QUIT:
          game_over = True
          game_close = False

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            game_close = False
            game_over = True
          if event.key == pygame.K_c:
            pvp_mode()

    # if the user clicks or presses a key
    # that does something, that is read here.
    # If they quit, it ends the program, if they
    # hit one of the arrow or wasd keys it sets the
    # direction change.
    # player one or blue snake is arrows, player
    # 2 or green snake is wasd.
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        game_over = True
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          x1_change = -Sizes.SNAKE_BLOCK
          y1_change = 0
        if event.key == pygame.K_RIGHT:
          x1_change = Sizes.SNAKE_BLOCK
          y1_change = 0
        if event.key == pygame.K_UP:
          x1_change = 0
          y1_change = -Sizes.SNAKE_BLOCK
        if event.key == pygame.K_DOWN:
          x1_change = 0
          y1_change = Sizes.SNAKE_BLOCK
        if event.key == pygame.K_a:
          x2_change = -Sizes.SNAKE_BLOCK
          y2_change = 0
        if event.key == pygame.K_d:
          x2_change = Sizes.SNAKE_BLOCK
          y2_change = 0
        if event.key == pygame.K_w:
          x2_change = 0
          y2_change = -Sizes.SNAKE_BLOCK
        if event.key == pygame.K_s:
          x2_change = 0
          y2_change = Sizes.SNAKE_BLOCK
    
    # checks if the p1 snake is out of bounds. 
    # assigns win to green if true.
    if snake_x1 == Sizes.SCREEN_WIDTH or snake_x1 < 0 or snake_y1 == Sizes.SCREEN_HEIGHT or snake_y1 < 0:
      print("Out of bounds")
      game_close = True
      blue_lose = True

    # checks if the p2 snake is out of bounds.
    # removes win from p1 if both are true, gives
    # win to p2 if only this is true. 
    if snake_x2 == Sizes.SCREEN_WIDTH or snake_x2 < 0 or snake_y2 == Sizes.SCREEN_HEIGHT or snake_y2 < 0:
      print(snake_x2, snake_y2)
      game_close = True
      if blue_lose == True:
        both_lose = True
      else:
        green_lose = True
    
    # changes the snake positions
    snake_x1 += x1_change
    snake_y1 += y1_change
    snake_x2 += x2_change
    snake_y2 += y2_change

    # draws the background and food
    dis.fill(Colors.BACKGROUND)
    pygame.draw.rect(dis, Colors.FOOD, [food_x, food_y, Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK])

    # creates a list for the snake head
    # and appends that list to the list containg
    # the whole snake
    snake_head_1 = []
    snake_head_1.append(snake_x1)
    snake_head_1.append(snake_y1)
    snake_list_1.append(snake_head_1)

    snake_head_2 = []
    snake_head_2.append(snake_x2)
    snake_head_2.append(snake_y2)
    snake_list_2.append(snake_head_2)

    # deletes the snakes tail so it isn't
    # growing infinitely
    if not len(snake_list_1) == snake_length_1:
      del snake_list_1[0]

    if not len(snake_list_2) == snake_length_2:
      del snake_list_2[0]

    # checks to see if the snake has hit
    # itself, ends the game if it has
    for x in snake_list_1[:-1]:
      if x == snake_head_1:
        print("Hit self")
        game_close = True
        blue_lose = True
    
    for x in snake_list_2[:-1]:
      if x == snake_head_2:
        print("Hit self")
        game_close = True
        if blue_lose == True:
          both_lose = True
        else:
          green_lose = True

    # checks to see if p2 ran into p1
    for i in snake_list_1[:-1]:
      if i == snake_head_2:
        print("collided with other player")
        game_close = True
        green_lose = True
    
    # checks to see if p1 ran into p2
    for i in snake_list_2[:-1]:
      if i == snake_head_1:
        print("Collided with other player")
        game_close = True
        if green_lose == True:
          both_lose = True
        else:
          blue_lose = True

      # checks to see if they bonked heads.
      # if they have, sets both to having lost
      if snake_head_1 == snake_head_2:
        print("Head to head")
        game_close = True
        both_lose = True

    # draws both snakes
    draw_snake(Sizes.SNAKE_BLOCK, Colors.SNAKE, snake_list_1)
    draw_snake(Sizes.SNAKE_BLOCK, Colors.GREENISH, snake_list_2)

    # shows every thing
    pygame.display.update()

    # if the snake has the food, generates
    # a new food positon and grows the snake
    if snake_x1 == food_x and snake_y1 == food_y:
      food_x = random.randint(0, Sizes.SCREEN_WIDTH)
      food_y = random.randint(0, Sizes.SCREEN_HEIGHT)
      food_x = food_x - food_x % Sizes.SNAKE_BLOCK
      food_y = food_y - food_y % Sizes.SNAKE_BLOCK
      snake_length_1 += 1
    elif snake_x2 == food_x and snake_y2 == food_y:
      food_x = random.randint(0, Sizes.SCREEN_WIDTH)
      food_y = random.randint(0, Sizes.SCREEN_HEIGHT)
      food_x = food_x - food_x % Sizes.SNAKE_BLOCK
      food_y = food_y - food_y % Sizes.SNAKE_BLOCK
      snake_length_2 += 1

    # makes time pass.
    clock.tick(SNAKE_SPEED)

  # ends the game once the loop is fully complete
  pygame.quit()
#   quit()

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