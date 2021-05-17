import cv2
import numpy as np
circles = np.zeros((4,2), np.int)
counter = 0
pts1= circles

def mousePoints(event,x,y,flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x,y
        counter += 1
        print(circles)

cv2.EVENT_LBUTTONDBLCLK
img = cv2.imread('Resources/cat3.jpg')

while True:

    if counter == 4:
        width, height = 250, 350
        pts1 = np.float32([circles[0], circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        imgOutput = cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow('Output Image', imgOutput)

    for x in range(4):
        cv2.circle(img, (int(pts1[x][0]), int(pts1[x][1])), 1, (0,0,255), cv2.FILLED)

    cv2.imshow("img",img)
    cv2.setMouseCallback("img", mousePoints)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


