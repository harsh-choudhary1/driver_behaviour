import cv2
import dlib
import threading
import sys
import random
from database import save_driver_record

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_of_face.dat")

stop_flag = False

def detect_drowsiness(driver_name):
    global stop_flag

    save_driver_record(driver_name, "Started")
    
    cap = cv2.VideoCapture(0)
    accuracy = random.randint(50, 95)

    while not stop_flag:
        ret, frame = cap.read()
        if not ret:
            print("Error: Camera not connected.")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        for face in faces:
            landmarks = predictor(gray, face)
            eye_left = landmarks.part(36).x, landmarks.part(36).y
            eye_right = landmarks.part(45).x, landmarks.part(45).y

            if abs(eye_left[1] - eye_right[1]) < 5:
                cv2.putText(frame, "DROWSY", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Drowsiness Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    save_driver_record(driver_name, "Stopped", accuracy)
    sys.exit(0)

def start_detection(driver_name):
    global stop_flag
    stop_flag = False
    thread = threading.Thread(target=detect_drowsiness, args=(driver_name,))
    thread.start()

def stop_detection():
    global stop_flag
    stop_flag = True