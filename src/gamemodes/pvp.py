import pygame
from pygame.locals import *
import numpy as np
from food import gen_food_position
from constants import Colors, GameEndStates, GameModes, GameWindowStates, Sizes, SNAKE_SPEED
from images import *

import init as globals

from draw_fns import draw_snake, draw_message

def start_pvp():
  # sets the window state to playing
  # the next time the main loop, well, loops, it will run the function for the gamemode.
  globals.GameStateContainer.window_state = GameWindowStates.PLAYING
  globals.GameStateContainer.game_mode = GameModes.PVP

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

  direction_blue = 'right'
  direction_green = 'right'

  # generates a starting apple position.
  food_x, food_y = gen_food_position(Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT)

  # continues as long as the game isn't over.
  # yeah.
  while globals.GameStateContainer.window_state == GameWindowStates.PLAYING:

    # after receiving the lose condition
    # this occurs, prompting whether or not
    # the player wants to go again.
    # We could add a high score save thing 
    # and/or a main menu option to choose a
    # new gamemode.
    # while game_close == True:
    #   globals.window.fill(Colors.FOOD)
    #   if blue_lose == True:
    #     draw_message("Player 2 (Green) snake wins! Press Q-Quit or C-Play again", Colors.GREENISH)
    #   elif green_lose == True:
    #     draw_message("Player 1 (Blue) snake wins! Press Q-Quit or C-Play again", Colors.SNAKE)
    #   else:
    #     globals.window.fill(Colors.BLACK)
    #     draw_message("You both lose! Press Q-Quit or C-Play again", Colors.RED)
      
    #   pygame.display.update()

    #   #waits for the user to pick an option
    #   for event in pygame.event.get():

    #     if event.type == pygame.QUIT:
    #       game_over = True
    #       game_close = False
    #       globals.GameStateContainer.window_state = GameWindowStates.END

    #     if event.type == pygame.KEYDOWN:
    #       if event.key == pygame.K_q:
    #         game_close = False
    #         game_over = True
    #         globals.GameStateContainer.window_state = GameWindowStates.END

    #       if event.key == pygame.K_c:
    #         pvp_mode()

    # if the user clicks or presses a key
    # that does something, that is read here.
    # If they quit, it ends the program, if they
    # hit one of the arrow or wasd keys it sets the
    # direction change.
    # player one or blue snake is arrows, player
    # 2 or green snake is wasd.
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        globals.GameStateContainer.window_state = GameWindowStates.EXIT
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          if not x1_change == Sizes.SNAKE_BLOCK:
            x1_change = -Sizes.SNAKE_BLOCK
            y1_change = 0
            direction_blue = 'left'
        if event.key == pygame.K_RIGHT:
          if not x1_change == -Sizes.SNAKE_BLOCK:
            x1_change = Sizes.SNAKE_BLOCK
            y1_change = 0
            direction_blue = 'right'
        if event.key == pygame.K_UP:
          if not y1_change == Sizes.SNAKE_BLOCK:
            x1_change = 0
            y1_change = -Sizes.SNAKE_BLOCK
            direction_blue = 'up'
        if event.key == pygame.K_DOWN:
          if not y1_change == -Sizes.SNAKE_BLOCK:
            x1_change = 0
            y1_change = Sizes.SNAKE_BLOCK
            direction_blue = 'down'
        if event.key == pygame.K_a:
          if not x2_change == Sizes.SNAKE_BLOCK:
            x2_change = -Sizes.SNAKE_BLOCK
            y2_change = 0
            direction_green = 'left'
        if event.key == pygame.K_d:
          if not x2_change == -Sizes.SNAKE_BLOCK:
            x2_change = Sizes.SNAKE_BLOCK
            y2_change = 0
            direction_green = 'right'
        if event.key == pygame.K_w:
          if not y2_change == Sizes.SNAKE_BLOCK:
            x2_change = 0
            y2_change = -Sizes.SNAKE_BLOCK
            direction_green = 'up'
        if event.key == pygame.K_s:
          if not y2_change == -Sizes.SNAKE_BLOCK:
            x2_change = 0
            y2_change = Sizes.SNAKE_BLOCK
            direction_green = 'down'
    
    # checks if the p1 snake is out of bounds. 
    # assigns win to green if true.
    if snake_x1 == Sizes.SCREEN_WIDTH or snake_x1 < 0 or snake_y1 == Sizes.SCREEN_HEIGHT or snake_y1 < 0:
      print("Out of bounds")
      game_close = True
      blue_lose = True
      globals.GameStateContainer.end_state = GameEndStates.P1_LOSE
      globals.GameStateContainer.window_state = GameWindowStates.END


    # checks if the p2 snake is out of bounds.
    # removes win from p1 if both are true, gives
    # win to p2 if only this is true. 
    if snake_x2 == Sizes.SCREEN_WIDTH or snake_x2 < 0 or snake_y2 == Sizes.SCREEN_HEIGHT or snake_y2 < 0:
      print(snake_x2, snake_y2)
      game_close = True
      if blue_lose == True:
        globals.GameStateContainer.end_state = GameEndStates.BOTH_LOSE
      else:
        globals.GameStateContainer.end_state = GameEndStates.P2_LOSE

      globals.GameStateContainer.window_state = GameWindowStates.END

    
    # changes the snake positions
    snake_x1 += x1_change
    snake_y1 += y1_change
    snake_x2 += x2_change
    snake_y2 += y2_change

    # draws the background and food
    globals.window.fill(Colors.BACKGROUND)
    globals.window.blit(grape_image, (food_x, food_y))

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
        globals.GameStateContainer.end_state = GameEndStates.P1_LOSE
        globals.GameStateContainer.window_state = GameWindowStates.END

    
    for x in snake_list_2[:-1]:
      if x == snake_head_2:
        print("Hit self")
        game_close = True
        if blue_lose == True:
          globals.GameStateContainer.end_state = GameEndStates.BOTH_LOSE
        else:
          globals.GameStateContainer.end_state = GameEndStates.P2_LOSE
          
        globals.GameStateContainer.window_state = GameWindowStates.END

    # checks to see if p2 ran into p1
    for i in snake_list_1[:-1]:
      if i == snake_head_2:
        print("collided with other player")
        game_close = True
        green_lose = True
        globals.GameStateContainer.end_state = GameEndStates.P2_LOSE
        globals.GameStateContainer.window_state = GameWindowStates.END
    
    # checks to see if p1 ran into p2
    for i in snake_list_2[:-1]:
      if i == snake_head_1:
        print("Collided with other player")
        game_close = True
        if green_lose == True:
          globals.GameStateContainer.end_state = GameEndStates.BOTH_LOSE
        else:
          globals.GameStateContainer.end_state = GameEndStates.P1_LOSE
        globals.GameStateContainer.window_state = GameWindowStates.END

      # checks to see if they bonked heads.
      # if they have, sets both to having lost
      if snake_head_1 == snake_head_2:
        print("Head to head")
        game_close = True
        both_lose = True
        globals.GameStateContainer.end_state = GameEndStates.BOTH_LOSE
        globals.GameStateContainer.window_state = GameWindowStates.END
        

    # draws both snakes
    draw_snake(Sizes.SNAKE_BLOCK, Colors.SNAKE, snake_list_1, direction_blue, snake_length_1)
    draw_snake(Sizes.SNAKE_BLOCK, Colors.GREENISH, snake_list_2, direction_green, snake_length_2)

    # shows every thing
    pygame.display.update()

    # if the snake has the food, generates
    # a new food positon and grows the snake
    if snake_x1 == food_x and snake_y1 == food_y:
      food_x, food_y = gen_food_position(Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT)
      snake_length_1 += 1
    elif snake_x2 == food_x and snake_y2 == food_y:
      food_x, food_y = gen_food_position(Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT)
      snake_length_2 += 1

    # makes time pass.
    globals.clock.tick(SNAKE_SPEED)