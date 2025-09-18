from pico2d import *
import math



def square_move(character):
    x = 400
    y = 90
    move_direction('right', 380)
    move_direction('up', 470)
    move_direction('left', 760)
    move_direction('down', 470)
    move_direction('right', 380)

def circle_move():
    pass


if __name__ == '__main__':
    open_canvas()

    grass = load_image('grass.png')
    character = load_image('character.png')

    while True:
        clear_canvas_now()
        grass.draw_now(400, 30) #배경 그리기


        square_move()
        circle_move()
        pass

    close_canvas()