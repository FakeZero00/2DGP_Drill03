from pico2d import *
import math

char_x = 400
char_y = 90

def move_direction(character, wallpaper, direction, distance):
    global char_x
    global char_y

    for i in range(distance):
        clear_canvas_now()
        wallpaper.draw_now(400, 30)

        if direction == 'right':
            char_x += 1
        elif direction == 'left':
            char_x -= 1
        elif direction == 'up':
            char_y += 1
        elif direction == 'down':
            char_y -= 1

        character.draw_now(char_x, char_y)
        delay(0.001)



def square_move(character, wallpaper):
    move_direction(character, wallpaper, 'right', 380)
    move_direction(character, wallpaper, 'up', 470)
    move_direction(character, wallpaper, 'left', 760)
    move_direction(character, wallpaper, 'down', 470)
    move_direction(character, wallpaper, 'right', 380)

def circle_move():
    pass


if __name__ == '__main__':
    open_canvas()

    grass = load_image('grass.png')
    character = load_image('character.png')

    while True: #배경 그리기

        square_move(character, grass)
        #circle_move()
        pass

    close_canvas()