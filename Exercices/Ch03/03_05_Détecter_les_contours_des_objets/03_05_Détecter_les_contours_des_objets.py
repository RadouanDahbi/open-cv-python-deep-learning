import numpy as np
import cv2

img = cv2.imread('..\\..\\Data\\image_05.jpg',1)
cv2.imshow("Source", img)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 111, 1)
cv2.imshow("Thresholding", thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img2 = img.copy()
thickness = 2
color = (255, 0, 0)

cv2.drawContours(img2, contours, -1, color, thickness)
cv2.imshow("Contours",img2)

 
h,w,c = img.shape 
img3 = np.zeros([h,w,1], 'uint8')
cv2.drawContours(img3, contours, -1, color, thickness)
cv2.imshow("Contours_over_black",img3) 
 


cv2.waitKey(0)
cv2.destroyAllWindows()