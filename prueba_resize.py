import cv2

# Carga el video
video = cv2.VideoCapture('vehicle-counting.mp4')

# Obtiene la resolución actual del video
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Crea un objeto VideoWriter para guardar el nuevo video con la resolución deseada
out = cv2.VideoWriter('nuevo_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (1280, 720))

while True:
    # Lee cada frame del video
    ret, frame = video.read()
    
    print(f"Frame original: {frame.shape}")
    # Si no hay más frames, sale del bucle
    if not ret:
        break
    
    # Redimensiona el frame al nuevo tamaño
    frame_resized = cv2.resize(frame, (1280, 720))
    
    # Escribe el frame redimensionado en el nuevo video
    out.write(frame_resized)
    print(f"Frame modificado: {frame_resized.shape}")

# Libera los recursos
video.release()
out.release()
cv2.destroyAllWindows()
