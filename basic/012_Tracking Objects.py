import cv2

cap = cv2. VideoCapture(0)

tracker = cv2.legacy_TrackerMOSSE.create() # fast low accuracy
# tracker = cv2.legacy_TrackerCSRT.create() # slow good accuracy
success, img = cap.read()
bbox = cv2.selectROI("Tracking", img, False)
tracker.init(img, bbox)

def drawBox(img,bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]) ,int(bbox[3])
    cv2.rectangle(img, (x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img, 'Tracking', (75, 70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.7, (1, 255, 1), 2)



while True:
    timer = cv2.getTickCount()
    success, img = cap.read()

    success, bbox = tracker.update(img)

    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img, 'Lost', (75,70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX,0.7, (122,12,211),4)

    fps = cv2.getTickFrequency()/(cv2.getTickCount() - timer)
    cv2.putText(img,str(int(fps)), (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (122,12,211),4)
    cv2.imshow("Tracking", img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break



