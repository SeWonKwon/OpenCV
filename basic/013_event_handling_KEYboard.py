# https://velog.io/@bangsy/Python-OpenCV-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EC%B2%98%EB%A6%AC

import numpy as np
import cv2

width, height = 512, 512
x, y, R = 256, 256, 50
direction = 0  # right

while True:
    # waitKey(키 입력 대기시간, ms)
    # 리턴값은 키보드로 입력한 키값의 아스키 코드
    key = cv2.waitKey(30)
    if key == 0x1B:
        break;

    # 방향키 방향전환
    elif key == ord(';'):  # right
        direction = 0
    # elif key == 0x280000:  # down
    elif key == ord('l'):
        direction = 1
    elif key == ord('k'):  # left
        direction = 2
    elif key == ord('o'):  # up
        direction = 3

    # 방향으로 이동
    if direction == 0:  # right
        x += 10
    elif direction == 1:  # down
        y += 10
    elif direction == 2:  # left
        x -= 10
    else:  # 3, up
        y -= 10

    #   경계확인
    if x < R:
        x = R
        direction = 0
    if x > width - R:
        x = width - R
        direction = 2
    if y < R:
        y = R
        direction = 1
    if y > height - R:
        y = height - R
        direction = 3

    # 지우고, 그리기
    img = np.zeros((width, height, 3), np.uint8) + 255  # 지우기
    cv2.circle(img, (x, y), R, (0, 0, 255), -1)
    cv2.imshow('img', img)

cv2.destroyAllWindows()