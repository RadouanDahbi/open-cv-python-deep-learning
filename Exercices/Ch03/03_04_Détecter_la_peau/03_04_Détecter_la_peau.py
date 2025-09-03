import numpy as np
import cv2

img_org = cv2.imread('../../Data/image_01.jpg', 1)

img = cv2.GaussianBlur(img_org, (3,3), 0)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

H = cv2.resize(h, (0,0), fx=0.5, fy=0.5)
S = cv2.resize(s, (0,0), fx=0.5, fy=0.5)
V = cv2.resize(v, (0,0), fx=0.5, fy=0.5)

# cv2.imshow("Original", img)

hsv_split = np.concatenate((H,S,V), axis=1)
# cv2.imshow("HSV", hsv_split)


ret, min_s = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
# cv2.imshow("Thresholding S",min_s)

ret, max_h = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow("Hue Filter",max_h)

res = cv2.bitwise_and(min_s,max_h)
# cv2.imshow("Final",res)

res_orig_1 = cv2.bitwise_and(img_org, img_org, mask=res)
# cv2.imshow("Result on Original 1", res_orig_1)

lower_skin = np.array([0, 80, 60], dtype = np.uint8)
upper_skin = np.array([15, 255, 255], dtype = np.uint8)

mask = cv2.inRange(hsv, lower_skin, upper_skin)

kernel = np.ones((3,3), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
# cv2.imshow("mask_skin", mask)

res_orig_2 = cv2.bitwise_and(img_org, img_org, mask=mask)
# cv2.imshow("Result on Original 2", res_orig_2)

contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
res_ctr = img_org.copy()
cv2.drawContours(res_ctr, contours, -1, (0,255,0), 2) 

ratio = 0.58
img_org = cv2.resize(img_org, (0, 0), fx=ratio, fy=ratio)
# res_orig_1 = cv2.resize(res_orig_1, (0, 0), fx=ratio, fy=ratio)
res_orig_2 = cv2.resize(res_orig_2, (0, 0), fx=ratio, fy=ratio)
res_ctr = cv2.resize(res_ctr, (0, 0), fx=ratio, fy=ratio)


res_orig = np.concatenate((img_org, res_orig_2, res_ctr), axis=1)
cv2.imshow("Result on Original", res_orig)
cv2.moveWindow("Result on Original",0,0)


cv2.waitKey(0)
cv2.destroyAllWindows()
