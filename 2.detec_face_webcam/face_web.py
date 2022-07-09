import cv2
import mediapipe as mp

# Initial Setup
camera = cv2.VideoCapture(0) # 0 para camera padrão
reconhecedor = mp.solutions.face_detection.FaceDetection()
quadrado = mp.solutions.drawing_utils

while True:
    
    status, frame = camera.read() # retorna se foi possível acessar e a informação acessada (caso possível)
    if not status:
        break

    lista_rostos = reconhecedor.process(frame)
    count = 0

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            count += 1
            quadrado.draw_detection(frame, rosto)

    cv2.rectangle(frame, (80, 10), (200, 100), (255, 0, 0), -1)
    cv2.putText(frame, str(count), (100, 100), cv2.FONT_HERSHEY_SIMPLEX,4, (255,255,255), 5)

    cv2.imshow("Video", frame)
    
    if cv2.waitKey(5) == 27: 
        # quantos milissegundos ele espera e qual botão espera (27 = esc)
        break

camera.release() # para desligar a webcam
cv2.destroyAllWindows() # para garantir que vai fechar as janelas abertas