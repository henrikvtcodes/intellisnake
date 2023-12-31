import pygame
from pygame.locals import *
from food import gen_food_position
from constants import (
    Colors,
    GameEndStates,
    GameModes,
    GameWindowStates,
    Sizes,
    SNAKE_SPEED,
)
from images import *
from sounds import *

import init as globals

from draw_fns import draw_snake, draw_background


def start_pvp():
    if globals.GameStateContainer.escape_pressed:
        globals.GameStateContainer.window_state = GameWindowStates.START
        globals.GameStateContainer.escape_pressed = False
        print("Autoavoid Race Condition: PvP Mode Start Aborted")
        return
    # sets the window state to playing
    # the next time the main loop, well, loops, it will run the function for the gamemode.
    globals.GameStateContainer.window_state = GameWindowStates.PLAYING
    globals.GameStateContainer.game_mode = GameModes.PVP


# loop for playing pvp mode
def pvp_mode():
    blue_lose = False
    green_lose = False

    # Generates starting position of both
    # snakes.
    snake_x1 = Sizes.SCREEN_WIDTH / 2
    snake_y1 = Sizes.SCREEN_HEIGHT / 2
    snake_x2 = Sizes.SCREEN_WIDTH / 2 - 2 * Sizes.SNAKE_BLOCK
    snake_y2 = Sizes.SCREEN_HEIGHT / 2

    snake_x1 -= snake_x1 % Sizes.SNAKE_BLOCK
    snake_y1 -= snake_y1 % Sizes.SNAKE_BLOCK
    snake_x2 -= snake_x2 % Sizes.SNAKE_BLOCK
    snake_y2 -= snake_y2 % Sizes.SNAKE_BLOCK

    # This is what decides how far the snakes
    # move.
    x1_change = 0
    y1_change = 0
    x2_change = 0
    y2_change = 0

    snake_list_1 = []
    snake_length_1 = 1
    snake_list_2 = []
    snake_length_2 = 1

    direction_blue = "right"
    direction_green = "right"

    # generates a starting apple position.
    food_x, food_y = gen_food_position(Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT, [], [])

    # continues as long as the game isn't over.
    # yeah.
    while globals.GameStateContainer.window_state == GameWindowStates.PLAYING:
        # if the user clicks or presses a key
        # that does something, that is read here.
        # If they quit, it ends the program, if they
        # hit one of the arrow or wasd keys it sets the
        # direction change.
        # player one or blue snake is arrows, player
        # 2 or green snake is wasd.
        p1_has_moved = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                globals.GameStateContainer.window_state = GameWindowStates.EXIT

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not x1_change == Sizes.SNAKE_BLOCK and not p1_has_moved:
                        x1_change = -Sizes.SNAKE_BLOCK
                        y1_change = 0
                        direction_blue = "left"
                        p1_has_moved = True
                if event.key == pygame.K_RIGHT:
                    if not x1_change == -Sizes.SNAKE_BLOCK and not p1_has_moved:
                        x1_change = Sizes.SNAKE_BLOCK
                        y1_change = 0
                        direction_blue = "right"
                        p1_has_moved = True
                if event.key == pygame.K_UP:
                    if not y1_change == Sizes.SNAKE_BLOCK and not p1_has_moved:
                        x1_change = 0
                        y1_change = -Sizes.SNAKE_BLOCK
                        direction_blue = "up"
                        p1_has_moved = True
                if event.key == pygame.K_DOWN:
                    if not y1_change == -Sizes.SNAKE_BLOCK and not p1_has_moved:
                        x1_change = 0
                        y1_change = Sizes.SNAKE_BLOCK
                        direction_blue = "down"
                        p1_has_moved = True
                if event.key == pygame.K_a:
                    if not x2_change == Sizes.SNAKE_BLOCK:
                        x2_change = -Sizes.SNAKE_BLOCK
                        y2_change = 0
                        direction_green = "left"
                        break
                if event.key == pygame.K_d:
                    if not x2_change == -Sizes.SNAKE_BLOCK:
                        x2_change = Sizes.SNAKE_BLOCK
                        y2_change = 0
                        direction_green = "right"
                        break
                if event.key == pygame.K_w:
                    if not y2_change == Sizes.SNAKE_BLOCK:
                        x2_change = 0
                        y2_change = -Sizes.SNAKE_BLOCK
                        direction_green = "up"
                        break
                if event.key == pygame.K_s:
                    if not y2_change == -Sizes.SNAKE_BLOCK:
                        x2_change = 0
                        y2_change = Sizes.SNAKE_BLOCK
                        direction_green = "down"

        # checks if the p1 snake is out of bounds.
        # assigns win to green if true.
        if (
            snake_x1 == Sizes.SCREEN_WIDTH
            or snake_x1 < 0
            or snake_y1 == Sizes.SCREEN_HEIGHT
            or snake_y1 < 0
        ):
            print("Out of bounds")
            pygame.mixer.Sound.play(willhelm)
            blue_lose = True
            globals.GameStateContainer.end_state = GameEndStates.P1_LOSE
            globals.GameStateContainer.window_state = GameWindowStates.END

        # checks if the p2 snake is out of bounds.
        # removes win from p1 if both are true, gives
        # win to p2 if only this is true.
        if (
            snake_x2 == Sizes.SCREEN_WIDTH
            or snake_x2 < 0
            or snake_y2 == Sizes.SCREEN_HEIGHT
            or snake_y2 < 0
        ):
            print(snake_x2, snake_y2)
            if blue_lose == True:
                globals.GameStateContainer.end_state = GameEndStates.BOTH_LOSE
                pygame.mixer.Sound.play(willhelm)
            else:
                globals.GameStateContainer.end_state = GameEndStates.P2_LOSE
                pygame.mixer.Sound.play(willhelm)

            globals.GameStateContainer.window_state = GameWindowStates.END

        # changes the snake positions
        snake_x1 += x1_change
        snake_y1 += y1_change
        snake_x2 += x2_change
        snake_y2 += y2_change

        # draws the background and food
        globals.window.fill(Colors.BACKGROUND)
        draw_background()
        globals.window.blit(grape_image, (food_x, food_y))

        # creates a list for the snake head
        # and appends that list to the list containg
        # the whole snake
        snake_head_1 = []
        snake_head_1.append(snake_x1)
        snake_head_1.append(snake_y1)
        snake_list_1.append(snake_head_1)

        snake_head_2 = []
        snake_head_2.append(snake_x2)
        snake_head_2.append(snake_y2)
        snake_list_2.append(snake_head_2)

        # deletes the snakes tail so it isn't
        # growing infinitely
        if not len(snake_list_1) == snake_length_1:
            del snake_list_1[0]

        if not len(snake_list_2) == snake_length_2:
            del snake_list_2[0]

        # checks to see if the snake has hit
        # itself, ends the game if it has
        for x in snake_list_1[:-1]:
            if x == snake_head_1:
                print("Hit self")
                pygame.mixer.Sound.play(bonk)
                blue_lose = True
                globals.GameStateContainer.end_state = GameEndStates.P1_LOSE
                globals.GameStateContainer.window_state = GameWindowStates.END

        for x in snake_list_2[:-1]:
            if x == snake_head_2:
                print("Hit self")
                if blue_lose == True:
                    pygame.mixer.Sound.play(bonk)
                    globals.GameStateContainer.end_state = GameEndStates.BOTH_LOSE
                else:
                    pygame.mixer.Sound.play(bonk)
                    globals.GameStateContainer.end_state = GameEndStates.P2_LOSE

                globals.GameStateContainer.window_state = GameWindowStates.END

        # checks to see if p2 ran into p1
        for i in snake_list_1[:-1]:
            if i == snake_head_2:
                print("collided with other player")
                pygame.mixer.Sound.play(bonk)
                green_lose = True
                globals.GameStateContainer.end_state = GameEndStates.P2_LOSE
                globals.GameStateContainer.window_state = GameWindowStates.END

        # checks to see if p1 ran into p2
        for i in snake_list_2[:-1]:
            if i == snake_head_1:
                print("Collided with other player")
                if green_lose == True:
                    pygame.mixer.Sound.play(bonk)
                    globals.GameStateContainer.end_state = GameEndStates.BOTH_LOSE
                else:
                    pygame.mixer.Sound.play(bonk)
                    globals.GameStateContainer.end_state = GameEndStates.P1_LOSE
                globals.GameStateContainer.window_state = GameWindowStates.END

            # checks to see if they bonked heads.
            # if they have, sets both to having lost
            if snake_head_1 == snake_head_2:
                print("Head to head")
                pygame.mixer.Sound.play(bonk)
                globals.GameStateContainer.end_state = GameEndStates.BOTH_LOSE
                globals.GameStateContainer.window_state = GameWindowStates.END

        # draws both snakes
        draw_snake(
            Sizes.SNAKE_BLOCK,
            Colors.SNAKE,
            snake_list_1,
            direction_blue,
            snake_length_1,
        )
        draw_snake(
            Sizes.SNAKE_BLOCK,
            Colors.GREENISH,
            snake_list_2,
            direction_green,
            snake_length_2,
        )

        # shows every thing
        pygame.display.update()

        # if the snake has the food, generates
        # a new food positon and grows the snake
        if snake_x1 == food_x and snake_y1 == food_y:
            pygame.mixer.Sound.play(mlem)
            food_x, food_y = gen_food_position(
                Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT, snake_list_1, snake_list_2
            )
            snake_length_1 += 1
        elif snake_x2 == food_x and snake_y2 == food_y:
            pygame.mixer.Sound.play(mlem)
            food_x, food_y = gen_food_position(
                Sizes.SCREEN_WIDTH, Sizes.SCREEN_HEIGHT, snake_list_1, snake_list_2
            )
            snake_length_2 += 1

        # makes time pass.
        globals.clock.tick(SNAKE_SPEED)
