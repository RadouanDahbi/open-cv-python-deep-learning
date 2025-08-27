import numpy as np
import cv2
img = cv2.imread("../../Data/image_05.jpg", 1)
 

print(f"Le type de l'objet img est : {type(img)}") 
print(f"Le nombre d'éléments dans img : {len(img)}") 


print(f"Le taille de l'élément img[0] img : {len(img[0])}")
print(f"{img.shape[0]} lignes et {img.shape[1]} colonnes dans l'image et {img.shape[2]} canaux de couleur")

print(f"img[0][0] = {img[0][0]}")
print(f"Le taille de l'élément img[0][0] img : {len(img[0][0])}") 


print(f"Les dimensions de l'objet img est : {img.shape}")
print(f"Le type de chaque élément de img est : {img.dtype}")
 
print(f"La taille totale : {img.shape[0]*img.shape[1]*img.shape[2]}")
print(f"La taille de l'objet img : {img.size}")

print(f"img[:, :, 0] = \n{img[:, :, 0]}")
print(f"img[0, 0, 0] = \n{img[0, 0, 0]}")
print(f"img[0, 0][0] = \n{img[0, 0][0]}")

 