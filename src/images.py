import pygame
import init as globals
from constants import Colors, Sizes, Fonts


# Creates snake p1 body
snake_body_blue = pygame.image.load('assets\snake_body_blue.png').convert_alpha()
snake_body_blue = pygame.transform.smoothscale(snake_body_blue, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))

# Creates snake p2 body
snake_body_green = pygame.image.load('assets\snake_body_green.png').convert_alpha()
snake_body_green = pygame.transform.smoothscale(snake_body_green, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))

# Creates snake p1 head
snake_head_blue = pygame.image.load('assets\snake_head_blue.png').convert_alpha()
snake_head_blue = pygame.transform.smoothscale(snake_head_blue, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))

# Creates snake p2 head
snake_head_green = pygame.image.load('assets\snake_head_green.png').convert_alpha()
snake_head_green = pygame.transform.smoothscale(snake_head_green, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))

# Creates snake p1 tail
snake_tail_blue = pygame.image.load('assets\snake_tail_blue.png').convert_alpha()
snake_tail_blue = pygame.transform.smoothscale(snake_tail_blue, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))

# Creates snake p2 tail
snake_tail_green = pygame.image.load('assets\snake_tail_green.png').convert_alpha()
snake_tail_green = pygame.transform.smoothscale(snake_tail_green, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))

# Creates the apple image
grape_image = pygame.image.load('assets\grape.png').convert_alpha()
grape_image = pygame.transform.smoothscale(grape_image, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))