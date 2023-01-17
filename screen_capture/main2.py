import cv2
import numpy
import time
import mss
from win32 import win32gui

with mss.mss() as sct:
    # Part of the screen to capture
    hwnd = win32gui.FindWindow(None, r'NNNesterJ 0.22c - Super Mario Bros.')
    win32gui.SetForegroundWindow(hwnd)
    dimensions = win32gui.GetWindowRect(hwnd)
    # hwnd = win32gui.FindWindow(None, r'NNNesterJ 0.22c - Super Mario Bros.')
    # monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}

    while "Screen capturing":
        last_time = time.time()
        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(dimensions))

        # Display the picture
        cv2.imshow("OpenCV/Numpy normal", img)

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        print(f"fps: {1 / (time.time() - last_time)}")

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break