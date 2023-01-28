import cv2
import numpy as np
import time
from mss import mss
import win32gui ,win32ui,win32con
from ObjectDection import findTargetPosition


    # Part of the screen to capture
captureWindow = win32gui.FindWindow(None, r'NNNesterJ 0.22c - Super Mario Bros.')
if not captureWindow:
    print(f'Window not found :{captureWindow}')
win32gui.SetForegroundWindow(captureWindow) # opens the capture window to we won't get the error

with mss() as sct:
    while True:
        dimensions = win32gui.GetWindowRect(captureWindow)
        last_time = time.time()
        img = sct.grab(dimensions)
        # img=np.array(img)
        img=np.ascontiguousarray(img)
        img = img[:,:,:3] # remove alpha channels so we wont get the opencv assertion error 
        img=np.ascontiguousarray(img)
        # img=np.array(img)
        findTargetPosition('bug.JPG',img , 0.40 , markers_options = "rectangles")

        print(f"FPS : {1/(time.time()-last_time)}")
        # cv2.imshow('test', img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
