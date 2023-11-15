from PyQt6.QtCore import QThread

from src.secret_realm import SecretRealm


class SecretRealmSweepTask(QThread):
    def __init__(self, func1, func2):
        super().__init__()
        self.func1 = func1
        # 回调方法
        self.func2 = func2

    def run(self):
        # 任务完成前的方法
        self.func1()

        # do something
        SecretRealm().sweep()

        # 任务完成后的方法
        self.func2()