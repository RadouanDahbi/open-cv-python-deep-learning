import numpy as np
import cv2

cap = cv2.VideoCapture("../../Data/cars_city.mp4")

# OpenCV uses BGR format instead of RGB
color_1 = (0,0,255) # Red color in BGR
color_2 = (0,255,0) # Green color in BGR
line_width = 2
radius = 15
point_1 = (876,172)
point_2 = (895,255)
point_3 = (920,295)

while(True):
	ret, frame = cap.read()
	if not ret:
		print("Fin de la vidéo ou erreur de lecture")
		break

	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
	cv2.circle(frame, point_1, radius, color_1, line_width)
	cv2.rectangle(frame, point_2, point_3, color_2, line_width) 

	cv2.imshow("Image",frame)
	cv2.moveWindow("Image",0,0) 

	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()