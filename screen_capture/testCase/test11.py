from PIL import ImageGrab
from win32 import win32gui

hwnd = win32gui.FindWindow(None, r'NNNesterJ 0.22c - Super Mario Bros.')
win32gui.SetForegroundWindow(hwnd)
dimensions = win32gui.GetWindowRect(hwnd)
print('dimension :',dimensions)
image = ImageGrab.grab(dimensions)
image.show()