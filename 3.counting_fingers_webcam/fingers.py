import cv2 
import mediapipe as mp

# Initial Setup
camera = cv2.VideoCapture(0)
hands_solution = mp.solutions.hands
hand = hands_solution.Hands(max_num_hands=1)
lines = mp.solutions.drawing_utils

while True:
    
    # Variables
    status, frame = camera.read()
    videoRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hand.process(videoRGB)
    hand_points = results.multi_hand_landmarks
    height, width, _ = frame.shape
    coordinates = []
    count = 0

    # Detecting and counting fingers
    if hand_points:
        for points in hand_points:
            lines.draw_landmarks(frame, points, hands_solution.HAND_CONNECTIONS)

            for id, coordinate in enumerate(points.landmark):
                cx, cy = int(coordinate.x * width), int(coordinate.y * height)
                coordinates.append((cx, cy))

        fingers = [8,12,16,20]

        if points:
            if coordinates[4][0] < coordinates[2][0]:
                count += 1
            for f in fingers:
                if coordinates[f][1] < coordinates[f-2][1]:
                    count += 1
    
    # Showing analysis
    cv2.rectangle(frame, (80, 10), (200, 100), (255, 0, 0), -1)
    cv2.putText(frame, str(count), (100, 100), cv2.FONT_HERSHEY_SIMPLEX,4, (255,255,255), 5)
    cv2.imshow("Video", frame)
    
    # To close the window with 'esc' buttom
    if cv2.waitKey(5) == 27: 
        break
    
# Make sure the webcam and window have been closed
camera.release()
cv2.destroyAllWindows()