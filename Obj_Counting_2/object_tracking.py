import cv2
import numpy as np

from object_detection import ObjectDetection

# Initialize Object Detection
od = ObjectDetection()

video = cv2.VideoCapture('C:\\Users\\Roberto\\Documents\\Udemy_Object_Detection\\object-counting\\Obj_Counting_2\\angeles.mp4')

count = 0

while True:
    ret, frame = video.read()
    count += 1
    if not ret:
        break

    # Detect objects in frame
    (class_id, scores, boxes) = od.detect(frame)
    for box in boxes:
        # box es un array con las 4 posiciones de una caja q recoge la pos del coche
        # podemos meterlo en estas variables y crear un rectangulo
        (x, y, h, w) = box
        # para poder contarlos, cogemos el centro del box
        cx = int((x+x+w) / 2)
        cy = int((y+y+h) / 2)
        print("Frame Nº", count, "BOX",x, y, w, h) # mostrando los boxes
        # para dibujar un rectangulo necesitamos top left point y bot right point
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0), thickness=2)
        # dibujamos un ciruclo donde se situe el centro del objeto
        cv2.circle(frame,(cx,cy),5, (0,0,255), -1)

    cv2.imshow('video', frame)

    # si se presiona la tecla 'Esc' sale del bucle
    key = cv2.waitKey(1)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()