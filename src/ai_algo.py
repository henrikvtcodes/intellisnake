
from constants import SnakeDirections, Sizes
import random


def calc_ai_move(ai_pos: tuple[int, int], ai_direction: SnakeDirections, opponent_pos: tuple[int,int], food_pos: tuple[int, int], max_pos: tuple[int, int] ) -> SnakeDirections:
  """Returns the next move for the AI snake.

  Args:
      ai_pos (tuple[int, int]): The position of the AI snake.
      food_pos (tuple[int, int]): The position of the food.

  Returns:
      tuple[int, int]: The next move for the AI snake.
  """
  
  ai_x, ai_y = ai_pos
  food_x, food_y = food_pos
  opponent_x, opponent_y = opponent_pos
  max_x, max_y = max_pos
  
  """ Make sure we don't suicide into the wall """
  if ai_direction == SnakeDirections.LEFT:
    if ai_x == 0:
      if ai_y == 0:
        return SnakeDirections.DOWN
      elif ai_y == max_x - Sizes.SNAKE_BLOCK:
        return SnakeDirections.UP
  elif ai_direction == SnakeDirections.RIGHT:
    if ai_x == max_x - Sizes.SNAKE_BLOCK:
      if ai_y == 0:
        return SnakeDirections.DOWN
      elif ai_y == max_x:
        return SnakeDirections.UP
  elif ai_direction == SnakeDirections.UP:
    if ai_y == 0:
      if ai_x == 0:
        return SnakeDirections.RIGHT
      elif ai_x == max_x - Sizes.SNAKE_BLOCK:
        return SnakeDirections.LEFT
  elif ai_direction == SnakeDirections.DOWN:
    if ai_y == max_y - Sizes.SNAKE_BLOCK:
      if ai_x == 0:
        return SnakeDirections.RIGHT
      elif ai_x == max_x - Sizes.SNAKE_BLOCK:
        return SnakeDirections.LEFT
      
  
  return ai_direction
    
  random_choice_list: list[SnakeDirections] = []
  # Impl Random Move
  for d in SnakeDirections:
    if d != ai_direction:
      random_choice_list.append(d)
      
  rand_move = random.choice(random_choice_list)
  
  print(f"Algo Result: {rand_move}")
  return rand_move
    
    
  head_above_food = ai_pos[1] < food_pos[1]
  head_left_of_food = ai_pos[0] < food_pos[0]
  
  
  
  return SnakeDirections.LEFT