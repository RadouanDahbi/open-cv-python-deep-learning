import numpy as np
import cv2

img = cv2.imread("..\\..\\Data\\image_05.jpg",1)

 
img_half = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
h,w,c = img.shape 
img_stretch = cv2.resize(img, (w, 3 * h))
 
cv2.imshow("Image",img)
cv2.imshow("Half",img_half)
cv2.imshow("Stretch",img_stretch)
 

cv2.waitKey(0)
cv2.destroyAllWindows()