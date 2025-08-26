import numpy as np
import cv2

cap = cv2.VideoCapture("../../Data/cars_city.mp4")
show_c = False
show_r = False
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/2)
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/2)

# OpenCV uses BGR format instead of RGB
color_1 = (0,0,255) # Red color in BGR
color_2 = (0,255,0) # Green color in BGR
line_width = 2
radius = 25
point_1 = (radius,radius)
side = 50
point_2 = (w-1-side,h-1-side)
point_3 = (w-1,h-1)
print(f"Point 1: {point_1}, Point 2: {point_2}, Point 3: {point_3}")

def click(event, x, y, flags, param):
	global point_1, point_2, point_3, show_c, show_r
	if event == cv2.EVENT_LBUTTONDOWN:
		show_c = True
		show_r = False
		point_1 = (x,y)
	elif event == cv2.EVENT_MBUTTONDOWN:
		show_r = True
		show_c = False
		point_2 = (x-side//2,y-side//2)
		point_3 = (x+side//2,y+side//2)

cv2.namedWindow("Image")
cv2.moveWindow("Image",0,0)
cv2.setMouseCallback("Image", click)

while(True):
	ret, frame = cap.read()
	if not ret :
		print("Fin de la vidéo ou erreur de lecture")
		break
	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)

	if show_c:
		cv2.circle(frame, point_1, radius, color_1, line_width)
	if show_r:
		cv2.rectangle(frame, point_2, point_3, color_2, line_width)

	cv2.imshow("Image",frame)
	
	if cv2.waitKey(10) & 0xFF == ord('q'):
		break


cv2.destroyAllWindows()