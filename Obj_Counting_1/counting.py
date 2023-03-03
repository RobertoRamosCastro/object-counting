import cv2
import argparse

from ultralytics import YOLO
import supervision as sv

import numpy as np

ZONE_POLYGON = np.array([
    [0, 300],
    [1200// 2, 300],
    [1500 // 2, 720],
    [0, 720] 
])

# creamos funcion para recibir argumentos
def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument("--webcam-resolution",
                        default=[1280,720],
                        nargs=2,
                        type=int
    )
    args = parser.parse_args()
    return args

def main():

    args = parse_arguments()

    # leemos el video
    cap = cv2.VideoCapture('nuevo_video.mp4')

    # creamos el modelo de YOLO
    model = YOLO("yolov8l.pt")

    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )

    zone = sv.PolygonZone(polygon=ZONE_POLYGON, frame_resolution_wh=tuple(args.webcam_resolution))
    zone_annotator = sv.PolygonZoneAnnotator(zone=zone,
                                            color=sv.Color.blue(),
                                            thickness=2,
                                            text_thickness=4,
                                            text_scale=2 
                                            )

    classes = [1,3,5,7]
    while True:
        # obtenemos frame y ret?? del video
        ret, frame = cap.read()

        result = model(frame, agnostic_nms= True)[0] # asi evitamos que se cuente un objeto con dos etiquetas a lavez, deshaciendonos de la q tenga menos confidence
        detections = sv.Detections.from_yolov8(result)

        detections=detections[detections.class_id==2]

        labels = [
            f"{model.model.names[class_id]} {confidence:0.3f}"
            for _, confidence, class_id, _
            in detections
        ]

        frame = box_annotator.annotate(scene=frame,
                                    detections=detections,
                                    labels=labels)
        
        zone.trigger(detections=detections)
        frame = zone_annotator.annotate(scene=frame)

        cv2.imshow("yolov8", frame)

        # si se presiona la tecla 'Esc' sale del bucle
        if (cv2.waitKey(30) == 27):
            break


if __name__ == "__main__":
    main()
