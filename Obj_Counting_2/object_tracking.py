import cv2
import numpy as np

cap = cv2.VideoCapture('los_angeles.mp4')


while True:

    ret, frame = cap.read()

    cv2.imshow(frame)

    if (cv2.waitKey(30) == 27):
            break