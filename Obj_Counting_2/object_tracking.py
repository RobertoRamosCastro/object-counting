import cv2
import numpy as np

video = cv2.VideoCapture('C:\\Users\\Roberto\\Documents\\Udemy_Object_Detection\\object-counting\\Obj_Counting_2\\traffic.mp4')

while True:
    _, frame = video.read()

    cv2.imshow('video', frame)

    # si se presiona la tecla 'Esc' sale del bucle
    if(cv2.waitKey(30) == 27):
        break

cv2.destroyAllWindows()