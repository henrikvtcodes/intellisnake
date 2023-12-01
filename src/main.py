import pygame
import numpy as np
import time
import random


# Displays the score. currently only called on the losing screen.
# Do we want to call it elsewhere so there is a constant score?
def your_score(score): 
  value = score_font.render("Your Score: " + str(score), True, green)
  dis.blit(value, [0, 0])

# Draws a snake. Currently called for one snake, should be able
# to call it for the second snake as well.
def draw_snake(snake_block, snake_list):
  for x in snake_list:
    pygame.draw.rect(dis, snake_color, [x[0], x[1], snake_block, snake_block])

# displays the message for the losing screen. idk why I can't get it centered.
def message(msg, color):
  mesg = font_style.render(msg, True, color)
  dis.blit(mesg, [dis_width / 6, dis_height / 3])

# The main game outline is here. We could make
# other functions for other gamemodes.
def game_loop():
  game_over = False
  game_close = False
  
  # Generates our current only snakes starting
  # pos. 
  snake_x1 = dis_width / 2
  snake_y1 = dis_height / 2

  # This is what decides how far the snake 
  # moves.
  x1_change = 0
  y1_change = 0

  snake_list = []
  snake_length = 1

  # generates a starting apple position.
  food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
  food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

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
      dis.fill(black)
      message("You lost! Press Q-Quit or C-Play again", red)
      your_score(snake_length - 1)
      pygame.display.update()

      #waits for the user to pick an option
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            game_close = False
            game_over = True
          if event.key == pygame.K_c:
            game_loop()

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
          x1_change = -snake_block
          y1_change = 0
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
          x1_change = snake_block
          y1_change = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
          x1_change = 0
          y1_change = -snake_block
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
          x1_change = 0
          y1_change = snake_block
    
    #checks if the snake is out of bounds
    if snake_x1 == dis_width or snake_x1 == 0 or snake_y1 == dis_height or snake_y1 == 0:
      game_close = True
    
    # changes the snake positions
    snake_x1 += x1_change
    snake_y1 += y1_change
    # draws the background and food
    dis.fill(background_color)
    pygame.draw.rect(dis, food_color, [food_x, food_y, snake_block, snake_block])

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
    draw_snake(snake_block, snake_list)

    # shows every thing
    pygame.display.update()

    # if the snake has the food, generates
    # a new food positon and grows the snake
    if snake_x1 == food_x and snake_y1 == food_y:
      food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
      food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
      snake_length += 1

    # makes time pass.
    clock.tick(snake_speed)

  # ends the game once the loop is fully complete
  pygame.quit()
  quit()

pygame.init()

# sets display size 
dis_width = 600
dis_height = 400
dis=pygame.display.set_mode((dis_width, dis_height))

# shows the screen
pygame.display.update()
pygame.display.set_caption("Intellisnake")

# the colors I used
background_color = (255, 112, 205)
snake_color = (90, 196, 255)
black = (0, 0, 0)
red = (255, 0, 0)
food_color = (200, 0, 200)
green = (52, 235, 134)

# size of the snake square.
# I figured it was easier to deal
# in squares to start rather than 
#starting with the assets.
snake_block = 10

# makes the clock and sets the game
# speed
clock = pygame.time.Clock()
snake_speed = 15

# fonts used for score and the lose
# menu
font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont("comicsansms", 35)

# the part that we actually run.
if __name__ == "__main__":

  game_loop()