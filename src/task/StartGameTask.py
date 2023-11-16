import time

import pyautogui
import pygetwindow as gw
from PyQt6.QtCore import QThread


class StartGameTask(QThread):

    def __init__(self):
        super().__init__()

    def run(self):
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.typewrite('PDLauncher')
        pyautogui.press('enter')

        while True:
            w_arr = gw.getWindowsWithTitle('梦幻模拟战')
            if len(w_arr) > 0:
                w = w_arr[0]
                # 窗口最大化
                w.maximize()
                break
            else:
                print('未检测到游戏窗口，1 秒后重试')
                time.sleep(1)
