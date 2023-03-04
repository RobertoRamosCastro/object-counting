import cv2
import numpy as np

video = cv2.VideoCapture('los_angeles.mp4')

_, frame = video.read()

cv2.imshow('video', frame)

# si se presiona la tecla 'Esc' sale del bucle
cv2.waitKey(0)

