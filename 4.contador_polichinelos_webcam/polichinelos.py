import cv2 
import mediapipe as mp
import math

video = cv2.VideoCapture('4.contador_polichinelos_webcam\polichinelos.mp4')
solucao_pose = mp.solutions.pose
Pose = solucao_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
linhas = mp.solutions.drawing_utils
contador = 0
check = True

while True:
    status, frame = video.read()
    videoRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = Pose.process(videoRGB)
    pontos_corpo = resultados.pose_landmarks
    linhas.draw_landmarks(frame, pontos_corpo, solucao_pose.POSE_CONNECTIONS)
    altura, largura, _ = frame.shape

    # Pontos: https://google.github.io/mediapipe/solutions/pose.html
    
    if pontos_corpo:
        pe_direito_x = int(pontos_corpo.landmark[solucao_pose.PoseLandmark.RIGHT_FOOT_INDEX].x*largura)
        pe_direito_y = int(pontos_corpo.landmark[solucao_pose.PoseLandmark.RIGHT_FOOT_INDEX].y*altura)

        pe_esquerdo_x = int(pontos_corpo.landmark[solucao_pose.PoseLandmark.LEFT_FOOT_INDEX].x*largura)
        pe_esquerdo_y = int(pontos_corpo.landmark[solucao_pose.PoseLandmark.LEFT_FOOT_INDEX].y*altura)

        mao_direita_x = int(pontos_corpo.landmark[solucao_pose.PoseLandmark.RIGHT_INDEX].x*largura)
        mao_direita_y = int(pontos_corpo.landmark[solucao_pose.PoseLandmark.RIGHT_INDEX].y*altura)

        mao_esquerda_x = int(pontos_corpo.landmark[solucao_pose.PoseLandmark.LEFT_INDEX].x*largura)
        mao_esquerda_y = int(pontos_corpo.landmark[solucao_pose.PoseLandmark.LEFT_INDEX].y*altura)

        distancia_maos = math.hypot(mao_direita_x - mao_esquerda_x, mao_direita_y - mao_esquerda_y)
        distancia_pes = math.hypot(pe_direito_x - pe_esquerdo_x, pe_direito_y - pe_esquerdo_y)

        if check and distancia_maos <= 150 and distancia_pes >= 150:
            contador += 1
            check = False

        if distancia_maos > 150 and distancia_pes < 150:
            check = True

    cv2.rectangle(frame, (80, 10), (200, 100), (255, 0, 0), -1)
    cv2.putText(frame, str(contador), (100, 100), cv2.FONT_HERSHEY_SIMPLEX,4, (255,255,255), 5)

    cv2.imshow('Resultado', frame)

    if cv2.waitKey(5) == 27: 
        break

cv2.destroyAllWindows()