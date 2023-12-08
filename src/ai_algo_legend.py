from constants import *

def generate_next_move(opp_snake, my_snake, x, y, goal_x, goal_y, cur_dir):
    
    oob_up = False
    oob_down = False
    oob_left = False
    oob_right = False
    # Checks out of bounds
    if x == Sizes.SCREEN_WIDTH - Sizes.SNAKE_BLOCK:
        oob_right = True
        print("oob right")
    if x < 20:
        oob_left = True
        print("oob left")
    if y == Sizes.SCREEN_HEIGHT - Sizes.SNAKE_BLOCK:
        oob_down = True
        print("oob down")
    if y < 20: 
        print("oob up")
        oob_up = True
    
    if oob_right:
        if cur_dir == SnakeDirections.RIGHT:
            if oob_down:
                print("oob right and down")
                return (0, -Sizes.SNAKE_BLOCK)
            else:
                print("oob right and up")
                print(x, y)
                return(0, Sizes.SNAKE_BLOCK)
        
    if oob_left:
        print(cur_dir)
        if cur_dir == SnakeDirections.LEFT:
            if oob_down:
                print("Oob left and down")
                return (0, -Sizes.SNAKE_BLOCK)
            else:
                print("oob left and up")
                return(0, Sizes.SNAKE_BLOCK)
        
    if oob_up:
        if cur_dir == SnakeDirections.UP:
            if oob_right:
                print("oob up and right")
                return(-Sizes.SNAKE_BLOCK, 0)
            else:
                print("oob up and left")
                return (Sizes.SNAKE_BLOCK, 0)
        
    if oob_down:
        if cur_dir == SnakeDirections.DOWN:
            if oob_right:
                print("oob down and right")
                return(-Sizes.SNAKE_BLOCK, 0)
            else:
                print("oob down and left")
                return (Sizes.SNAKE_BLOCK, 0)
    
    print("no oob detected")
    return (0, 0)

    # Checks if it will hit itself
    # checks if it will hit other snake
    # Tries to move to grape