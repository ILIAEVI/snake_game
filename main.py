from pyray import *
from raylib import *
import random

init_window(800, 800, "Snake Game")
set_target_fps(10)
apple = load_texture('images/apple.png')

SIZE = 50

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
    for i in range(16):
        for j in range(16):
            if (i + j) % 2 == 0:
                draw_rectangle(i * SIZE, j * SIZE, SIZE, SIZE, DARK_GREEN_TILE)
            else:
                draw_rectangle(i * SIZE, j * SIZE, SIZE, SIZE, DARK_GRAY_TILE)


class Snake:

    def __init__(self):
        self.body = [[2, 0], [1, 0], [0, 0]]  # Initial Position
        self.direction = DIR_RIGHT  # Initial direction (->)

    def move(self):
        # calculate new head
        head = [self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1]]
        # check if snake is out of the bound
        head = [head[0] % 16, head[1] % 16]
        # insert head in body and remove last part of the tail
        self.body.insert(0, head)
        self.body.pop()

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def eat_food(self):
        if self.body[0][0] == food_position[0] and self.body[0][1] == food_position[1]:
            new_head = [self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1]]
            self.body.insert(0, new_head)
            return True
        return False

    def detect_collision(self):
        for i in range(1, len(self.body)):
            if self.body[0][0] == self.body[i][0] and self.body[0][1] == self.body[i][1]:
                return True
        return False


snake = Snake()
food_position = (5, 5)

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
        new_position = (random.randint(0, 15), random.randint(0, 15))

        while new_position in snake.body:
            new_position = (random.randint(0, 15), random.randint(0, 15))

        food_position = new_position

    begin_drawing()
    clear_background(WHITE)
    draw_board()

    draw_texture_pro(apple, Rectangle(0, 0, apple.width, apple.height),Rectangle(food_position[0] * SIZE, food_position[1] * SIZE, SIZE , SIZE), Vector2(0,0), 0, WHITE)

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
