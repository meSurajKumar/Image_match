import cv2 as cv
import numpy as np
import os
from time import time
import pyautogui




os.chdir(os.path.dirname(os.path.abspath(__file__)))

loop_time = time()
while(True):
    screenshot = pyautogui.screenshot()
    # screenshot =screentShotCapture() 
    
    screenshot = cv.cvtColor(np.ascontiguousarray(screenshot),cv.COLOR_RGB2BGR)
    cv.imshow('Window capture',screenshot)
    print(f"FPS {1/(time()-loop_time)}")
    loop_time = time()
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break
print('Done')



