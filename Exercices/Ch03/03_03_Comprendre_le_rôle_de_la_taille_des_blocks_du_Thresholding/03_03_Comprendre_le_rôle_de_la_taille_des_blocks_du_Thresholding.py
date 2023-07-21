import numpy as np
import cv2

img = cv2.imread('..\\..\\Data\\image_05.jpg',0)
 
cv2.imshow("Original",img) 

thresh = 100

 
ret, thresh_1 = cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)
cv2.imshow("Thresholding simple",thresh_1) 

thres_2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 201, 1)
cv2.imshow("Thersholding adaptatif block=201",thres_2)

thres_2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 111, 1)
cv2.imshow("Thersholding adaptatif block=111",thres_2)

thres_2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 1)
cv2.imshow("Thersholding adaptatif block=51",thres_2)

 
thres_3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 1)
cv2.imshow("Thersholding adaptatif block=9",thres_3)

 
 

cv2.waitKey(0)
cv2.destroyAllWindows()