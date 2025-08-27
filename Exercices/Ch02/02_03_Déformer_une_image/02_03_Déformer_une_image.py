import numpy as np
import cv2

 
color = cv2.imread("../../Data/image_05.jpg", 1)
cv2.imshow("Image",color)
cv2.moveWindow("Image",0,0)


'''
b,g,r = cv2.split(color)

cv2.imshow("Blue",b)
cv2.imshow("Green",g)
cv2.imshow("Red",r)
'''


img = np.zeros([150,200,3],'uint8')
# img[:,:,0] += 255
img[:,:] = (255,0,0)
cv2.imshow("image", img)



b,g,r = cv2.split(img)

cv2.imshow("Blue",b)
print(f"La taille de l'image img est : {img.shape}")
print(f"La taille de l'image b est : {b.shape}")

  
cv2.waitKey(0)
cv2.destroyAllWindows()