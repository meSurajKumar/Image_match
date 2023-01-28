import numpy as np
from PIL import Image, ImageGrab
from time import time
import cv2 as cv


import win32gui
import win32ui
import win32con

w = 1920 # set this
h = 1080 # set this
bmpfilenamename = "out.bmp" #set this


def captureScreren():
    hwnd = win32gui.FindWindow(None, r'NNNesterJ 0.22c - Super Mario Bros.')
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
    
    # conversion to opencv readable format..
    signedIntArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntArray,dtype='uint8')
    img.shape = (h,w,4)
    
    # dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    return img


loop_time = time()

while(True):
    screenShot = captureScreren()
    cv.imshow('screenshot ',screenShot)
    print(f'FPS {1/(time()-loop_time)}')
    loop_time = time()
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break
print('Done')
