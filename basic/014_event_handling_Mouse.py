# https://velog.io/@bangsy/Python-OpenCV-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EC%B2%98%EB%A6%AC
import numpy as np
import cv2


# 마우스 입력 값에 따라 어떤 동작을 실행할 것인지 지정하는 함수
# event : 마우스 이벤트 타입
# x, y : 마우스 이벤트의 x, y좌표
# flags : 마우스 이벤트가 발생할 때 키보드 또는 마우스 상태
# param : 콜백 함수에 전달된 데이터(마우스 이벤트)
def onMouse(event, x, y, flags, param):
    ##    global img

    # 마우스 왼쪽 버튼을 누른 경우
    if event == cv2.EVENT_LBUTTONDOWN:
        # Shift 키를 누른 경우
        if flags & cv2.EVENT_FLAG_SHIFTKEY:
            cv2.rectangle(param[0], (x - 5, y - 5), (x + 5, y + 5), (255, 0, 0))  # 파란 사각형 그리기
        else:
            cv2.circle(param[0], (x, y), 5, (255, 0, 0), 3)  # 파란 원 그리기

    # 마우스 오른쪽 버튼을 누른 경우
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(param[0], (x, y), 5, (0, 0, 255), 3)  # 빨간 원 그리기

    # 마우스 왼쪽 버튼을 더블클릭하는 경우
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        param[0] = np.zeros(param[0].shape, np.uint8) + 255

    cv2.imshow("img", param[0])


# 하얀 배경 생성
img = np.zeros((512, 512, 3), np.uint8) + 255

cv2.imshow('img', img)  # 이미지 보여주기

# img란 GUI창위에 onMouse란 콜백 함수를 이용하여, 데이터 전달하기
# [img] : onMouse란 콜백 함수에 전달할 데이터
# 마우스 이벤트가 입력되면 사전에 작성한 함수를 불러와서 작동
cv2.setMouseCallback('img', onMouse, [img])  # 마우스 콜백 함수
cv2.waitKey()
cv2.destroyAllWindows()