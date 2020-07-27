import sys
import cv2 # for webcam access
from jeanCV import skinDetector

def show_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        ret, img = cam.read()
        if not ret:
            break
        cv2.imshow('Cam input', img)
        k = cv2.waitKey(1)
        if k%256 == 27: # esc to exit
            break
        elif k%256 == 32: # space to capture frame
            detector = skinDetector(img)
            detector.find_skin()
    cv2.destroyAllWindows()
    cam.release()

def main():
    if (len(sys.argv) < 2):
        show_webcam()
    else: 
        detector = skinDetector(cv2.imread(sys.argv[1]))
        detector.find_skin()

if __name__ == '__main__':
    main()