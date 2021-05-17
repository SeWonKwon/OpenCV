import cv2
import numpy as np

kernel = np.ones((5,5), dtype=np.uint8)
# print(kernel)

path = "./Resources/dog3.jpg"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny100 = cv2.Canny(imgBlur,100,100)
imgCanny50 = cv2.Canny(imgBlur,50,50)
imgDilation = cv2.dilate(imgCanny100,kernel, iterations=1 )
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)

cv2.imshow("image",img)
cv2.imshow("gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny100",imgCanny100)
cv2.imshow("Canny50", imgCanny50)
cv2.imshow("Dilation",imgDilation)
cv2.imshow("Eroded",imgEroded)
cv2.waitKey(0)
# cv2.waitKey(2000) # 2초 사라짐