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
        elif direction == 'left-up':
            char_x -= 1
            char_y += 1
        elif direction == 'left-down':
            char_x -= 1
            char_y -= 1

        character.draw_now(char_x, char_y)
        delay(0.001)



def square_move(character, wallpaper):
    move_direction(character, wallpaper, 'right', 380)
    move_direction(character, wallpaper, 'up', 470)
    move_direction(character, wallpaper, 'left', 760)
    move_direction(character, wallpaper, 'down', 470)
    move_direction(character, wallpaper, 'right', 380)

def circle_move(character, wallpaper, origin, radius):
    global char_x
    global char_y

    for deg in range(270, -90, -1):
        clear_canvas_now()
        wallpaper.draw_now(400, 30)

        char_x = origin[0] + radius * math.cos(math.radians(deg))
        char_y = origin[1] + radius * math.sin(math.radians(deg))

        character.draw_now(char_x, char_y)
        delay(0.001)

def triangle_move(character, wallpaper):
    move_direction(character, wallpaper, 'right', 380)
    move_direction(character, wallpaper, 'left-up', 380)
    move_direction(character, wallpaper, 'left-down', 380)
    move_direction(character, wallpaper, 'right', 380)


if __name__ == '__main__':
    open_canvas()

    grass = load_image('grass.png')
    character = load_image('character.png')

    while True: #배경 그리기

        square_move(character, grass)
        triangle_move(character, grass)
        circle_move(character, grass, (400, 300), 210)
        pass

    close_canvas()