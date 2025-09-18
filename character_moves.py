from pico2d import *
import math


def square_move():
    pass


def circle_move():
    pass


if __name__ == '__main__':
    open_canvas()

    grass = load_image('grass.png')
    character = load_image('character.png')

    while True:
        square_move()
        circle_move()
        pass

    close_canvas()