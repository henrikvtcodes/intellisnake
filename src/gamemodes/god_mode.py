import pygame
from pygame.locals import *
from food import *
from constants import (
    Colors,
    GameEndStates,
    GameModes,
    GameWindowStates,
    Sizes,
    SNAKE_SPEED,
    MAX_SCORE,
)
import init as globals
from draw_fns import draw_snake, draw_message, draw_score, draw_background_god
from images import *
from sounds import *


def start_god_mode():
    if globals.GameStateContainer.escape_pressed:
        globals.GameStateContainer.window_state = GameWindowStates.START
        globals.GameStateContainer.escape_pressed = False
        print("Autoavoid Race Condition: Classic Mode Start Aborted")
        return
    # sets the window state to playing
    # the next time the main loop, well, loops, it will run the function for the gamemode.
    globals.GameStateContainer.window_state = GameWindowStates.PLAYING
    globals.GameStateContainer.game_mode = GameModes.GOD


# The main game outline is here. We could make
# other functions for other gamemodes.
def god_mode():
    # Generates our current only snakes starting
    # pos.
    snake_x1 = Sizes.SCREEN_WIDTH / 2
    snake_y1 = Sizes.SCREEN_HEIGHT / 2

    snake_x1 -= snake_x1 % Sizes.SNAKE_BLOCK
    snake_y1 -= snake_y1 % Sizes.SNAKE_BLOCK

    # This is what decides how far the snake
    # moves.
    x1_change = 0
    y1_change = 0

    speed = SNAKE_SPEED
    direction = "right"

    snake_list = []
    snake_length = 1

    # generates a starting apple position.
    food_x, food_y = gen_food_position(Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT, [], [])
    num_food = 1
    food_list = []
    food_list.append([food_x, food_y])
    left1 = pygame.K_LEFT
    left2 = pygame.K_a
    right1 = pygame.K_RIGHT
    right2 = pygame.K_d
    up1 = pygame.K_UP
    up2 = pygame.K_w
    down1 = pygame.K_DOWN
    down2 = pygame.K_s

    up = "up"
    down = "down"
    left = "left"
    right = "right"

    # continues as long as the game isn't over.
    # yeah.
    while globals.GameStateContainer.window_state == GameWindowStates.PLAYING:
        # if the user clicks or presses a key
        # that does something, that is read here.
        # If they quit, it ends the program, if they
        # hit one of the arrow or wasd keys it sets the
        # direction change.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                globals.GameStateContainer.window_state = GameWindowStates.EXIT

            if event.type == pygame.KEYDOWN:
                if event.key == left1 or event.key == left2:
                    if not direction == right:
                        x1_change = -Sizes.SNAKE_BLOCK
                        y1_change = 0
                        direction = left
                        break
                elif event.key == right1 or event.key == right2:
                    if not direction == left:
                        x1_change = Sizes.SNAKE_BLOCK
                        y1_change = 0
                        direction = right
                        break
                elif event.key == up1 or event.key == up2:
                    if not direction == down:
                        x1_change = 0
                        y1_change = -Sizes.SNAKE_BLOCK
                        direction = up
                        break
                elif event.key == down1 or event.key == down2:
                    if not direction == up:
                        x1_change = 0
                        y1_change = Sizes.SNAKE_BLOCK
                        direction = down

        # checks to see if the board is full
        if snake_length == MAX_SCORE:
            pygame.mixer.Sound.play(win)
            globals.GameStateContainer.end_state = GameEndStates.CLASSIC_WIN
            globals.GameStateContainer.window_state = GameWindowStates.END

        # checks if the snake is out of bounds
        if (
            snake_x1 == Sizes.SCREEN_WIDTH
            or snake_x1 < 0
            or snake_y1 == Sizes.SCREEN_HEIGHT
            or snake_y1 < 0
        ):
            pygame.mixer.Sound.play(willhelm)
            globals.GameStateContainer.end_state = GameEndStates.CLASSIC_LOSE
            globals.GameStateContainer.window_state = GameWindowStates.END

        # changes the snake positions
        snake_x1 += x1_change
        snake_y1 += y1_change

        # draws the background and food
        globals.window.fill(Colors.BACKGROUND_GOD)
        draw_background_god()

        for b in food_list:
            globals.window.blit(grape_image, (b[0], b[1]))

        # creates a list for the snake head
        # and appends that list to the list containg
        # the whole snake
        snake_head = (snake_x1, snake_y1)
        snake_list.append(snake_head)

        # deletes the snakes tail so it isn't
        # growing infinitely
        if not len(snake_list) == snake_length:
            del snake_list[0]

        # checks to see if the snake has hit
        # itself, ends the game if it has
        for x in snake_list[:-1]:
            if tuple(x) == snake_head:
                pygame.mixer.Sound.play(bonk)
                globals.GameStateContainer.end_state = GameEndStates.CLASSIC_LOSE
                globals.GameStateContainer.window_state = GameWindowStates.END

        # draws the snake.
        draw_snake(Sizes.SNAKE_BLOCK, Colors.SNAKE, snake_list, direction, snake_length)

        # shows every thing
        pygame.display.update()

        # if the snake has the food, generates
        # a new food positon and grows the snake
        for i in food_list:
            if snake_x1 == i[0] and snake_y1 == i[1]:
                pygame.mixer.Sound.play(mlem)
                i[0], i[1] = gen_food_position(
                    Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT, snake_list, []
                )
                snake_length += 1

                gods_choice = random.randint(0, 2)
                # doubles speed
                if gods_choice == 0:
                    speed = speed * 2
                # adds another grape
                elif gods_choice == 1:
                    num_food += 1
                    plchldr_x, plchldr_y = gen_food_position(
                    Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT, snake_list, []
                    )
                    food_list.append([plchldr_x, plchldr_y])
                # inverts controls
                else:
                    #plchldr_dir = left
                    #left = right
                    #right = plchldr_dir
                    #plchldr_dir = up
                    #up = down
                    #down = plchldr_dir

                    plchldr_dir = left1
                    left1 = right1
                    right1 = plchldr_dir
                    plchldr_dir = up1
                    up1 = down1
                    down1 = plchldr_dir

                    plchldr_dir = left2
                    left2 = right2
                    right2 = plchldr_dir
                    plchldr_dir = up2
                    up2 = down2
                    down2 = plchldr_dir
                    print(f"up: {up} down: {down} left: {left} right: {right}")

        # makes time pass.
        globals.clock.tick(speed)
