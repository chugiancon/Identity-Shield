import cv2
import cvzone
from ultralytics import YOLO

cap = cv2.VideoCapture(0)
facemodel = YOLO('yolov8n-face.pt')

while True:
    rt, video = cap.read()
    video = cv2.resize(video, (1020, 720))
    face_result = facemodel.predict(video, conf=0.40)
    for info in face_result:
        parameters = info.boxes
        for box in parameters:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            height, width = y2-y1, x2-x1
            cvzone.cornerRect(video, [x1, y1, width, height], l=9, rt=3)
    cv2.imshow('frame', video)
    cv2.waitKey(1)
