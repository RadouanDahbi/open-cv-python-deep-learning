import numpy as np
import cv2


img = cv2.imread("../../Data/image_02.jpg")
cv2.namedWindow("Faces")

# OpenCV uses BGR format instead of RGB
color_1 = (0,0,255) # Red color in BGR
color_2 = (0,255,0) # Green color in BGR
color_3 = (255,0,0) # Blue color in BGR
line_width = 3 
radius = 110 
point_1 = (185,215)
point_2 = (520,100)
point_3 = (670,300)
point_4 = (735,0)
point_5 = (900,185) 

img = cv2.resize(img, (900,700))
cv2.circle(img, point_1, radius, color_1, line_width)
cv2.rectangle(img, point_2, point_3, color_2, line_width) 
cv2.rectangle(img, point_4, point_5, color_3, line_width)
cv2.imshow("Faces", img)
cv2.moveWindow("Faces", 0, 0)

cv2.waitKey(0)

cv2.imwrite("image_02_opencv.jpg", img)

cv2.destroyAllWindows()