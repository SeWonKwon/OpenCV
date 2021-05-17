import cv2

def mousePoints(event,x,y,flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)


img = cv2.imread('Resources/book.PNG')
cv2.imshow("img",img)
cv2.setMouseCallback("img", mousePoints)

cv2.waitKey(0)