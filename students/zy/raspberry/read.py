from mvnc import mvncapi as mvnc
import sys
import numpy as np
import cv2
import time
import os
import csv
import math
import csv

def handle_keys(raw_key):
    global GN_PROBABILITY_MIN, TY_MAX_IOU, TY_BOX_PROBABILITY_THRESHOLD, do_googlenet
    ascii_code = raw_key & 0xFF
    if ((ascii_code == ord('q')) or (ascii_code == ord('Q'))):
        return False
    elif (ascii_code == ord('B')):
        TY_BOX_PROBABILITY_THRESHOLD = TY_BOX_PROBABILITY_THRESHOLD + 0.05
        print("New TY_BOX_PROBABILITY_THRESHOLD is " + str(TY_BOX_PROBABILITY_THRESHOLD))
    elif (ascii_code == ord('b')):
        TY_BOX_PROBABILITY_THRESHOLD = TY_BOX_PROBABILITY_THRESHOLD - 0.05
        print("New TY_BOX_PROBABILITY_THRESHOLD is " + str(TY_BOX_PROBABILITY_THRESHOLD))
    elif (ascii_code == ord('G')):
        GN_PROBABILITY_MIN = GN_PROBABILITY_MIN + 0.05
        print("New GN_PROBABILITY_MIN is " + str(GN_PROBABILITY_MIN))
    elif (ascii_code == ord('g')):
        GN_PROBABILITY_MIN = GN_PROBABILITY_MIN - 0.05
        print("New GN_PROBABILITY_MIN is " + str(GN_PROBABILITY_MIN))
    elif (ascii_code == ord('I')):
        TY_MAX_IOU = TY_MAX_IOU + 0.05
        print("New TY_MAX_IOU is " + str(TY_MAX_IOU))
    elif (ascii_code == ord('i')):
        TY_MAX_IOU = TY_MAX_IOU - 0.05
        print("New TY_MAX_IOU is " + str(TY_MAX_IOU))
    elif (ascii_code == ord('2')):
        do_googlenet = not do_googlenet
        print("New do_googlenet is " + str(do_googlenet))

    return True

while True:
    while True :
        video_device = cv2.VideoCapture('/home/zy/tensorflow/ncappzoo/apps/street_cam/1213_1.jpg')
        ret_val, input_image = video_device.read()
        print(type(input_image))
        csv_reader = csv.reader(open("data.csv"))
        for row in csv_reader:
            for i in range(0,9):
                row[i] = int(row[i])
            print(row)
        boxx = row
        display_image = input_image.copy()
        source_image_width = display_image.shape[1]
        source_image_height = display_image.shape[0]
        for j in range(1,4):
            for i in range(1,4):
                cv2.rectangle(display_image, (source_image_width//5*i, source_image_height//5*j),(source_image_width//5*(i+1), source_image_height//5*(j+1)), (0, 0, 255), 2)
        for i in range(0,9):
            if boxx[i] != 0:
                y = math.floor(i / 3) + 1
                x = i + 1 - (y - 1) * 3
                cv2.circle(display_image, ((1 + 2 * (x-1)) * source_image_width // 10, (1 + 2 * y) * source_image_height // 10), 10 * boxx[i],(0,0,255),-1)
        #display_image = cv2.resize(display_image, (int(source_image_width), int(source_image_height)),
        #                           cv2.INTER_LINEAR)
        cv2.imshow('ss', display_image)
        raw_key = cv2.waitKey(1)
        if (raw_key != -1):
            if (handle_keys(raw_key) == False):
                end_time = time.time()
                exit_app = True
                break
        time.sleep(0.2)
