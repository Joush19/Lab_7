import numpy as np
import cv2
import os

ruta_carpeta = r"C:\Users\CAMI\Documents\Camila\embebidos 2\Lab_7"

color_rojo = np.zeros((100, 100, 3), dtype=np.uint8)
color_rojo[:, :, 2] = 255  # rojo

color_verde = np.zeros((100, 100, 3), dtype=np.uint8)
color_verde[:, :, 1] = 255  #verde

color_azul = np.zeros((100, 100, 3), dtype=np.uint8)
color_azul[:, :, 0] = 255  # azul

cv2.imwrite(os.path.join(ruta_carpeta, 'rojo.jpg'), color_rojo)
cv2.imwrite(os.path.join(ruta_carpeta, 'verde.jpg'), color_verde)
cv2.imwrite(os.path.join(ruta_carpeta, 'azul.jpg'), color_azul)
