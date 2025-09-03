import numpy as np
import cv2

img = cv2.imread('../../Data/image_05.jpg',1)
# cv2.imshow("Source", img)

h, w, c = img.shape 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 111, 1)
# cv2.imshow("Thresholding", thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img2 = img.copy()
thickness = 2
color = (255, 0, 0)

cv2.drawContours(img2, contours, -1, color, thickness)
# cv2.imshow("Contours",img2)

ctr_img = np.zeros([h, w, c], 'uint8')
cv2.drawContours(ctr_img, contours, -1, color, thickness)

ratio = 0.8
img = cv2.resize(img, (0, 0), fx=ratio, fy=ratio)
# thresh = cv2.resize(thresh, (0, 0), fx=ratio, fy=ratio)
# thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
img2 = cv2.resize(img2, (0, 0), fx=ratio, fy=ratio)
ctr_img = cv2.resize(ctr_img, (0, 0), fx=ratio, fy=ratio)

res = np.concatenate((img, img2, ctr_img), axis = 0)
cv2.imshow("Result", res)
 


cv2.waitKey(0)
cv2.destroyAllWindows()