import pygame
from pygame.locals import *
from food import *
from constants import Colors, GameEndStates, GameModes, GameWindowStates, Sizes, SNAKE_SPEED, MAX_SCORE
import init as globals
from draw_fns import draw_snake, draw_message, draw_score, draw_background
from images import *
from sounds import *

def start_classic():
  if globals.GameStateContainer.escape_pressed:
    globals.GameStateContainer.window_state = GameWindowStates.START
    globals.GameStateContainer.escape_pressed = False
    print("Autoavoid Race Condition: Classic Mode Start Aborted")
    return
  # sets the window state to playing
  # the next time the main loop, well, loops, it will run the function for the gamemode.
  globals.GameStateContainer.window_state = GameWindowStates.PLAYING
  globals.GameStateContainer.game_mode = GameModes.CLASSIC

# The main game outline is here. We could make
# other functions for other gamemodes.
def classic_mode():
  game_over = False
  game_close = False
  
  # Generates our current only snakes starting
  # pos. 
  snake_x1 = Sizes.SCREEN_WIDTH / 2
  snake_y1 = Sizes.SCREEN_HEIGHT / 2

  snake_x1 -= snake_x1 % Sizes.SNAKE_BLOCK
  snake_y1 -= snake_y1 % Sizes.SNAKE_BLOCK

  # This is what decides how far the snake 
  # moves.
  x1_change = 0
  y1_change = 0

  direction = 'right'

  snake_list = []
  snake_length = 1

  # generates a starting apple position.
  food_x, food_y = gen_food_position(Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT, [], [])

  # continues as long as the game isn't over.
  # yeah.
  while globals.GameStateContainer.window_state == GameWindowStates.PLAYING:
    # if the user clicks or presses a key
    # that does something, that is read here.
    # If they quit, it ends the program, if they
    # hit one of the arrow or wasd keys it sets the
    # direction change.
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        globals.GameStateContainer.window_state = GameWindowStates.EXIT
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
          if not x1_change == Sizes.SNAKE_BLOCK:
            x1_change = -Sizes.SNAKE_BLOCK
            y1_change = 0
            direction = 'left'
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
          if not x1_change == -Sizes.SNAKE_BLOCK:
            x1_change = Sizes.SNAKE_BLOCK
            y1_change = 0
            direction = 'right'
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
          if not y1_change == Sizes.SNAKE_BLOCK:
            x1_change = 0
            y1_change = -Sizes.SNAKE_BLOCK
            direction = 'up'
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
          if not y1_change == -Sizes.SNAKE_BLOCK:
            x1_change = 0
            y1_change = Sizes.SNAKE_BLOCK
            direction = 'down'
    
    # checks to see if the board is full
    if snake_length == MAX_SCORE:
      pygame.mixer.Sound.play(win)
      globals.GameStateContainer.end_state = GameEndStates.CLASSIC_WIN
      globals.GameStateContainer.window_state = GameWindowStates.END


    # checks if the snake is out of bounds
    if snake_x1 == Sizes.SCREEN_WIDTH or snake_x1 < 0 or snake_y1 == Sizes.SCREEN_HEIGHT or snake_y1 < 0:
      pygame.mixer.Sound.play(willhelm)
      globals.GameStateContainer.end_state = GameEndStates.CLASSIC_LOSE
      globals.GameStateContainer.window_state = GameWindowStates.END

    
    # changes the snake positions
    snake_x1 += x1_change
    snake_y1 += y1_change
    
    # draws the background and food
    globals.window.fill(Colors.BACKGROUND)
    draw_background()
    globals.window.blit(grape_image, (food_x, food_y))

    # creates a list for the snake head
    # and appends that list to the list containg
    # the whole snake
    snake_head = (snake_x1, snake_y1)
    snake_list.append(snake_head)

    # deletes the snakes tail so it isn't
    # growing infinitely
    if not len(snake_list) == snake_length:
      del snake_list[0]

    # checks to see if the snake has hit
    # itself, ends the game if it has
    for x in snake_list[:-1]:
      if tuple(x) == snake_head:
        pygame.mixer.Sound.play(willhelm)
        globals.GameStateContainer.end_state = GameEndStates.CLASSIC_LOSE
        globals.GameStateContainer.window_state = GameWindowStates.END


    # draws the snake. 
    draw_snake(Sizes.SNAKE_BLOCK, Colors.SNAKE, snake_list, direction, snake_length)

    # shows every thing
    pygame.display.update()

    # if the snake has the food, generates
    # a new food positon and grows the snake
    if snake_x1 == food_x and snake_y1 == food_y:
      pygame.mixer.Sound.play(mlem)
      food_x, food_y = gen_food_position(Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT, snake_list, [])
      snake_length += 1

    # makes time pass.
    globals.clock.tick(SNAKE_SPEED)