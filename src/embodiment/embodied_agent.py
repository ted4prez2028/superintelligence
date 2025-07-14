"""
Simulated embodied agent using webcam (OpenCV) and mic input.
"""
import cv2
import time

def start_camera_loop():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Camera not found.")
        return

    print("[Embodied Agent] Watching...")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("ASI Vision", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
