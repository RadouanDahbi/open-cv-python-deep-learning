import numpy as np
import cv2

image = cv2.imread("../../Data/image_02.jpg")

'''
cv2.imshow("Original",image)

blur_1 = cv2.GaussianBlur(image, (7,31), 0)
cv2.imshow("Blur_1",blur_1)

blur_2 = cv2.GaussianBlur(image, (31,7), 0)
cv2.imshow("Blur_2",blur_2)

blur_3 = cv2.GaussianBlur(image, (31,31), 0)
cv2.imshow("Blur_3",blur_3)


blur_4 = cv2.GaussianBlur(image[0:300,0:300,:], (31,31),0)
cv2.imshow("Blur_4",blur_4)

image[0:300,0:300,:] = blur_4
cv2.imshow("Original_2",image)
'''

h = image.shape[0]
w = image.shape[1]


color = (0,255,0) # Green color in BGR
line_width = 2
side = 180
point_1, point_2 = None, None

def blur(event, x, y, flags, param):
    global point_1, point_2
    if event == cv2.EVENT_LBUTTONDOWN:
        point_1 = (x-side//2, y-side//2)
        point_2 = (x+side//2, y+side//2)

    
    
cv2.namedWindow("Original")
cv2.moveWindow("Original",0,0)
cv2.setMouseCallback("Original", blur)

while True :

    image_copy = image.copy()

    if point_1 and point_2:

        x1, y1 = point_1
        x2, y2 = point_2

        x1, y1 = max(0, x1), max(0, y1)     
        x2, y2 = min(w-1, x2), min(h-1, y2) 
        
        roi_blur = cv2.GaussianBlur(image_copy[y1:y2,x1:x2,:], (31,31), 0)
        image_copy[y1:y2,x1:x2,:] = roi_blur
        
        cv2.rectangle(image_copy, point_1, point_2, color, line_width)

    cv2.imshow("Original",image_copy)


    if cv2.waitKey(1) & 0xFF == 27:  # ESC pour quitter
        break


cv2.destroyAllWindows()