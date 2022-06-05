import cv2
import mediapipe as mp
import sys

with mp.solutions.face_detection.FaceDetection() as reconhecedor:

    imagem = cv2.imread(r'C:\Users\Bruno\Documents\projeto_final\caso_base\img.jpg')
    results = mp.solutions.face_detection.FaceDetection().process(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))

    if not results.detections:
        print('Sem resultados')
        sys.exit()

    imagem_identificada = imagem.copy()

    for detection in results.detections:
        mp.solutions.drawing_utils.draw_detection(imagem_identificada, detection)
    cv2.imwrite('caso_base\imagem_identificada.png', imagem_identificada)