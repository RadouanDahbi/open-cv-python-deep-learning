import cv2 
from ultralytics import YOLO
import supervision as sv

box_annotator = sv.BoxAnnotator (
    thickness=2,
    text_thickness=2,
    text_scale=1 
)

img = cv2.imread("..\\..\\Data\\image_07.PNG",1) 
 
model = YOLO("yolov8l.pt") 

results = model(img)[0]
 
detections = sv.Detections.from_yolov8(results) 
 
labels = [f"{model.model.names[class_id]} - {confidence:0.2f}" for _, _, confidence, class_id, _  in detections ]

img = box_annotator.annotate(scene=img, detections=detections, labels=labels )

cv2.imshow('Yolov8', img)
cv2.moveWindow("Yolov8", 0, 0)


cv2.waitKey(0)
cv2.destroyAllWindows()


 

 