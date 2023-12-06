import pygame
import init as globals
from constants import Colors, Sizes, Fonts
import platform

# Windows NTFS paths uses backslashes for some reason, so this code is for loading images on Windows
if platform.system() == 'Windows':
  # Creates snake p1 body
  snake_body_blue = pygame.image.load('assets\snake_body_blue.png').convert_alpha()
  # Creates snake p2 body
  snake_body_green = pygame.image.load('assets\snake_body_green.png').convert_alpha()
  # Creates snake p1 head
  snake_head_blue = pygame.image.load('assets\snake_head_blue.png').convert_alpha()
  # Creates snake p2 head
  snake_head_green = pygame.image.load('assets\snake_head_green.png').convert_alpha()
  # Creates snake p1 tail
  snake_tail_blue = pygame.image.load('assets\snake_tail_blue.png').convert_alpha()
  # Creates snake p2 tail
  snake_tail_green = pygame.image.load('assets\snake_tail_green.png').convert_alpha()
  # Creates the p1 mini head
  snake_head_blue_mini = pygame.image.load('assets\snake_head_blue_mini.png').convert_alpha()
  # Creates the p2 mini head
  snake_head_green_mini = pygame.image.load('assets\snake_head_green_mini.png').convert_alpha()
  # Creates the apple image
  grape_image = pygame.image.load('assets\grape.png').convert_alpha()

# Code that loads images on Mac 
else:
  # Creates snake p1 body
  snake_body_blue = pygame.image.load('assets/snake_body_blue.png').convert_alpha()
  # Creates snake p2 body
  snake_body_green = pygame.image.load('assets/snake_body_green.png').convert_alpha()
  # Creates snake p1 head
  snake_head_blue = pygame.image.load('assets/snake_head_blue.png').convert_alpha()
  # Creates snake p2 head
  snake_head_green = pygame.image.load('assets/snake_head_green.png').convert_alpha()
  # Creates snake p1 tail
  snake_tail_blue = pygame.image.load('assets/snake_tail_blue.png').convert_alpha()
  # Creates snake p2 tail
  snake_tail_green = pygame.image.load('assets/snake_tail_green.png').convert_alpha()
  # Creates the p1 mini head
  snake_head_blue_mini = pygame.image.load('assets/snake_head_blue_mini.png').convert_alpha()
  # Creates the p2 mini head
  snake_head_green_mini = pygame.image.load('assets/snake_head_green_mini.png').convert_alpha()
  # Creates the apple image
  grape_image = pygame.image.load('assets/grape.png').convert_alpha()

# Make sure all images are scaled to the proper size in-game

snake_body_blue = pygame.transform.smoothscale(snake_body_blue, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))

snake_body_green = pygame.transform.smoothscale(snake_body_green, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))

snake_head_blue = pygame.transform.smoothscale(snake_head_blue, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))

snake_head_green = pygame.transform.smoothscale(snake_head_green, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))

snake_tail_blue = pygame.transform.smoothscale(snake_tail_blue, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))

snake_tail_green = pygame.transform.smoothscale(snake_tail_green, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))

snake_head_blue_mini = pygame.transform.smoothscale(snake_head_blue_mini, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))

snake_head_green_mini = pygame.transform.smoothscale(snake_head_green_mini, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))

grape_image = pygame.transform.smoothscale(grape_image, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))