#importing libraries
import cv2 
import time
import numpy as np

cap=cv2.VideoCapture(0)
image = cv2.imread("bangkok.webp")
time.sleep(2)
bg=0

while True:
    ret,frame = cap.read()
    print(frame)
    frame = cv2.resize(frame,(640,480))
    image = cv2.resize(image,(640,480))
    ublack = np.array([104,153,70])
    lblack = np.array([30,30,0])
    mask = cv2.inRange(frame,lblack,ublack)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    f = frame-res
    f=np.where(f==0,image,f)
    cv2.imshow("video",frame)
    cv2.imshow("mask",f)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()