import pygame
import init as globals
from constants import Colors, Sizes, Fonts


# Creates snake p1 body
snake_body = pygame.image.load('assets\snake_body.png').convert_alpha()
snake_body = pygame.transform.scale(snake_body, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))

# Creates the apple image
grape_image = pygame.image.load('assets\grape.png').convert_alpha()
grape_image = pygame.transform.scale(grape_image, (Sizes.SNAKE_BLOCK, Sizes.SNAKE_BLOCK))