import numpy as np
import cv2
import os

def convertir_a_grises(imagen):
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    return imagen_gris


color_rojo = np.zeros((100, 100, 3), dtype=np.uint8)
color_rojo[:, :, 2] = 255  # rojo

color_verde = np.zeros((100, 100, 3), dtype=np.uint8)
color_verde[:, :, 1] = 255  #verde

color_azul = np.zeros((100, 100, 3), dtype=np.uint8)
color_azul[:, :, 0] = 255  #azul

rojo_gris = convertir_a_grises(color_rojo)
verde_gris = convertir_a_grises(color_verde)
azul_gris = convertir_a_grises(color_azul)

cv2.imshow('Imagen Roja', color_rojo)
cv2.imshow('Imagen Roja en Escala de Grises', rojo_gris)

cv2.imshow('Imagen Verde', color_verde)
cv2.imshow('Imagen Verde en Escala de Grises', verde_gris)

cv2.imshow('Imagen Azul', color_azul)
cv2.imshow('Imagen Azul en Escala de Grises', azul_gris)

cv2.waitKey(0)
cv2.destroyAllWindows()
