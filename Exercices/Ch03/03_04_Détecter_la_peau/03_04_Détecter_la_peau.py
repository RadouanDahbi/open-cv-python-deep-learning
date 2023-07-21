import numpy as np
import cv2

img = cv2.imread('..\\..\\Data\\image_01.jpg',1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

cv2.imshow("Original",img)

hsv_split = np.concatenate((h,s,v), axis=1)
cv2.imshow("HSV",hsv_split)

 
ret, min_s = cv2.threshold(s,40,255, cv2.THRESH_BINARY)
cv2.imshow("Thresholding S",min_s)

ret, max_h = cv2.threshold(h,15, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Hue Filter",max_h)

res = cv2.bitwise_and(min_s,max_h)
cv2.imshow("Final",res)
 


cv2.waitKey(0)
cv2.destroyAllWindows()
