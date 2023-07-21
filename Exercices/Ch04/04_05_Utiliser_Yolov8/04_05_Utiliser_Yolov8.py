import cv2 
from ultralytics import YOLO

  
 

img = cv2.imread("..\\..\\Data\\image_07.PNG",1) 


model = YOLO("yolov8l.pt") 

results = model(img)

cv2.imshow('Yolov8', img)


cv2.waitKey(0)
cv2.destroyAllWindows()



'''
while True:
    
    hasFrame, frame = cap.read()
     
    frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
    
    results = model(frame)
   
     
    cv2.imshow('Yolov8', frame)
    cv2.moveWindow("Yolov8", 0, 0)
     
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break



'''