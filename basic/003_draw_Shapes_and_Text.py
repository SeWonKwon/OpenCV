import cv2

import numpy as np

img = np.zeros((512,512,3), np.uint8)

# img[250:,250:,:] = 255,0,0 # blue
# img2 = np.zeros((512,512,3), np.uint8)
# img2[:] = 0,0,255 # Red
# cv2.imshow("Image", img)
# cv2.imshow("Image2", img2)

# img 시작점
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)

# img 왼쪽위 상자, 오른쪽 아래 상자
cv2.rectangle(img,(350,100),(450,200),(0,0,255),2)
cv2.rectangle(img,(360,110),(430,180),(0,255,255),cv2.FILLED)

# img 중심, 반지름
cv2.circle(img, (100,360),40,(255,0,0),3)

# img str 시작점 폰트, 크기, 색, 두깨
cv2.putText(img,"Drawing Shaping Practice",(75,50),cv2.FONT_HERSHEY_SIMPLEX,1,(111,111,111),2)
cv2.imshow("Canvas",img)
cv2.waitKey(4000)