from typing import List, Tuple
from constants import DIRECTION_VALUES


# This class represents a snake
class Snake():
    __snake_pos__ = []
    # Valid values: left, right, up, down
    __current_direction__ = "right"
    x_bound = -1
    y_bound = -1

    def __init__(self, start_x: int, start_y: int, x_bound: int, y_bound: int):
        initial_pos = (start_x, start_y)
        self.__snake_pos__.append(initial_pos)

        self.x_bound = x_bound
        self.y_bound = y_bound

    def advance(self):
        return 0;

    def change_direction(self, new_direction):
        if new_direction not in DIRECTION_VALUES:
            raise ValueError(f"{new_direction} is not a valid direction value. "
                             f"Valid values are {DIRECTION_VALUES}")

        self.__current_direction__ = new_direction


class Player:
    x = 10
    y = 10
    speed = 1

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed
