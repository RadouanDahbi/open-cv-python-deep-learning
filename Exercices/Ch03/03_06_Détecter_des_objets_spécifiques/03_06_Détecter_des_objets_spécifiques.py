import numpy as np
import cv2

img = cv2.imread('../../Data/image_05.jpg',1)
# cv2.imshow("Source", img)

h,w,c = img.shape

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 111, 1)
# cv2.imshow("Thresholding", thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

thickness = 2
color_1 = (255, 0, 0)
color_2 = (0, 255, 0)

img2 = np.zeros([h,w,c], 'uint8')
cv2.drawContours(img2, contours, -1, color_1, thickness)
# cv2.imshow("All contours", img2)

maxArea = 0
maxContour = None

for cont in contours:
    area = cv2.contourArea(cont)
    if area > maxArea:
        maxArea = area
        maxContour = cont

res = np.zeros([h,w,c], 'uint8')
cv2.drawContours(res, [maxContour], -1, color_2, thickness) 
# cv2.imshow("Max contour", res)    

img2_rect = img2.copy()
for cont in contours:
    x,y,w,h = cv2.boundingRect(cont)
    cv2.rectangle(img2_rect, (x, y), (x+w, y+h), color_2, thickness)

ratio = 0.7
img = cv2.resize(img, (0, 0), fx=ratio, fy=ratio)
img2 = cv2.resize(img2, (0, 0), fx=ratio, fy=ratio)
img2_rect = cv2.resize(img2_rect, (0, 0), fx=ratio, fy=ratio)
res = cv2.resize(res, (0, 0), fx=ratio, fy=ratio)

final = np.concatenate((img, img2, img2_rect, res), axis = 0)
cv2.imshow("Result", final)

# max_area = 0

# for c in contours:
# 	area = cv2.contourArea(c)	
# 	if area > max_area :
# 		max_area = area 	

# countours_without_border = []
# for c in contours : 
# 	area = cv2.contourArea(c)	
# 	if area != max_area : 
# 		countours_without_border.append(c)


# max_area = 0
# max_contour = None 


# for c in countours_without_border:
# 	area = cv2.contourArea(c) 
# 	if area  > max_area :
# 		max_area = area 
# 		max_contour = c 
		

# cv2.drawContours(img2, max_contour, -1, color, thickness)
# cv2.imshow("Max area",img2) 



cv2.waitKey(0)
cv2.destroyAllWindows()