import cv2 # for webcam access
from jeanCV import skinDetector


def show_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        ret, img = cam.read()
        cv2.imshow('input', img)
        detector = skinDetector(img)
        detector.find_skin()
        if cv2.waitKey(250) == 27:
            break # esc to exit
    cv2.destroyAllWindows()

def main():
    show_webcam()

if __name__ == '__main__':
    main()