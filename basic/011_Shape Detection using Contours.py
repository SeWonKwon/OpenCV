import cv2
import numpy as np
from doumi.helpfunc import stackImages

def empty():
    pass

def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Area", "Parameters") # 최소 면적을 설정해서 그 이상만 찾는다.

        if area > areaMin:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 5)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5)
            cv2.putText(imgContour, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 255, 0), 2)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 255, 0), 2)

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 20, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 23, 255, empty)
cv2.createTrackbar("Area", "Parameters", 1000, 30000, empty)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    imgContour = img
    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    getContours(imgDil, imgContour)

    imgstack = stackImages(0.8, ([img, imgGray, imgCanny], [imgDil, imgDil, imgDil]))
    cv2.imshow("Result", imgstack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()