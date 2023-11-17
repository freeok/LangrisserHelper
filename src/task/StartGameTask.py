import time

import pyautogui
import pygetwindow as gw
from PyQt6.QtCore import QThread


class StartGameTask(QThread):

    def __init__(self, text):
        super().__init__()
        self.text = text

    def run(self):
        # 启动游戏
        if self.text == '启动游戏':
            pyautogui.press('win')
            pyautogui.typewrite('PDLauncher', interval=0.01)
            pyautogui.press('enter')
            # 此时要选择是、否按钮打开程序，pyautogui 无效，暂时手动选择
            # pyautogui.press('left')
            # pyautogui.press('enter')

            while True:
                w_arr = gw.getWindowsWithTitle('梦幻模拟战')
                if len(w_arr) > 0:
                    print('检测到游戏窗口')
                    w = w_arr[0]
                    # 窗口最大化
                    w.maximize()
                    break
                else:
                    print('未检测到游戏窗口，1 秒后重试')
                    time.sleep(1)
        # 关闭游戏
        elif self.text == '关闭游戏':
            w = gw.getWindowsWithTitle('梦幻模拟战')[0]
            w.close()
