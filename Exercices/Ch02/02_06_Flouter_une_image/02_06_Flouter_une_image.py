import numpy as np
import cv2

image = cv2.imread("..\\..\\Data\\image_02.jpg")
cv2.imshow("Original",image)

'''
blur_1 = cv2.GaussianBlur(image, (7,31),0)
cv2.imshow("Blur_1",blur_1)

blur_2 = cv2.GaussianBlur(image, (31,7),0)
cv2.imshow("Blur_2",blur_2)

blur_3 = cv2.GaussianBlur(image, (31,31),0)
cv2.imshow("Blur_3",blur_3)
'''

blur_4 = cv2.GaussianBlur(image[0:300,0:300,:], (31,31),0)
cv2.imshow("Blur_4",blur_4)

image[0:300,0:300,:] = blur_4
cv2.imshow("Original_2",image)

cv2.waitKey(0)
cv2.destroyAllWindows()