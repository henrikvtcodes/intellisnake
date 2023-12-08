from constants import *

def check_collison_course(opp_snake, my_snake, x, y, cur_dir):
    print(cur_dir)
    if cur_dir == SnakeDirections.DOWN:
        y += Sizes.SNAKE_BLOCK
    if cur_dir == SnakeDirections.UP:
        y -= Sizes.SNAKE_BLOCK
    if cur_dir == SnakeDirections.LEFT:
        x -= Sizes.SNAKE_BLOCK
    if cur_dir == SnakeDirections.RIGHT:
        x += Sizes.SNAKE_BLOCK
 
    for i in opp_snake:
        if i[0] == x and i[1] == y:
            print("Collision immenent!")
            return True
    for k in my_snake:
        if k[0] == x and k[1] == y:
            return True
    return False



def generate_next_move(opp_snake, my_snake, x, y, goal_x, goal_y, cur_dir):
    
    up = (0, -Sizes.SNAKE_BLOCK)
    down = (0, Sizes.SNAKE_BLOCK)
    left = (-Sizes.SNAKE_BLOCK, 0)
    right = (Sizes.SNAKE_BLOCK, 0)

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
                return up
            elif oob_up:
                print("oob right and up")
                return down
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.UP):
                return down
            else:
                return up
        
    if oob_left:
        print(cur_dir)
        if cur_dir == SnakeDirections.LEFT:
            if oob_down:
                print("Oob left and down")
                return up
            elif oob_up:
                print("oob left and up")
                return down
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.UP):
                return down
            else:
                return up
        
    if oob_up:
        if cur_dir == SnakeDirections.UP:
            if oob_right:
                print("oob up and right")
                return left
            elif oob_left:
                print("oob up and left")
                return right
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.LEFT):
                return right
            else:
                return left
        
    if oob_down:
        if cur_dir == SnakeDirections.DOWN:
            if oob_right:
                print("oob down and right")
                return left
            elif oob_left:
                print("oob down and left")
                return right
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.LEFT):
                return right
            else:
                return left
    
    if check_collison_course(opp_snake, my_snake, x, y, cur_dir):
        print("Collision warning received")
        if cur_dir == SnakeDirections.UP or cur_dir == SnakeDirections.DOWN:
            print("issue is here 1")
            if oob_left:
                return right
            elif oob_right:
                return right
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.LEFT):
                return right
            else:
                return left
        elif cur_dir == SnakeDirections.LEFT or cur_dir == SnakeDirections.RIGHT:
            print("issue is here 2")
            if oob_down:
                return up
            elif oob_up:
                return down
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.UP):
                return down
            else:
                return up


    print("no oob detected")
    return (0, 0)

    # Checks if it will hit itself
    # checks if it will hit other snake
    # Tries to move to grape