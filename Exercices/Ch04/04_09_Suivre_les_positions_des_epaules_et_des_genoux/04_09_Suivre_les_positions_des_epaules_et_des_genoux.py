import cv2 
import mediapipe as mp
 

draw_tool = mp.solutions.drawing_utils 
posEstimation = mp.solutions.pose 
pose = posEstimation.Pose()
 
cap = cv2.VideoCapture("..\\..\\Data\\player_2.mov")

 

while True:
    hasFrame, frame = cap.read()
     
    frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    results = pose.process(frameRGB) 

     
    target= [11,12,25,26]
    
    

    if results.pose_landmarks : 
        for id, mark in enumerate(results.pose_landmarks.landmark):
            if id in target : 
                h,w,c = frame.shape 
                cx,cy = int(mark.x*w), int(mark.y*h)
                cv2.circle(frame, (cx,cy), 3,(0,0,255), cv2.FILLED) 

       
    cv2.imshow('Pose estimation', frame)
    cv2.moveWindow("Pose estimation", 0, 0)
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

