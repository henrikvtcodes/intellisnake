from constants import *

# checks if the given direction will cause the 
# ai snake to hit itself or the other snake on the
# next move
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
            return True
    for k in my_snake:
        if k[0] == x and k[1] == y:
            return True
    return False


# generates the ai's next move
def generate_next_move(opp_snake, my_snake, x, y, goal_x, goal_y, cur_dir):

    # sets the possible return values
    up = (0, -Sizes.SNAKE_BLOCK)
    down = (0, Sizes.SNAKE_BLOCK)
    left = (-Sizes.SNAKE_BLOCK, 0)
    right = (Sizes.SNAKE_BLOCK, 0)

    # sets the desired directions for finding the grapes
    if x > goal_x:
        desired_x = left
    elif x < goal_x:
        desired_x = right
    else:
        desired_x = right
    if y > goal_y:
        desired_y = up
    elif y < goal_y:
        desired_y = down
    else:
        desired_y = down

    # oob = out of bounds
    # defaults all oob values to false
    oob_up = False
    oob_down = False
    oob_left = False
    oob_right = False

    # Checks if the snake is on the edge,
    # if it does sets the oob for that side to true
    if x == Sizes.SCREEN_WIDTH - Sizes.SNAKE_BLOCK:
        oob_right = True

    if x < 20:
        oob_left = True

    if y == Sizes.SCREEN_HEIGHT - Sizes.SNAKE_BLOCK:
        oob_down = True

    if y < 20: 

        oob_up = True
    
    if oob_right:
        if cur_dir == SnakeDirections.RIGHT:
            # if going right and in the right lower corner
            # moves it up (only option)
            if oob_down: 
                return up
            # if going right and in the right upper corner
            elif oob_up:
                return down
            # checks if going up will send snake into another snake
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.UP):
                return down
            # checks if going down will send snake into another snake
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.DOWN):
                return up
            # otherwise tries to go towards grape
            else:
                return desired_y
        
    
    if oob_left:
        print(cur_dir)
        if cur_dir == SnakeDirections.LEFT:
            # if going left and in the left lower corner
            # moves it up (only maybe safe option)
            if oob_down:
                return up
            # if going left and in the left upper corner
            elif oob_up:
                return down
            # checks if going up will send snake into another snake
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.UP):
                return down
            # checks if going down will send snake into another snake
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.DOWN):
                return up
            # otherwise tries to go towards grape
            else:
                return desired_y
        
    if oob_up:
        if cur_dir == SnakeDirections.UP:
            # if going up and in the right upper corner
            if oob_right:
                return left
            # if going up and in the left upper corner
            elif oob_left:
                return right
            # checks if going left will send snake into another snake
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.LEFT):
                return right
            # checks if going right will send snake into another snake
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.RIGHT):
                return left
            # otherwise tries to go towards grape
            else:
                return desired_x
            
    if oob_down:
        if cur_dir == SnakeDirections.DOWN:
            # if going down and in the right lower corner
            if oob_right:
                return left
            # if going down and in the left lower corner
            elif oob_left:
                return right
            # checks if going left will send snake into another snake
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.LEFT):
                return right
            # checks if going right will send snake into another snake
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.RIGHT):
                return left
            # otherwise tries to go towards grape
            else:
                return desired_x
           
    # checks if the snakes current course will send it out of bounds
    if check_collison_course(opp_snake, my_snake, x, y, cur_dir):
        # if the snake is going up or down, decides whether to go left or right
        if cur_dir == SnakeDirections.UP or cur_dir == SnakeDirections.DOWN:
            # makes sure direction change doesn't send snake out of bounds
            if oob_left:
                return right
            elif oob_right:
                return left
            # checks if going left will send snake into another snake
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.LEFT):
                return right
            # checks if going right will send snake into another snake
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.RIGHT):
                return left
            # otherwise tries to go towards grape
            else:
                return desired_x
            
        # if the snake is going left or right, decides whether to go up or down
        elif cur_dir == SnakeDirections.LEFT or cur_dir == SnakeDirections.RIGHT:
            # makes sure direction change doesn't send snake out of bounds
            if oob_down:
                return up
            elif oob_up:
                return down
            # checks if going up will send snake into a snake
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.UP):
                return down
            # checks if going down will send snake into a snake
            elif check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.DOWN):
                return up
            # otherwise tries to go towards grape
            else:
                return desired_y

    # sees if changing direction will get the snake closer to grape
    if cur_dir == SnakeDirections.UP or cur_dir == SnakeDirections.DOWN:
        if x > goal_x:
            if not check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.LEFT) and not oob_left:
                return left
        elif x < goal_x:
            if not check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.RIGHT) and not oob_right:
                return right
    if cur_dir == SnakeDirections.LEFT or cur_dir == SnakeDirections.RIGHT:
        if y > goal_y:
            if not check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.UP) and not oob_up:
                return up
        elif y < goal_y:
            if not check_collison_course(opp_snake, my_snake, x, y, SnakeDirections.DOWN) and not oob_down:
                return down
    
    # if not in danger and no direction change, returns 0, 0
    return (0, 0)
