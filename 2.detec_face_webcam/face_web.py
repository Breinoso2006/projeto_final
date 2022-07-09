import cv2
import mediapipe as mp

# Initial Setup
camera = cv2.VideoCapture(0) # 0 is default
recognizer = mp.solutions.face_detection.FaceDetection()
square = mp.solutions.drawing_utils

while True:
    
    # 'status' returns a boolean (True/False) and 'frame' returns an image
    status, frame = camera.read()

    if not status:
        break

    # Variables
    list_of_faces = recognizer.process(frame)
    count = 0

    # Detecting and counting faces
    if list_of_faces.detections:
        for face in list_of_faces.detections:
            count += 1
            square.draw_detection(frame, face)

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