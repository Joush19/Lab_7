import numpy as np
import cv2
def crear_imagen_color(color):
    imagen = np.zeros((100, 100, 3), dtype=np.uint8)

    if color == 'rojo':
        imagen[:, :, 2] = 255  
    elif color == 'verde':
        imagen[:, :, 1] = 255  
    elif color == 'azul':
        imagen[:, :, 0] = 255  

    return imagen


def convertir_a_hsv(imagen):
    return cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

def mostrar_imagen(title, imagen):
    cv2.imshow(title, imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detectar_color_hsv(imagen_hsv, color):
    
    if color == 'rojo':
        
        lower = np.array([0, 120, 70])
        upper = np.array([10, 255, 255])
    elif color == 'verde':
        
        lower = np.array([35, 100, 100])
        upper = np.array([85, 255, 255])
    elif color == 'azul':
        
        lower = np.array([100, 150, 0])
        upper = np.array([140, 255, 255])
    
    
    mask = cv2.inRange(imagen_hsv, lower, upper)
    return mask


imagen_roja = crear_imagen_color('rojo')

imagen_hsv_roja = convertir_a_hsv(imagen_roja)

mask_roja = detectar_color_hsv(imagen_hsv_roja, 'rojo')

mostrar_imagen('Imagen Roja', imagen_roja)
mostrar_imagen('Máscara Roja Detectada', mask_roja)

imagen_verde = crear_imagen_color('verde')

imagen_hsv_verde = convertir_a_hsv(imagen_verde)

mask_verde = detectar_color_hsv(imagen_hsv_verde, 'verde')

mostrar_imagen('Imagen Verde', imagen_verde)
mostrar_imagen('Máscara Verde Detectada', mask_verde)

imagen_azul = crear_imagen_color('azul')

imagen_hsv_azul = convertir_a_hsv(imagen_azul)

mask_azul = detectar_color_hsv(imagen_hsv_azul, 'azul')

mostrar_imagen('Imagen Azul', imagen_azul)
mostrar_imagen('Máscara Azul Detectada', mask_azul)
