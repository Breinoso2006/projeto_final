import cv2 
import mediapipe as mp
import math

# Initial Setup
video = cv2.VideoCapture('4.contador_polichinelos_webcam\polichinelos.mp4')
pose_solution = mp.solutions.pose
Pose = pose_solution.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
lines = mp.solutions.drawing_utils
count = 0
check = True

while True:
    
    # Variables
    status, frame = video.read()
    RGBvideo = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = Pose.process(RGBvideo)
    body_points = results.pose_landmarks
    lines.draw_landmarks(frame, body_points, pose_solution.POSE_CONNECTIONS)
    height, width, _ = frame.shape

    # Pontos: https://google.github.io/mediapipe/solutions/pose.html
    
    # Detecting body and counting jumping jacks
    if body_points:
        right_foot_x = int(body_points.landmark[pose_solution.PoseLandmark.RIGHT_FOOT_INDEX].x*width)
        right_foot_y = int(body_points.landmark[pose_solution.PoseLandmark.RIGHT_FOOT_INDEX].y*height)

        left_foot_x = int(body_points.landmark[pose_solution.PoseLandmark.LEFT_FOOT_INDEX].x*width)
        left_foot_y = int(body_points.landmark[pose_solution.PoseLandmark.LEFT_FOOT_INDEX].y*height)

        right_hand_x = int(body_points.landmark[pose_solution.PoseLandmark.RIGHT_INDEX].x*width)
        right_hand_y = int(body_points.landmark[pose_solution.PoseLandmark.RIGHT_INDEX].y*height)

        left_hand_x = int(body_points.landmark[pose_solution.PoseLandmark.LEFT_INDEX].x*width)
        left_hand_y = int(body_points.landmark[pose_solution.PoseLandmark.LEFT_INDEX].y*height)

        hands_distance = math.hypot(right_hand_x - left_hand_x, right_hand_y - left_hand_y)
        feet_distance = math.hypot(right_foot_x - left_foot_x, right_foot_y - left_foot_y)

        if check and hands_distance <= 150 and feet_distance >= 150:
            count += 1
            check = False

        if hands_distance > 150 and feet_distance < 150:
            check = True

    # Showing analysis
    cv2.rectangle(frame, (80, 10), (200, 100), (255, 0, 0), -1)
    cv2.putText(frame, str(count), (100, 100), cv2.FONT_HERSHEY_SIMPLEX,4, (255,255,255), 5)
    cv2.imshow('Video', frame)

    # To close the window with 'esc' buttom
    if cv2.waitKey(5) == 27: 
        break

# Make sure the window have been closed
cv2.destroyAllWindows()