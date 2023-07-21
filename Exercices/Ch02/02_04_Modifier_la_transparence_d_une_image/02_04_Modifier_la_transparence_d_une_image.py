import numpy as np
import cv2

color = cv2.imread("..\\..\\Data\\image_05.jpg",1)

gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray.jpg",gray)

 
b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

rgba_b = cv2.merge((b,g,r,b))
rgba_g = cv2.merge((b,g,r,g) )
rgba_r = cv2.merge((b,g,r,r))
 
cv2.imwrite("rgba_b.png",rgba_b)
cv2.imwrite("rgba_g.png",rgba_g)
cv2.imwrite("rgba_r.png",rgba_r)
