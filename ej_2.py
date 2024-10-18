import cv2

def resize_img(img, width, height):
    up_points = (width, height)
    img_resize = cv2.resize(img, up_points)
    return img_resize

def menu():
    img = cv2.imread("imagen_prueba.jpg")
    if img is None:
        print("Error: No se pudo cargar la imagen.")
        return

    while True:
        print("0. Original, 1. Small, 2. Medium, 3. Big, 4. Salir\n")
        a = int(input("Por favor ingrese un valor: "))

        if a == 0:
            cv2.imshow("Imagen normal", img)
        elif a == 1:
            img_resize = resize_img(img, 100, 100) 
            cv2.imshow("Imagen Small", img_resize)
        elif a == 2:
            img_resize = resize_img(img, 1000, 1000) 
            cv2.imshow("Imagen Medium", img_resize)
        elif a == 3: 
            img_resize = resize_img(img, 3000, 3000)
            cv2.imshow("Imagen Big", img_resize)
        elif a == 4:
            break
        else:
            print("Intente de nuevo.")
            continue

        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    menu()
