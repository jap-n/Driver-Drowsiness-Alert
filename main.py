from src.capture import CaptureThread
from src.detector import FaceDetector
from src.visual import draw_boxes
import cv2
import time

def main():
    capture = CaptureThread(src=0).start()
    detector = FaceDetector()
    time.sleep(1)  # tunggu thread stabil

    while True:
        frame = capture.read()
        if frame is None:
            continue

        boxes = detector.detect(frame)
        draw_boxes(frame, boxes)

        cv2.imshow("DDA Monitor", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    capture.stop()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
