import numpy as np
import cv2

color = cv2.imread("../../Data/image_05.jpg",1)

gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.jpg",gray)
cv2.imshow("Gray",gray)

# gris = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
# cv2.imshow("Gris",gris)

# isEqual = np.array_equal(gray,gris)
# print(f"Les images gray et gris sont égales : {isEqual}")


b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

# blue,green,red = cv2.split(color)

# print(f"is b equal to blue : {np.array_equal(b,blue)}")
# print(f"is g equal to green : {np.array_equal(g,green)}")
# print(f"is r equal to red : {np.array_equal(r,red)}")


bgra_b = cv2.merge((b,g,r,b))
bgra_g = cv2.merge((b,g,r,g))
bgra_r = cv2.merge((b,g,r,r))
 
cv2.imwrite("rgba_b.png",bgra_b)
cv2.imshow("BGRA - B",bgra_b)
cv2.imwrite("rgba_g.png",bgra_g)
cv2.imshow("BGRA - G",bgra_g)
cv2.imwrite("rgba_r.png",bgra_r)
cv2.imshow("BGRA - R",bgra_r)


cv2.waitKey(0)
cv2.destroyAllWindows()