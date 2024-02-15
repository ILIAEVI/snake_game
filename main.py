from pyray import *

init_window(800, 800, "Snake Game")
set_target_fps(60)

SIZE = 100
COLOR1 = Color(0, 97, 34, 245)
COLOR2 = Color(0, 87, 34, 245)

while not window_should_close():
    begin_drawing()
    clear_background(WHITE)

    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                draw_rectangle(i * SIZE, j * SIZE, SIZE, SIZE, COLOR1)
            else:
                draw_rectangle(i * SIZE, j * SIZE, SIZE, SIZE, COLOR2)

    end_drawing()

close_window()
