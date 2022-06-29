import cv2
import mediapipe as mp

camera = cv2.VideoCapture(0) # 0 para camera padrão
reconhecedor = mp.solutions.face_detection.FaceDetection()
quadrado = mp.solutions.drawing_utils

while True:
    
    status, frame = camera.read() # retorna se foi possível acessar e a informação acessada (caso possível)
    if not status:
        break

    lista_rostos = reconhecedor.process(frame)
    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            quadrado.draw_detection(frame, rosto)

    cv2.imshow("Video", frame)
    
    if cv2.waitKey(5) == 27: 
        # quantos milissegundos ele espera e qual botão espera (27 = esc)
        break

camera.release() # para desligar a webcam
cv2.destroyAllWindows() # para garantir que vai fechar as janelas abertas