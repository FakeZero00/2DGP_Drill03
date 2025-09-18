from pico2d import *
import math



if __name__ == '__main__':
    open_canvas()

    grass = load_image('grass.png')
    character = load_image('character.png')

    # 사각형 경로 좌표
    rect_points = [(50, 90), (750, 90), (750, 510), (50, 510)]
    rect_index = 0

    # 원 경로 정보
    circle_center = (400, 300)
    circle_radius = 210
    circle_angle = 0

    # 상태: 0=사각형, 1=원
    state = 0

    x, y = rect_points[0]

    while True:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        update_canvas()
        delay(0.01)
        get_events()

        if state == 0:  # 사각형 운동
            next_index = (rect_index + 1) % 4
            nx, ny = rect_points[next_index]
            dx, dy = nx - x, ny - y
            dist = math.hypot(dx, dy)
            if dist < 1:
                rect_index = next_index
                if rect_index == 0:
                    state = 1  # 사각형 끝나면 원 운동으로 전환
                    circle_angle = 0
                continue
            x += dx / dist * 5
            y += dy / dist * 5

        elif state == 1:  # 원 운동
            circle_angle += 0.03
            if circle_angle > 2 * math.pi:
                circle_angle = 0
                state = 0  # 원 운동 끝나면 사각형 운동으로 전환
                x, y = rect_points[0]
                rect_index = 0
                continue
            x = circle_center[0] + circle_radius * math.cos(circle_angle)
            y = circle_center[1] + circle_radius * math.sin(circle_angle)

    close_canvas()