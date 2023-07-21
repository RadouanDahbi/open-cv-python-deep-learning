import cv2 
from ultralytics import YOLO
import supervision as sv

box_annotator = sv.BoxAnnotator (
    thickness=2,
    text_thickness=2,
    text_scale=1 
)


cap = cv2.VideoCapture("..\\..\\Data\\player_1.mov") 
model = YOLO("yolov8l.pt")  

while True:
    
    hasFrame, frame = cap.read()     
    frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)    
    

    results = model(frame)[0]
    detections = sv.Detections.from_yolov8(results) 
    
    labels = [f"{model.model.names[class_id]} - {confidence:0.2f}" for _, _, confidence, class_id, _  in detections ]
    frame = box_annotator.annotate(scene=frame, detections=detections, labels=labels )
    cv2.imshow('Yolov8', frame)
    cv2.moveWindow("Yolov8", 0, 0) 
     
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break


 