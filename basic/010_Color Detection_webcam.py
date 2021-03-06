

import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)

cap.set(3, frameWidth)
cap.set(4, frameHeight)
def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",30,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",66,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",58,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",129,255,empty)
cv2.createTrackbar("Val Min","TrackBars",179,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    _, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img,img, mask = mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hstack = np.hstack([img, mask, result])
    print(lower)
    print(upper)


    # cv2.imshow('Original',img)
    # cv2.imshow('HSV Color Space', imgHsv)
    # cv2.imshow('Mask',mask)
    # cv2.imshow('Result',result)
    cv2.imshow('Horizontal Stacking',hstack)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
