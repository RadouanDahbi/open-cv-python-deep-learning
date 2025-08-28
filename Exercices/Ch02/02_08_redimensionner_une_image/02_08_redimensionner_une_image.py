import numpy as np
import cv2

img = cv2.imread("../../Data/image_05.jpg",1)
cv2.imshow("Original",img)

h,w = img.shape[:2]
print(f"hauteur: {h}, largeur: {w}")

img_half = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
cv2.imshow("Half",img_half)

img_stretch = cv2.resize(img, (w, int(h*2)), interpolation = cv2.INTER_LINEAR)
cv2.imshow("Stretch",img_stretch)

cv2.waitKey(0)
cv2.destroyAllWindows()
 