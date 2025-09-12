import cv2

img = cv2.imread("../../Data/image_06.jpg",1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

path1 = "haarcascade_frontalface_default.xml"
path2 = "haarcascade_eye.xml"


face_cascade = cv2.CascadeClassifier(path1)
eye_cascade = cv2.CascadeClassifier(path2)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=6, minSize=(40,40))
# eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=20, minSize=(10,10)) 

# for (x, y, w, h) in faces:
# 	cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

# for (x, y, w, h) in eyes:
# 	xc = x + w//2
# 	yc = y + h//2
# 	radius = max(w, h)//2
# 	cv2.circle(img, (xc,yc), radius, (255,0,0), 2)


for (x, y, w, h) in faces:
	cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

	gray_roi = gray[y:y+h, x:x+w]
	img_roi = img[y:y+h, x:x+w]
	eyes = eye_cascade.detectMultiScale(gray_roi, scaleFactor=1.05, minNeighbors=20, minSize=(10,10))
	for (xx, yy, ww, hh) in eyes:
		xc = xx + ww//2
		yc = yy + hh//2
		radius = max(ww, hh)//2
		cv2.circle(img_roi, (xc,yc), radius, (0,255,0), 2)


cv2.imshow("Image",img)
cv2.moveWindow("Image",0,0)
cv2.waitKey(0)
cv2.destroyAllWindows()