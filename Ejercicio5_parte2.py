import cv2

webcam = cv2.VideoCapture(0)
show_gray = False

while True:
    check, frame = webcam.read()
    if not check:
        break

    if show_gray:
        display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        window_name = "Capturing - Grayscale"
    else:
        display_frame = frame
        window_name = "Capturing - RGB"

    cv2.imshow(window_name, display_frame)

    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite('saved_img.jpg', frame)
    elif key == ord('g'):
        show_gray = True
    elif key == ord('r'):
        show_gray = False
    elif key == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
