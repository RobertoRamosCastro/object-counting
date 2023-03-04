import cv2

# Carga el video
video = cv2.VideoCapture('los_angeles.mp4')

# Obtiene la resolución actual del video
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Crea un objeto VideoWriter para guardar el nuevo video con la resolución deseada
#out = cv2.VideoWriter('nuevo_video_angeles.mp4', cv2.VideoWriter_fourcc(*'mp4v'),30, (1280, 720))

while True:
    # Lee cada frame del video
    ret, frame = video.read()
    
    # Si no hay más frames, sale del bucle
    if not ret:
        break
    
    cv2.imshow('video',frame)
    '''# Redimensiona el frame al nuevo tamaño
    frame_resized = cv2.resize(frame, (960, 540))
    
    # Escribe el frame redimensionado en el nuevo video
    out.write(frame_resized)'''

# Libera los recursos
video.release()
#out.release()
cv2.destroyAllWindows()
