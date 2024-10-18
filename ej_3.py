import cv2

def rotar(imagen):
   while (True):
      cv2.imshow('Rota la imagen', imagen)
      key = cv2.waitKey(0)
      imagen = cv2.rotate(imagen, cv2.ROTATE_90_CLOCKWISE)
      if key == 27:
         break
   cv2.destroyAllWindows()
if __name__ == "__main__":
   ima = cv2.imread("mario.jpg")
   rotar(ima)
