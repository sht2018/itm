# -*- coding: utf-8 -*-
import cv2
import numpy as np
import urllib.request

img=np.zeros((300,159,3), np.uint8)

while(1):

    response = urllib.request.urlopen('http://192.168.77.128/number.html')

    people_number = int(response.read().decode('utf-8'))

    for i in range(3):

        for j in range(3):

            # cv2.rectangle(img,(3+50*i,64+50*j),(53+50*i,114+50*j),(255,255,255),2)

            if (i+j)%2 == 0:
                cv2.rectangle(img,(3+50*j,64+50*i),(53+50*j,114+50*i),(0,0,0),-1)

            if people_number > 0:
                cv2.circle(img,(28+50*j,89+50*i),20,(255,255,255),-1)
                if (i+j)%2 == 0:
                    people_number -= 1

            if (i+j)%2 == 1:
                cv2.rectangle(img,(3+50*j,64+50*i),(53+50*j,114+50*i),(255,255,255),-1)
                if people_number > 0:
                    cv2.circle(img,(28+50*j,89+50*i),20,(0,0,0),-1)
                    people_number -= 1
    # hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    cv2.imshow('img',img)
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break

cv2.destroyAllWindows()

