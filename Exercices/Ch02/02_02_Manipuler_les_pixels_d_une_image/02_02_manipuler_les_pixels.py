import numpy as np
import cv2

black_1 = np.zeros([150,200,1],'uint8')
cv2.imshow("Black_1",black_1)
print(black_1[0,0,:])

black_2 = np.zeros([150,200,3],'uint8')
cv2.imshow("Black_2",black_2)
print(black_2[0,0,:])



white = np.ones([150,200,3],'uint16')
white *= (2**16-1)
cv2.imshow("White",white)
print(white[0,0,:])

color = black_2.copy()
color[:,:] = (255,0,0)
cv2.imshow("Blue",color)
print(color[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()