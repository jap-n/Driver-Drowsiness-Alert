import cv2

class FaceDetector:
    def __init__(self, model_path="models/haarcascade_frontalface_default.xml"):
        self.face_cascade = cv2.CascadeClassifier(model_path)

    def detect(self, frame):
        resized = cv2.resize(frame, (640, 360))
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        h_ratio = frame.shape[0] / 360
        w_ratio = frame.shape[1] / 640
        return [(int(x * w_ratio), int(y * h_ratio), int(w * w_ratio), int(h * h_ratio)) for (x, y, w, h) in faces]
