import pyautogui
import pygetwindow as gw
from PyQt6.QtCore import QThread

from src.util.window_utils import WindowUtils


class StartGameTask(QThread):

    def __init__(self, btn):
        super().__init__()
        self.btn = btn
        self.text = btn.text()

    def run(self):
        # 启动游戏
        if self.text == '启动游戏':
            pyautogui.press('win')
            pyautogui.typewrite('PDLauncher', interval=0.01)
            pyautogui.press('enter')
            # 此时要选择是、否按钮打开程序，pyautogui 无效，暂时手动选择
            # pyautogui.press('left')
            # pyautogui.press('enter')

        # 关闭游戏
        elif self.text == '关闭游戏':
            w = gw.getWindowsWithTitle('梦幻模拟战')[0]
            w.close()
