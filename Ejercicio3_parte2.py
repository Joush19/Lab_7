import numpy as np
import cv2

class Imagen:
    def __init__(self):        
        self.color_rojo = np.zeros((100, 100, 3), dtype=np.uint8)
        self.color_rojo[:, :, 2] = 255  #rojo

        self.color_verde = np.zeros((100, 100, 3), dtype=np.uint8)
        self.color_verde[:, :, 1] = 255  #verde

        self.color_azul = np.zeros((100, 100, 3), dtype=np.uint8)
        self.color_azul[:, :, 0] = 255  #azul

        self.imagen = self.color_rojo

    def convertir_a_rgb(self):        
        imagen_rgb = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2RGB)
        return imagen_rgb
    
    def convertir_a_hsv(self):
        imagen_hsv = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2HSV)
        return imagen_hsv
    
    def convertir_a_grises(self):
        imagen_gris = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)
        return imagen_gris

    def mostrar_imagen(self, title, imagen):
        cv2.imshow(title, imagen)
        cv2.waitKey(0)

    def limpiar(self):
        cv2.destroyAllWindows()

    def set_imagen(self, color):
        """Selecciona qué color utilizar (rojo, verde, azul)"""
        if color == 'rojo':
            self.imagen = self.color_rojo
        elif color == 'verde':
            self.imagen = self.color_verde
        elif color == 'azul':
            self.imagen = self.color_azul
        else:
            print("Color no válido.")

if __name__ == "__main__":
    imagen_obj = Imagen()

    imagen_obj.set_imagen('verde')

    imagen_rgb = imagen_obj.convertir_a_rgb()
    imagen_obj.mostrar_imagen('Imagen en RGB', imagen_rgb)

    imagen_hsv = imagen_obj.convertir_a_hsv()
    imagen_obj.mostrar_imagen('Imagen en HSV', imagen_hsv)

    imagen_gris = imagen_obj.convertir_a_grises()
    imagen_obj.mostrar_imagen('Imagen en Escala de Grises', imagen_gris)
