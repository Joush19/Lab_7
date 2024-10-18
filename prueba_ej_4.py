import cv2
from abc import ABC, abstractmethod

class Imagen_Config(ABC):
    @abstractmethod
    def mostrar_imagen(self, title, imagen):
        pass

    @abstractmethod
    def resize_image(self, ancho, largo):
        pass

    @abstractmethod
    def cut_horizontally(self):
        pass

    @abstractmethod
    def cut_vertically(self):
        pass

    @abstractmethod
    def quadrants(self):
        pass

    @abstractmethod
    def limpieza(self):
        pass


class Pasos(Imagen_Config):
    def __init__(self, image_path):
        self.imagen = cv2.imread(image_path)
        if self.imagen is None:
            raise ValueError("Error: No se pudo cargar la imagen.")

    def mostrar_imagen(self, title, imagen):
        cv2.imshow(title, imagen)
        cv2.waitKey(0)

    def resize_image(self, ancho, largo):
        self.imagen = cv2.resize(self.imagen, (ancho, largo))

    def cut_horizontally(self):
        height, width = self.imagen.shape[:2]
        half_height = height // 2
        top_half = self.imagen[:half_height, :]
        bottom_half = self.imagen[half_height:, :]
        return top_half, bottom_half

    def cut_vertically(self):
        height, width = self.imagen.shape[:2]
        half_width = width // 2
        left_half = self.imagen[:, :half_width]
        right_half = self.imagen[:, half_width:]
        return left_half, right_half

    def quadrants(self):
        height, width = self.imagen.shape[:2]
        half_height = height // 2
        half_width = width // 2
        return [
            self.imagen[:half_height, :half_width],
            self.imagen[:half_height, half_width:],
            self.imagen[half_height:, :half_width],
            self.imagen[half_height:, half_width:]
        ]

    def limpieza(self):
        cv2.destroyAllWindows()


if __name__ == "__main__":
    ima = 'mario.jpg'
    objeto1 = Pasos(ima)

    objeto1.mostrar_imagen('Imagen Original', objeto1.imagen)

    objeto1.resize_image(600, 400)
    objeto1.mostrar_imagen('Imagen Redimensionada', objeto1.imagen)

    top_half, bottom_half = objeto1.cut_horizontally()
    objeto1.mostrar_imagen('Parte Superior', top_half)
    objeto1.mostrar_imagen('Parte Inferior', bottom_half)

    left_half, right_half = objeto1.cut_vertically()
    objeto1.mostrar_imagen('Parte Izquierda', left_half)
    objeto1.mostrar_imagen('Parte Derecha', right_half)

    cuadrantes = objeto1.quadrants()
    titulos = ['Cuadrante 1', 'Cuadrante 2', 'Cuadrante 3', 'Cuadrante 4']
    for titulo, cuadrante in zip(titulos, cuadrantes):
        objeto1.mostrar_imagen(titulo, cuadrante)

    objeto1.limpieza()
