import numpy as np
import cv2

 
color = cv2.imread("../../Data/image_05.jpg", 1)
cv2.imshow("Image",color)
cv2.moveWindow("Image",0,0)
 
  
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

'''
h,s,v = cv2.split(hsv)
 
cv2.imshow("HSV",hsv)
cv2.imshow("H",h)
cv2.imshow("S",s)
cv2.imshow("V",v)

print(f"La dimension de l'image color est : {color.shape}")
print(f"La dimension de l'image h est : {h.shape}")
print(f"La dimension de l'image s est : {s.shape}")
print(f"La dimension de l'image v est : {v.shape}")
'''

lower_blue = np.array([104,120,40], dtype = "uint8")
upper_blue = np.array([130,255,255], dtype = "uint8")

mask = cv2.inRange(hsv, lower_blue, upper_blue)
# cv2.imshow("Mask", mask)

kernel = np.ones((3,3), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
# mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
# cv2.imshow("Mask_2", mask)

obj_blue = cv2.bitwise_and(color, color, mask=mask)
cv2.imshow("Object Blue", obj_blue)

cv2.waitKey(0)
cv2.destroyAllWindows()