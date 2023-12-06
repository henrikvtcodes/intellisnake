import random

from constants import Sizes

def gen_food_position(width: int, height: int, snake1, snake2, allow_edge = True) -> tuple[int, int]:
  """Generates a random position for the food to be placed. By setting allow_edge to False, the food will not be placed on the edge of the screen."""
  
  if allow_edge:
    food_x = random.randint(0, width)
    food_y = random.randint(0, height)
  else:
    food_x = random.randint(1, width - 1)
    food_y = random.randint(1, height - 1)
  
  food_x = food_x - food_x % Sizes.SNAKE_BLOCK
  food_y = food_y - food_y % Sizes.SNAKE_BLOCK

  for x in snake1:
    if food_x == x[0] and food_y == x[1]:
      food_x, food_y = gen_food_position(width, height, snake1, snake2)
  for x in snake2:
    if food_x == x[0] and food_y == x[1]:
      food_x, food_y = gen_food_position(width, height, snake1, snake2)
    
  
  return (food_x, food_y)