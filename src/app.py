import cv2 # for webcam access
from jeanCV import skinDetector


def show_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        ret, img = cam.read()
        cv2.imshow('input', img)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k%256 == 27: # esc to exit
            break
        elif k%256 == 32: # space to capture frame
            detector = skinDetector(img)
            detector.find_skin()
    cv2.destroyAllWindows()

def main():
    show_webcam()

if __name__ == '__main__':
    main()