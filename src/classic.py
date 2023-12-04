import pygame
from pygame.locals import *
import numpy as np
from snake import Snake, Player
import time
import random
from constants import Fonts, Colors, Sizes, SNAKE_SPEED, DIRECTION_VALUES
import init as globals
from draw_fns import draw_snake, draw_message, draw_score

# The main game outline is here. We could make
# other functions for other gamemodes.
def classic_mode():
  game_over = False
  game_close = False
  
  # Generates our current only snakes starting
  # pos. 
  snake_x1 = Sizes.SCREEN_WIDTH / 2
  snake_y1 = Sizes.SCREEN_HEIGHT / 2

  # This is what decides how far the snake 
  # moves.
  x1_change = 0
  y1_change = 0

  snake_list = []
  snake_length = 1

  # generates a starting apple position.
  food_x = round(random.randrange(0, Sizes.SCREEN_WIDTH - Sizes.SNAKE_BLOCK) / 10.0) * 10.0
  food_y = round(random.randrange(0, Sizes.SCREEN_HEIGHT - Sizes.SNAKE_BLOCK) / 10.0) * 10.0

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
      globals.window.fill(Colors.BLACK)
      draw_message("You lost! Press Q-Quit or C-Play again", Colors.RED)
      draw_score(snake_length - 1)
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
            classic_mode()

    # if the user clicks or presses a key
    # that does something, that is read here.
    # If they quit, it ends the program, if they
    # hit one of the arrow or wasd keys it sets the
    # direction change.
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        game_over = True
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
          x1_change = -Sizes.SNAKE_BLOCK
          y1_change = 0
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
          x1_change = Sizes.SNAKE_BLOCK
          y1_change = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
          x1_change = 0
          y1_change = -Sizes.SNAKE_BLOCK
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
          x1_change = 0
          y1_change = Sizes.SNAKE_BLOCK
    
    #checks if the snake is out of bounds
    if snake_x1 == Sizes.SCREEN_WIDTH or snake_x1 == 0 or snake_y1 == Sizes.SCREEN_HEIGHT or snake_y1 == 0:
      game_close = True
    
    # changes the snake positions
    snake_x1 += x1_change
    snake_y1 += y1_change
    # draws the background and food
    globals.window.fill(Colors.BACKGROUND)
    pygame.draw.rect(globals.window, Colors.FOOD, [food_x, food_y, Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK])

    # creates a list for the snake head
    # and appends that list to the list containg
    # the whole snake
    snake_head = []
    snake_head.append(snake_x1)
    snake_head.append(snake_y1)
    snake_list.append(snake_head)

    # deletes the snakes tail so it isn't
    # growing infinitely
    if not len(snake_list) == snake_length:
      del snake_list[0]

    # checks to see if the snake has hit
    # itself, ends the game if it has
    for x in snake_list[:-1]:
      if x == snake_head:
        game_close = True

    # draws the snake. 
    draw_snake(Sizes.SNAKE_BLOCK, Colors.SNAKE, snake_list)

    # shows every thing
    pygame.display.update()

    # if the snake has the food, generates
    # a new food positon and grows the snake
    if snake_x1 == food_x and snake_y1 == food_y:
      food_x = round(random.randrange(0, Sizes.SCREEN_WIDTH - Sizes.SNAKE_BLOCK) / 10.0) * 10.0
      food_y = round(random.randrange(0, Sizes.SCREEN_HEIGHT - Sizes.SNAKE_BLOCK) / 10.0) * 10.0
      snake_length += 1

    # makes time pass.
    globals.clock.tick(SNAKE_SPEED)

  # ends the game once the loop is fully complete
  pygame.quit()
#   quit()

# size of the snake square.
# I figured it was easier to deal
# in squares to start rather than 
#starting with the assets.