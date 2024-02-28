from pyray import *
from raylib import *
import random

init_window(1000, 1000, "Snake Game")
set_target_fps(10)

SIZE = 100

DARK_GREEN_TILE = (30, 47, 26, 255)
DARK_GRAY_TILE = (24, 24, 24, 255)
SNAKE_BODY_COLOR = (65, 153, 45, 255)
SNAKE_HEAD_COLOR = (232, 163, 73, 255)


DIR_UP = (0, -1)
DIR_DOWN = (0, 1)
DIR_LEFT = (-1, 0)
DIR_RIGHT = (1, 0)


game_over = False

def draw_board():
    for i in range(10):
        for j in range(10):
            if (i + j) % 2 == 0:
                draw_rectangle(i * SIZE, j * SIZE, SIZE, SIZE, DARK_GREEN_TILE)
            else:
                draw_rectangle(i * SIZE, j * SIZE, SIZE, SIZE, DARK_GRAY_TILE)


class Snake:

    def __init__(self):
        self.body = [[2, 0], [1, 0], [0, 0]]  # Initial Position
        self.direction = DIR_LEFT
        self.ops = [DIR_UP, DIR_RIGHT, DIR_RIGHT]

    def move(self):
        # check if snake is out of bound
        for i in range(len(self.body)):
            self.body[i][0] = (self.body[i][0] + self.ops[i][0]) % 10
            self.body[i][1] = (self.body[i][1] + self.ops[i][1]) % 10

        # Shift operation to right
        for i in range(len(self.ops) - 1, 0, -1):
            self.ops[i] = self.ops[i - 1]
        # Append new operation
        self.ops[0] = self.direction

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def eat_food(self):
        if self.body[0][0] == food_position[0] and self.body[0][1] == food_position[1]:
            new_head = [
                (self.body[0][0] + self.ops[0][0]) % 10,
                (self.body[0][1] + self.ops[0][1]) % 10,
            ]
            self.body.insert(0, new_head)
            self.ops.insert(0, self.direction)
            return True

        return False

    def detect_collision(self):
        for i in range(1, len(self.body)):
            if self.body[0][0] == self.body[i][0] and self.body[0][1] == self.body[i][1]:
                return True
        return False


snake = Snake()
food_position = (3, 3)

while not window_should_close():
    if game_over:
        begin_drawing()
        clear_background(WHITE)
        draw_text("Game Over, Snake is dead!", 100, 100, 30, RED)
        end_drawing()
        continue

    if is_key_down(KEY_RIGHT):
        snake.change_direction(DIR_RIGHT)
    elif is_key_down(KEY_LEFT):
        snake.change_direction(DIR_LEFT)
    elif is_key_down(KEY_UP):
        snake.change_direction(DIR_UP)
    elif is_key_down(KEY_DOWN):
        snake.change_direction(DIR_DOWN)

    snake.move()

    if snake.detect_collision():
        game_over = True

    if snake.eat_food():
        new_position = (random.randint(0, 9), random.randint(0, 9))

        while new_position in snake.body:
            new_position = (random.randint(0, 9), random.randint(0, 9))

        food_position = new_position

    begin_drawing()
    clear_background(WHITE)
    draw_board()

    draw_circle(
        (food_position[0] * SIZE) + SIZE // 2,
        (food_position[1] * SIZE) + SIZE // 2,
        SIZE // 2,
        RED,
    )

    for i in range(len(snake.body)):
        draw_rectangle(
            snake.body[i][0] * SIZE,
            snake.body[i][1] * SIZE,
            SIZE,
            SIZE,
            SNAKE_BODY_COLOR,
        )

    draw_rectangle(
        snake.body[0][0] * SIZE, snake.body[0][1] * SIZE, SIZE, SIZE, SNAKE_HEAD_COLOR
    )

    end_drawing()


close_window()
