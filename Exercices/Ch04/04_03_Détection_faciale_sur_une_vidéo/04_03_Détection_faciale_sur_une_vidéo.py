import cv2

cap = cv2.VideoCapture("../../Data/friends.mov")
 
path_xml_face = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(path_xml_face)
path_xml_eye = "haarcascade_eye.xml"
eye_cascade = cv2.CascadeClassifier(path_xml_eye)
 

while(True):
	ret, frame = cap.read()
	if not ret:
		break

	# frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))
	
	for x,y,w,h in faces :
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
		
		gray_roi = gray[y:y+h, x:x+w]
		frame_roi = frame[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(gray_roi, scaleFactor=1.10, minNeighbors=5, minSize=(10,10))
		for (xx, yy, ww, hh) in eyes:
			xc = xx + ww//2
			yc = yy + hh//2
			radius = max(ww, hh)//2
			cv2.circle(frame_roi, (xc, yc), radius, (255,0,0), 2)
	
	 
	cv2.imshow("Image",frame)
	cv2.moveWindow("Image", 0,0)
	 
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
 

cap.release()
cv2.destroyAllWindows()
