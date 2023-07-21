import numpy as np
import cv2

img = cv2.imread('..\\..\\Data\\image_05.jpg',1)
cv2.imshow("Source", img)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 111, 1)
 

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("###", type(contours))
 
thickness = 5
color = (255, 0, 0)

h,w,c = img.shape 
img2 = np.zeros([h,w,3], 'uint8')

max_area = 0

for c in contours:
	area = cv2.contourArea(c)	
	if area > max_area :
		max_area = area 	

countours_without_border = []
for c in contours : 
	area = cv2.contourArea(c)	
	if area != max_area : 
		countours_without_border.append(c)



max_area = 0
max_contour = None 
 
for c in countours_without_border:
	area = cv2.contourArea(c) 
	if area  > max_area :
		max_area = area 
		max_contour = c 
		




cv2.drawContours(img2, max_contour, -1, color, thickness)
cv2.imshow("Max area",img2) 



cv2.waitKey(0)
cv2.destroyAllWindows()