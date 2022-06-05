import cv2 
import mediapipe as mp

camera = cv2.VideoCapture(0)
solucao_maos = mp.solutions.hands
mao = solucao_maos.Hands(max_num_hands=1)
linhas = mp.solutions.drawing_utils

while True:
    
    status, frame = camera.read()
    resultados = mao.process(frame)
    pontos_mao = resultados.multi_hand_landmarks
    altura, largura, _ = frame.shape
    coordenada_pontos = []
    contador = 0

    if pontos_mao:
        for pontos in pontos_mao:
            linhas.draw_landmarks(frame, pontos, solucao_maos.HAND_CONNECTIONS)

            for id, coordenada in enumerate(pontos.landmark):
                cx, cy = int(coordenada.x * largura), int(coordenada.y * altura)
                #cv2.putText(frame, str(id), (cx, cy+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2)
                coordenada_pontos.append((cx, cy))

        dedos= [8,12,16,20]

        if pontos:
            if coordenada_pontos[4][0] < coordenada_pontos[2][0]:
                contador += 1
            for d in dedos:
                if coordenada_pontos[d][1] < coordenada_pontos[d-2][1]:
                    contador += 1
    
    cv2.rectangle(frame, (80, 10), (200, 100), (255, 0, 0), -1)
    cv2.putText(frame, str(contador), (100, 100), cv2.FONT_HERSHEY_SIMPLEX,4, (255,255,255), 5)

    cv2.imshow("Video", frame)
    
    if cv2.waitKey(5) == 27: 
        break

camera.release()
cv2.destroyAllWindows()