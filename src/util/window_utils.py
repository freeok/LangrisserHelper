import time

import pyautogui
import pygetwindow as gw


class WindowUtils:

    @staticmethod
    def maximize(title, retry=False):
        while True:
            w_arr = gw.getWindowsWithTitle(title)
            if len(w_arr) > 0:
                print('检测到窗口：{}'.format(title))
                w = w_arr[0]
                # 窗口最大化
                w.maximize()
                break
            if retry:
                print('未检测到窗口：{}，1 秒后重试'.format(title))
                time.sleep(1)
            else:
                break

    # 窗口还原
    @staticmethod
    def restore(title):
        w_arr = gw.getWindowsWithTitle(title)
        if len(w_arr) > 0:
            w = w_arr[0]
            # 如果最大化或最小化，则将窗口恢复到正常大小
            w.restore()
            # TODO 自定义窗口大小
            # w.resizeTo(1920, 1200)
            size = pyautogui.size()
            x = int((size.width - 1920) / 2)
            y = int((size.height - 1200) / 2)
            w.moveTo(x, y)
