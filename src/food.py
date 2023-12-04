import random

def gen_food_position(width: int, height: int, allow_edge = True) -> tuple[int, int]:
  """Generates a random position for the food to be placed. By setting allow_edge to False, the food will not be placed on the edge of the screen."""
  
  if allow_edge:
    food_x = random.randint(0, width)
    food_y = random.randint(0, height)
  else:
    food_x = random.randint(1, width - 1)
    food_y = random.randint(1, height - 1)
  
  return (food_x, food_y)