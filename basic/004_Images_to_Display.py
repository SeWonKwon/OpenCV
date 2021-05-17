import cv2
import numpy as np

img1 = cv2.imread('./Resources/dog3.jpg')
img2 = cv2.imread('./Resources/dog.jpg')

print(img1.shape,img2.shape)

# img1 = cv2.resize(img1, (0,0),None, 0.5, 0.5)
# img2 = cv2.resize(img2, (0,0), None, 0.5, 0.5)
img1 = cv2.resize(img1, (110,110),None)
img2 = cv2.resize(img2, (110,110), None)
hor = np.hstack((img1, img2))
ver = np.vstack((img1, img2))

cv2.imshow('Vertical',ver)
cv2.imshow('Horizontal',hor)

cv2.waitKey(0)