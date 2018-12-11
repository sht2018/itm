import sys
import numpy as np
import cv2
import time
import os
from urllib import request

img=np.zeros((512,512,3), np.uint8)
L=512
W=512

print(L,W)

SIZE=100

X0=int(W/2-1.5*SIZE)
Y0=int(L/2-1.5*SIZE)



while(True):
    number = 0
    with request.urlopen('http://192.168.112.128/number.html') as f:
        number = int(f.read())
        print('number ', number)
    n = 1
    cv2.rectangle(img,(0,0),(W,L),(0,0,0),-1)
    for j in range(3):
        for i in range(3):
            if (n <= number):
                cv2.rectangle(img,(i*SIZE+X0,j*SIZE+Y0),(i*SIZE+SIZE+X0,j*SIZE+SIZE+Y0),(255,255,255),-1)
            cv2.rectangle(img,(i*SIZE+X0,j*SIZE+Y0),(i*SIZE+SIZE+X0,j*SIZE+SIZE+Y0),(0,0,0),5)
            n += 1
    
    cv2.imshow('img',img)
    if cv2.waitKey(100)&0xFF==ord('q'):
        break
cv2.destroyAllWindows()