import numpy as np
import cv2

img = cv2.imread("..\\..\\Data\\image_01.jpg",1)

h, w,c = img.shape 



'''
R1 = cv2.getRotationMatrix2D((0,0), -45, 1)
rotated_1 = cv2.warpAffine(img, R1, (img.shape[0], img.shape[1]))
cv2.imshow("Normal",img)
cv2.imshow("Rotated_1",rotated_1)
''' 

 
R2 = cv2.getRotationMatrix2D((w/2,h/2), -90, 1)
rotated_2 = cv2.warpAffine(img, R2, (img.shape[1], img.shape[0]))
cv2.imshow("Normal",img)
cv2.imshow("Rotated_2",rotated_2)

cv2.waitKey(0)
cv2.destroyAllWindows()