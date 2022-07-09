import cv2
import mediapipe as mp
import sys
import os

# Initial Setup
recognizer = mp.solutions.face_detection.FaceDetection()

for filename in os.listdir():

    # Variables
    final_path = 'new_' + filename
    count = 0

    # To confirm that 'filename' is an image
    if (not filename.endswith('.jpg') and not filename.endswith('.jpeg')):
        continue

    # Getting image
    image = cv2.imread(filename)
    results = recognizer.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Treating possible errors
    if not results.detections:
        print('No face detected in this image.')
        sys.exit()
    new_image = image.copy()

    # Detecting, counting and drawing on image
    for detection in results.detections:
        count += 1
        mp.solutions.drawing_utils.draw_detection(new_image, detection)

    cv2.rectangle(new_image, (80, 10), (200, 100), (255, 0, 0), -1)
    cv2.putText(new_image, str(count), (100, 100), cv2.FONT_HERSHEY_SIMPLEX,4, (255,255,255), 5)
    cv2.imwrite(final_path, new_image)
