import numpy as np
import cv2
import mediapipe as mp


draw_tool = mp.solutions.drawing_utils
faceDetection = mp.solutions.face_detection

## image statique
# img = cv2.imread("../../Data/image_06.jpg",1)
# img = cv2.resize(img, (0,0), fx=0.6, fy=0.6)
# imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

with faceDetection.FaceDetection(
    model_selection=1,
    min_detection_confidence=0.6
) as FD:
    ## video
    cap = cv2.VideoCapture("../../Data/friends.mov")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
        frameRGB  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = FD.process(frameRGB)

        h, w = frame.shape[:2]
        if results.detections:
            for det in results.detections:
                ## boîte + keypoints
                # draw_tool.draw_detection(frame, det)
                ## seulement boîte
                box = det.location_data.relative_bounding_box
                xx, yy = int(box.xmin * w), int(box.ymin * h)
                ww, hh = int(box.width * w), int(box.height * h)
                cv2.rectangle(frame, (xx,yy), (xx+ww, yy+hh), (0,255,0), 2)

        
        cv2.imshow("Face Detection", frame)
        cv2.moveWindow("Face Detection", 0, 0)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    ## image statique
    # results = FD.process(imgRGB)

    # h, w =img.shape[:2]
    # if results.detections:
    #     for det in results.detections:
    #         ## boîte + keypoints
    #         # draw_tool.draw_detection(img, det)
    #         ## seulement boîte
    #         box = det.location_data.relative_bounding_box
    #         xx, yy = int(box.xmin * w), int(box.ymin * h)
    #         ww, hh = int(box.width * w), int(box.height * h) 
    #         cv2.rectangle(img, (xx,yy), (xx+ww, yy+hh), (0,255,0), 2)
    
    # cv2.imshow("Result", img)

# cv2.waitKey(0)
cv2.destroyAllWindows()
