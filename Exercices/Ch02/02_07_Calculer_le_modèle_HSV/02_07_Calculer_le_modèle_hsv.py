import numpy as np
import cv2

 
color = cv2.imread("..\\..\\Data\\image_05.jpg", 1)
cv2.imshow("Image",color)
cv2.moveWindow("Image",0,0)
 
  


hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
 
cv2.imshow("HSV",hsv)
cv2.imshow("H",h)
cv2.imshow("S",s)
cv2.imshow("V",v)

print(f"La dimension de l'image color est : {color.shape}")
print(f"La dimension de l'image h est : {h.shape}")
print(f"La dimension de l'image s est : {s.shape}")
print(f"La dimension de l'image v est : {v.shape}")
 
cv2.waitKey(0)
cv2.destroyAllWindows()