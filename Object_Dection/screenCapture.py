import cv2
import numpy as np
import time
from mss import mss
import win32gui ,win32ui,win32con
from ObjectDection import findTargetPosition


    # Part of the screen to capture
captureWindow = win32gui.FindWindow(None, r'NNNesterJ 0.22c - Super Mario Bros.')
cascade_trainner = cv2.CascadeClassifier('imgaes/classifier/cascade.xml')
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

        rectangles = cascade_trainner.detectMultiScale(img)

        # findTargetPosition('bug.JPG',img , 0.40 , markers_options = "rectangles")
       
        top_left = (436, 326)
        bottom_right = (490, 369)

        output=cv2.rectangle(img,top_left , bottom_right , (0,255,0),cv2.LINE_4,2)


        cv2.imshow('test', output)
        print(f"FPS : {1/(time.time()-last_time)}")
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
