import cv2
import numpy as np
import math
from object_detection import ObjectDetection

# Initialize Object Detection
od = ObjectDetection()

video = cv2.VideoCapture('C:\\Users\\Roberto\\Documents\\Udemy_Object_Detection\\object-counting\\Obj_Counting_2\\angeles.mp4')

count = 0
prev_center_points = []

tracking_objects = {}
track_id = 0

while True:
    ret, frame = video.read()

    count += 1

    if not ret:
        break

    # guardar todos los centros para poder compararlos con los centros del frame siguiente
    curr_center_points = []

    # Detect objects in frame
    (class_id, scores, boxes) = od.detect(frame)
    for box in boxes:
        # box es un array con las 4 posiciones de una caja q recoge la pos del coche
        # podemos meterlo en estas variables y crear un rectangulo
        (x, y, h, w) = box
        # para poder contarlos, cogemos el centro del box
        cx = int((x+x+w) / 2)
        cy = int((y+y+h) / 2)
        curr_center_points.append((cx,cy))
        #print("Frame Nº", count, "BOX",x, y, w, h) # mostrando los boxes
        # para dibujar un rectangulo necesitamos top left point y bot right point
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0), thickness=2)
        # dibujar un circulo en el centro de los bounding boxes
        #cv2.circle(frame, points, 5, (0,0,255), -1)


    # Comparamos al comienzo del video, el actual y el previo frame
    if count <= 2:
        for pt in curr_center_points:
                for pt2 in prev_center_points:
                    # calculamos la distancia entre los puntos
                    distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])

                    if distance < 20:
                        tracking_objects[track_id] = pt
                        track_id += 1
    else:
        for pt in curr_center_points:
            for object_id, pt2 in tracking_objects.items():

                # calculamos la distancia entre los puntos
                distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])
                # update object position
                if distance < 20:
                    tracking_objects[object_id] = pt

    for object_id, pt in tracking_objects.items():
        cv2.circle(frame, pt, 5, (0,0,255), -1)
        cv2.putText(frame, str(object_id), (pt[0], pt[1] - 7), 0, 1, (0,0,255), 2) # frame, text, position of the text, font type, size, color, thickness

    print("Tracking objects", tracking_objects)

    print("CURR_FRAME", curr_center_points)
    print("PREV_FRAME", prev_center_points)

    cv2.imshow('video', frame)

    # Antes de que se acabe el loop hacemos una copia de las lista de centros
    # asi posteriormente podemos comparar el current frame y el previous
    prev_center_points = curr_center_points.copy()

    # si se presiona la tecla 'Esc' sale del bucle
    key = cv2.waitKey(0)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()