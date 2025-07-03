import numpy as np
import cv2

cap = cv2.VideoCapture("../../Data/cars_city.mp4")

while(True):
	ret, frame = cap.read()
	if not ret:
		print("Fin de la vidéo ou erreur de lecture")
		break

	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
	cv2.imshow("Image",frame)
	cv2.moveWindow("Image",0,0) 
	 
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()