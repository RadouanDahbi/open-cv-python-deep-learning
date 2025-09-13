import numpy as np
import cv2 
import mediapipe as mp
 
 

draw_tool = mp.solutions.drawing_utils # module de dessin permettant de dessiner les résultats des modèles de mediapipe
style_tool = mp.solutions.drawing_styles # module de styles de dessin
posEstimation = mp.solutions.pose # module d'estimation de pose corps entier

seuil = 0.5 

# pose = posEstimation.Pose() # création d'une instance du modèle d'estimation de pose 
with posEstimation.Pose(
    static_image_mode=True,
    model_complexity=1,
    smooth_landmarks=True,
    enable_segmentation=True,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
) as pose:
    ## video
    cap = cv2.VideoCapture("../../Data/player_1.mov")

    while True:
        
        hasFrame, frame = cap.read()
        if not hasFrame:
            break
        
        frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # MediaPipe attend RGB
        results = pose.process(frameRGB) 
        if results.pose_landmarks: 
            draw_tool.draw_landmarks(frame, results.pose_landmarks, posEstimation.POSE_CONNECTIONS)

        print(results.pose_landmarks)

        cv2.imshow('Pose estimation', frame)
        cv2.moveWindow("Pose estimation", 0, 0)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

#     ## image statique
#     img = cv2.imread("../../Data/image_00.jpg")
#     img = cv2.resize(img, (0,0), fx=0.4, fy=0.4)
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = pose.process(imgRGB)

#     # out = img.copy()
#     if results.segmentation_mask is not None:
#         mask = results.segmentation_mask
#         # person = (mask > seuil).astype("uint8")
#         _,person_mask = cv2.threshold(mask, seuil, 1, cv2.THRESH_BINARY)
#         person_mask = person_mask.astype('uint8')
#         person = cv2.bitwise_and(img, img, mask=person_mask)
#         # person_mask_3 = cv2.merge((person_mask, person_mask, person_mask))
#         # person = img * person_mask_3



    
#     if results.pose_landmarks:
#         # draw_tool.draw_landmarks(img, results.pose_landmarks, posEstimation.POSE_CONNECTIONS)
#         draw_tool.draw_landmarks(
#             person, 
#             results.pose_landmarks, 
#             posEstimation.POSE_CONNECTIONS,
#             )


#     # cv2.imshow("Segmentation", person)
#     # cv2.imshow("Pose estimation", img)
#     cv2.imshow("Result", np.concatenate((img, person), axis=1))


# cv2.waitKey(0)
# cv2.destroyAllWindows()





