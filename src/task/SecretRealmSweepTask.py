from PyQt6.QtCore import QThread

from src.secret_realm import SecretRealm
from src.util.pyautogui_utils import PAGUtils
from src.util.window_utils import WindowUtils


class SecretRealmSweepTask(QThread):
    def __init__(self, func1, args1, func2, args2):
        super().__init__()
        self.func1 = func1
        self.args1 = args1
        # 回调方法
        self.func2 = func2
        self.args2 = args2

    def run(self):
        WindowUtils.maximize('梦幻模拟战')

        PAGUtils.click_gui('assets/img/world.png', False)

        # 任务完成前的方法
        self.func1(self.args1[0], self.args1[1])

        # do something
        SecretRealm().sweep()

        # 任务完成后的方法
        self.func2(self.args2[0], self.args2[1])
