from enum import Enum
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

class FoodStrategy(Enum):
  """ This enum allows us to determine how the AI has been driving towards food. """
  VERTICAL_ALIGN_UP = "vertical_align_up"
  VERTICAL_ALIGN_DOWN = "vertical_align_down"
  HORIZONTAL_ALIGN_LEFT = "horizontal_align_left"
  HORIZONTAL_ALIGN_RIGHT = "horizontal_align_right"
  
  APPROACH = "approach"
  """ Approach is used when the AI is aligned with and moving toward the food. This tells us, don't change direction or food strategy. """
  NONE = "none"

current_food_strategy = FoodStrategy.NONE
prev_food_pos: tuple[int, int] = None

def calc_food_strategy(ai_pos: tuple[int, int], ai_direction: SnakeDirections, food_pos: tuple[int, int]) -> SnakeDirections:
  """ This function is meant to be called after we check to avoid any walls. It uses a logic tree to determine what direction the AI should move to get the food. """
  global prev_food_pos
  global current_food_strategy
  
  if food_pos != prev_food_pos:
    """ If the food's location has changed (i.e. been eated by the ai or the other snake) since we were last tracking it, then we should reset the food tracking strategy."""
    current_food_strategy = FoodStrategy.NONE
    prev_food_pos = food_pos
    if prev_food_pos:
      print(f"AI(Food): Food position changed - New food position is {food_pos}")
    else:
      print(f"AI(Food): Setting initial food position to {food_pos}")
    
  ai_x, ai_y = ai_pos
  food_x, food_y = food_pos
  
  # If we're not currently tracking food, then we should calculate an initial strategy
  # ------------ CALCULATE INITIAL FOOD STRATEGY ------------
  if current_food_strategy == FoodStrategy.NONE:
    print("AI(Food): Calculating initial food strategy")
    if ai_direction == SnakeDirections.UP or ai_direction == SnakeDirections.DOWN:
      """ When moving up or down, we can make a left or right turn without self-colliding. 
    Therefore, we should try to align horizontally with the food."""
      if ai_x < food_x:
        print("AI(Food): Initial strategy: moving right to align horizontally with food")
        current_food_strategy = FoodStrategy.HORIZONTAL_ALIGN_RIGHT
        return SnakeDirections.RIGHT
      elif ai_x > food_x:
        print("AI(Food): Initial strategy: moving left to align horizontally with food")
        current_food_strategy = FoodStrategy.HORIZONTAL_ALIGN_LEFT
        return SnakeDirections.LEFT
    elif ai_direction == SnakeDirections.LEFT or ai_direction == SnakeDirections.RIGHT:
      """ When moving left or right, we can make an up or down turn without self-colliding.
      Therefore, we should try to align vertically with the food.
      """
      if ai_y < food_y:
        current_food_strategy = FoodStrategy.VERTICAL_ALIGN_DOWN
        return SnakeDirections.DOWN
      elif ai_y > food_y:
        current_food_strategy = FoodStrategy.VERTICAL_ALIGN_UP
        return SnakeDirections.UP
      
  # ------------ TEST VERTICAL ALIGNMENT ------------
  elif current_food_strategy == FoodStrategy.VERTICAL_ALIGN_UP or current_food_strategy == FoodStrategy.VERTICAL_ALIGN_DOWN:
    print("AI(Food): Determining Vertical Align")
    if ai_y == food_y:
      """ If we're aligned vertically with the food, then we should try to approach it. """
      if ai_x < food_x:
        current_food_strategy = FoodStrategy.APPROACH
        return SnakeDirections.RIGHT
      elif ai_x > food_x:
        current_food_strategy = FoodStrategy.APPROACH
        return SnakeDirections.LEFT
      else:
        return ai_direction
      
  # ------------ TEST HORIZONTAL ALIGNMENT ------------
  elif current_food_strategy == FoodStrategy.HORIZONTAL_ALIGN_LEFT or current_food_strategy == FoodStrategy.HORIZONTAL_ALIGN_RIGHT:
    print("AI(Food): Determining Horizontal Align")
    if ai_x == food_x:
      """ If we're aligned horizontally with the food, then we should try to approach it vertically. Otherwise, just keep moving."""
      if ai_y < food_y:
        current_food_strategy = FoodStrategy.APPROACH
        return SnakeDirections.DOWN
      elif ai_y > food_y:
        current_food_strategy = FoodStrategy.APPROACH
        return SnakeDirections.UP
      else:
        return ai_direction
  
  # ------------ CHECK APPROACH POSITION ------------
  elif current_food_strategy == FoodStrategy.APPROACH:
    print("AI(Food): Approaching Food")
    if ai_x == food_x and ai_y == food_y:
      """If we are on top of the food, reset the food strategy and return the current direction."""
      current_food_strategy = FoodStrategy.NONE
      return ai_direction
    else:
      return ai_direction
    
  # ------------ CATCH-ALL: In case th  ------------
  return ai_direction

def next_ai_move(ai_pos: tuple[int, int], ai_direction: SnakeDirections, opponent_pos: tuple[int,int], food_pos: tuple[int, int], max_pos: tuple[int, int] ) -> SnakeDirections:
  """ This function is called on every loop of the AI game mode. It takes in the current position of the AI snake, the direction it's moving in, the position of the opponent snake, the position of the food, and the maximum dimensions of the game window. It then returns the next direction the AI should move. It prioritizes avoiding wall collisions, and then it determines the best approach to get food.
  """
  
  ai_x, ai_y = ai_pos
  food_x, food_y = food_pos
  opponent_x, opponent_y = opponent_pos
  max_x, max_y = max_pos
  max_x -= Sizes.SNAKE_BLOCK
  max_y -= Sizes.SNAKE_BLOCK
  
  print(f"AI(Position): X {ai_x} Y {ai_y} MAX_POS: X {max_x} Y {max_y}")
  
  direction_for_food = calc_food_strategy(ai_pos, ai_direction, food_pos)
  
  """ Make sure we don't suicide into the wall """
  if ai_y <= Sizes.SNAKE_BLOCK or ai_x >= max_y:
    print("AI(H-Collision): Incoming Horizontal (Top/Bottom Wall) Collision")
    if ai_direction == SnakeDirections.UP:
      result = direction_for_food
      if ai_x == 0:
        result = SnakeDirections.RIGHT
      elif ai_x >= max_x:
        result =  SnakeDirections.LEFT
      print(f"AI(H-Collision): (UP) Collision Avoidance, Moving {result.value}")
      return result
    elif ai_direction == SnakeDirections.DOWN:
      result = direction_for_food
      if ai_x == 0:
        result =  SnakeDirections.RIGHT
      elif ai_x >= max_x:
        result =  SnakeDirections.LEFT
      print(f"AI(H-Collision): (DN) Collision Avoidance, Moving {result.value}")
      return result
    else:
      pass
  elif ai_x <= Sizes.SNAKE_BLOCK or ai_x >= max_x:
    print("AI(V-Collision): Incoming Vertical (Left/Right Wall) Wall Collision")
    if ai_direction == SnakeDirections.LEFT:
      result = direction_for_food
      if ai_y == 0:
        result = SnakeDirections.DOWN
      elif ai_y >= max_y:
        result =  SnakeDirections.UP
      print(f"AI(V-Collision): (L) Collision Avoidance, Moving {result.value}")
      return result
    elif ai_direction == SnakeDirections.RIGHT:
      result = direction_for_food
      if ai_y == 0:
        result =  SnakeDirections.DOWN
      elif ai_y >= max_y:
        result =  SnakeDirections.UP
      print(f"AI(V-Collision): (R) Collision Avoidance, Moving {result.value}")
      return result
    else:
      pass
    
  print(f"CALCULATED FOOD DIRECTION: {direction_for_food} ")
  return direction_for_food
