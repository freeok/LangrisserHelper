import time

import pygetwindow as gw


class WindowUtils:

    @staticmethod
    def maximize(title, always=False):
        while True:
            w_arr = gw.getWindowsWithTitle(title)
            if len(w_arr) > 0:
                print('检测到窗口：{}'.format(title))
                w = w_arr[0]
                # 窗口最大化
                w.maximize()
            if always:
                print('未检测到窗口：{}，1 秒后重试'.format(title))
                time.sleep(1)
            else:
                break
