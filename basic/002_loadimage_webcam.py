import cv2
# import numpy as np


# img = cv2.imread("./Resources/cat2.jpg")
#
# cv2.imshow("cat", img)
# cv2.waitKey(2000) # 1000은 1초
#

frameWidth = 640
frameHeight = 480

# cap = cv2.VideoCapture("./Resources/Airport.mp4")
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

while(True):

    success, img = cap.read()
    img = cv2.resize(img,(frameWidth,frameHeight))
    cv2.imshow("Video",img)
    # print(success)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



