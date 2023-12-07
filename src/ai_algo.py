
import logging
from constants import Sizes, SnakeDirections, Sizes
import random

initial_move = random.choice([SnakeDirections.UP, SnakeDirections.DOWN])

logger = logging.getLogger("algorithm")

def calc_smart_coords(coords: tuple[int, int]):
  return coords[0] // Sizes.SNAKE_BLOCK, coords[1] // Sizes.SNAKE_BLOCK

def avoid_horizontal_wall_collision(ai_pos: tuple[int, int], ai_direction: SnakeDirections, max_pos: tuple[int, int]) -> SnakeDirections | None:
  """ This function is called when the AI snake is about to collide with the top or bottom (horizontal) walls. It decides whether to go left or right depending on if the snake is near a corner, so that it doesn't crash into the left or right walls while trying to avoid a horizontal wall.
  """
  ai_x, ai_y = ai_pos
  max_x, max_y = max_pos
  
  if ai_y <= 0 and ai_direction == SnakeDirections.UP:
    if ai_x <= 0:
      return SnakeDirections.RIGHT
    elif ai_x >= max_x:
      return SnakeDirections.LEFT
  if ai_y >= max_y and ai_direction == SnakeDirections.DOWN:
    if ai_x <= 0:
      return SnakeDirections.RIGHT
    elif ai_x >= max_x:
      return SnakeDirections.LEFT
  
  return None


def avoid_vertical_wall_collision(ai_pos: tuple[int, int], ai_direction: SnakeDirections, max_pos: tuple[int, int]) -> SnakeDirections | None:
  ai_x, ai_y = ai_pos
  max_x, max_y = max_pos
  
  if ai_x <= 0 and ai_direction == SnakeDirections.LEFT:
    if ai_y <= 0:
      return SnakeDirections.RIGHT
    elif ai_y >= max_y:
      return SnakeDirections.LEFT
  if ai_x >= max_x and ai_direction == SnakeDirections.RIGHT:
    if ai_y <= 0:
      return SnakeDirections.RIGHT
    elif ai_y >= max_y:
      return SnakeDirections.LEFT
  
  return None
  

def calc_ai_move(ai_pos: tuple[int, int], ai_direction: SnakeDirections, opponent_pos: tuple[int,int], food_pos: tuple[int, int], max_pos: tuple[int, int] ) -> SnakeDirections:
  """
  """
  
  # ai_x, ai_y = calc_smart_coords(ai_pos)
  ai_x, ai_y = ai_pos
  food_x, food_y = food_pos
  opponent_x, opponent_y = opponent_pos
  # max_x, max_y = calc_smart_coords(max_pos)
  max_x, max_y = max_pos
  max_x -= Sizes.SNAKE_BLOCK
  max_y -= Sizes.SNAKE_BLOCK
  
  print(f"AI MODE COORDS: X {ai_x} Y {ai_y} MAX_POS: X {max_x} Y {max_y}")
  
  """ Make sure we don't suicide into the wall """
  if ai_y <= Sizes.SNAKE_BLOCK or ai_x >= max_y:
    horizontal_avoid = avoid_horizontal_wall_collision(ai_pos, ai_direction, (max_x, max_y))
    # vertical_avoid can return None, so if it does, that means we should move on to the rest of the algorithm
    if horizontal_avoid:
      return horizontal_avoid
    else:
      pass
  elif ai_x <= Sizes.SNAKE_BLOCK or ai_x >= max_x:
    vertical_avoid =  avoid_vertical_wall_collision(ai_pos, ai_direction, (max_x, max_y))
    # vertical_avoid can return None, so if it does, that means we should move on to the rest of the algorithm
    if vertical_avoid:
      return vertical_avoid
    else:
      pass
  
  
    
  random_choice_list: list[SnakeDirections] = []
  # Impl Random Move
  for d in SnakeDirections:
    if d != ai_direction:
      random_choice_list.append(d)
      
  rand_move = random.choice(random_choice_list)
  
  # print(f"Algo Result: {rand_move}")
  return SnakeDirections.DOWN
    
    
  head_above_food = ai_pos[1] < food_pos[1]
  head_left_of_food = ai_pos[0] < food_pos[0]
  
  
  
  return SnakeDirections.LEFT