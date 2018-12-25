import numpy as np
import cv2

cap=cv2.VideoCapture(0)
ret,frame = cap.read()

L=len(frame)
W=len(frame[0])

print(L,W)

SIZE=150

X0=int(W/2-1.5*SIZE)
Y0=int(L/2-1.5*SIZE)

while(True):
    ret,frame = cap.read()
    for i in range(3):
        for j in range(3):
            cv2.rectangle(frame,(i*int(W/3),j*int(L/3)),((i+1)*int(W/3),(j+1)*int(L/3)),(255,128,255),5)  
    cv2.imshow('frame',frame)
    if cv2.waitKey(1000)&0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
