import time

import pygetwindow as gw
from PyQt6.QtCore import QThread


class CheckGameRunningTask(QThread):

    def __init__(self, window):
        super().__init__()
        self.window = window

    def run(self):

        while True:
            w_arr = gw.getWindowsWithTitle('梦幻模拟战')

            # 游戏窗口存在
            if len(w_arr) > 0:
                # 按钮设为红色，改变文本
                self.window.setStyleSheet('background: #e47470; color: #fff')
                self.window.setText('关闭游戏')
            else:
                # 按钮设为绿色，改变文本
                self.window.setStyleSheet('background: #7ec050; color: #fff')
                self.window.setText('启动游戏')

            time.sleep(1)
