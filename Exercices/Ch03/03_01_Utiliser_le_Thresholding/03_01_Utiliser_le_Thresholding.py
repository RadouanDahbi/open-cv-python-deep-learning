import numpy as np
import cv2

img = cv2.imread('..\\..\\Data\\image_05.jpg',0)
height, width = img.shape[0:2]
cv2.imshow("Original",img)


binary = np.zeros([height,width,1],'uint8')

thresh = 100

for row in range(0,height):
	for col in range(0, width):
		if img[row][col]>thresh:
			binary[row][col]=255

cv2.imshow("Custom",binary)

 
ret, thresh = cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)
print(ret)
cv2.imshow("OpenCV",thresh)
 
 

cv2.waitKey(0)
cv2.destroyAllWindows()
