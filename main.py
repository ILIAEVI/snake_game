from pyray import *
from raylib import *
import random

init_window(1000, 1000, "Snake Game")
set_target_fps(10)

SIZE = 100
COLOR1 = Color(0, 97, 34, 245)
COLOR2 = Color(0, 87, 34, 245)


class Snake:

    def __init__(self):
        self.body = [(2, 0), (1, 0), (0, 0)]  # Initial Position
        self.direction = (1, 0)  # Initial Direction, it moves right

    def move(self):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        head = (head[0] % 10, head[1] % 10)
        self.body.insert(0, head)
        if head in self.body[1:]:
            return False
        self.body.pop()
        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def eat_food(self, x):
        if self.body[0] == food.position:
            self.body.insert(0, (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1]))
            return True
        return False


class Food:
    def __init__(self):
        self.position = (3, 3)

    def spawn(self):
        self.position = (random.randrange(10), random.randrange(10))


snake = Snake()
food = Food()

while not window_should_close():
    begin_drawing()
    clear_background(WHITE)

    for i in range(10):
        for j in range(10):
            if (i+j) % 2 == 0:
                draw_rectangle(i * SIZE, j * SIZE, SIZE, SIZE, COLOR1)
            else:
                draw_rectangle(i * SIZE, j * SIZE, SIZE, SIZE, COLOR2)

    snake_alive = snake.move()
    if not snake_alive:
        draw_text("Game Over, Snake is dead!", 100, 100, 30, RED)
        break

    for body in snake.body:
        draw_rectangle(body[0]*SIZE, body[1]*SIZE, SIZE, SIZE, VIOLET)

    draw_circle((food.position[0]*SIZE) + SIZE//2, (food.position[1]*SIZE) + SIZE//2, SIZE//2, RED)
    if snake.eat_food(food.position):
        food.spawn()

    end_drawing()

    if is_key_down(KEY_RIGHT):
        snake.change_direction((1, 0))
    elif is_key_down(KEY_LEFT):
        snake.change_direction((-1, 0))
    elif is_key_down(KEY_UP):
        snake.change_direction((0, -1))
    elif is_key_down(KEY_DOWN):
        snake.change_direction((0, 1))

close_window()
