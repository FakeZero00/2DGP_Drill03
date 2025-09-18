#2022182034 임성진
from pico2d import *
import math

if __name__ == '__main__':
    open_canvas()

    grass = load_image('grass.png')
    character = load_image('character.png')

    # 사각형 경로 좌표
    rect_points = [(50, 90), (750, 90), (750, 510), (50, 510)]
    rect_index = 0

    # 삼각형 경로 좌표
    tri_points = [(400, 510), (750, 90), (50, 90)]
    tri_index = 0

    # 원 경로 정보
    circle_center = (400, 300)
    circle_radius = 210
    circle_angle = 0
    start_circle_angle = 0 # 원 운동 시작 각도 저장

    # 상태: 0=사각형, 1=삼각형, 2=원
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
            if dist < 5:
                x, y = nx, ny
                rect_index = next_index
                if rect_index == 0:
                    state = 1
                    tri_index = 0
                    x, y = tri_points[0] # 삼각형 시작점으로 이동
                continue
            x += dx / dist * 5
            y += dy / dist * 5

        elif state == 1:  # 삼각형 운동
            next_index = (tri_index + 1) % 3
            nx, ny = tri_points[next_index]
            dx, dy = nx - x, ny - y
            dist = math.hypot(dx, dy)
            if dist < 5:
                x, y = nx, ny
                tri_index = next_index
                if tri_index == 0:
                    state = 2
                    dx = x - circle_center[0]
                    dy = y - circle_center[1]
                    start_circle_angle = math.atan2(dy, dx)
                    if start_circle_angle < 0:
                        start_circle_angle += 2 * math.pi
                    circle_angle = start_circle_angle
                continue
            x += dx / dist * 5
            y += dy / dist * 5

        elif state == 2:  # 원 운동
            circle_angle += 0.03
            # 한 바퀴를 다 돌았는지 체크
            if abs(circle_angle - (start_circle_angle + 2 * math.pi)) < 0.03:
                state = 0
                rect_index = 0
                x, y = rect_points[0] # 사각형 시작점으로 이동
                continue
            x = circle_center[0] + circle_radius * math.cos(circle_angle)
            y = circle_center[1] + circle_radius * math.sin(circle_angle)

    close_canvas()