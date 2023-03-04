import cv2
import numpy as np

def main():

    cap = cv2.VideoCapture('nuevo_video_angeles.mp4')

    # Obtiene la resolución actual del video
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(frame_width, frame_height)

    '''while True:

        ret, frame = cap.read()

        cv2.imshow('video',frame)

        if (cv2.waitKey(30) == 27):
                break
        
    # Libera los recursos
    cap.release()
    cv2.destroyAllWindows()'''

if __name__ == '__main__':
    main()