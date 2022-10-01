import time

import pyautogui
import win32gui

size = pyautogui.size()
print(size)

window = win32gui.FindWindow(None, '梦幻模拟战')
rect = win32gui.GetWindowRect(window)
print(rect)

width = rect[2] - rect[0]
height = rect[3] - rect[1]
print('梦战窗体宽、高：%s x %s' % (width, height))

# print(list(pyautogui.locateAllOnScreen('../res/img/t.png')))
# print(pyautogui.locateOnScreen('../res/img/t.png'))
