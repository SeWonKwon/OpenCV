import cv2

path = "Resources/cat3.jpg"
img = cv2.imread(path)
print(img.shape) # 525,525,3 (높이, 넓이, 3색), (height, width, BGR)

width, height = 310,210
imgResize = cv2.resize(img, (width,height))
print(imgResize.shape)

imgCropped = img[75:425,130:410,: ] # [height, width, BGR]// [top:bottom,left:right,BGR]
imgResizetoOriginal = cv2.resize(imgCropped,(img.shape[1],img.shape[0]))

cv2.imshow("Cat", img)
cv2.imshow("resize", imgResize)
cv2.imshow("Cropped", imgCropped)
cv2.imshow("Crop2Original", imgResizetoOriginal)

cv2.waitKey(4000)