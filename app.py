import sys
import time

import pyautogui
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from src.task.SecretRealmSweepTask import SecretRealmSweepTask
from src.task.StartGameTask import StartGameTask
from src.ui.pyqt import Ui_MainWindow


class MyMainForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyMainForm, self).__init__()
        # 主要线程：秘境扫荡、每日任务
        self.t = None
        # 次要线程：游戏启动
        self.t2 = None
        self.setupUi(self)

        # 扫荡秘境按钮
        self.pushButton_sweep.clicked.connect(self.secret_realm_sweep)
        # 每日任务按钮
        self.pushButton_task.clicked.connect(self.daily_tasks)
        # 终止任务按钮
        self.pushButton_abort.clicked.connect(self.abort_task)
        # 启动游戏按钮
        self.pushButton_start.clicked.connect(self.start_game)

    def secret_realm_sweep(self):
        self.t = SecretRealmSweepTask(self.sweep_pre_handle, self.sweep_post_handle)
        self.t.start()

    def daily_tasks(self):
        QMessageBox.information(self, '信息', '功能开发中')

    def abort_task(self):
        if self.t is not None and self.t.isRunning():
            self.t.terminate()
            self.set_btn_disable(False)
            self.btn_font_reset()
        else:
            QMessageBox.information(self, '信息', '无任务执行')

    def start_game(self):
        self.t2 = StartGameTask()
        self.t2.start()

    # 线程任务执行前调用
    def sweep_pre_handle(self):
        self.set_btn_disable(True)
        self.pushButton_sweep.setText('扫荡中 ...')

    # 线程任务执行后调用
    def sweep_post_handle(self):
        self.pushButton_sweep.setText('扫荡秘境')
        self.set_btn_disable(False)

    def set_btn_disable(self, flag):
        self.pushButton_sweep.setDisabled(flag)
        self.pushButton_task.setDisabled(flag)

    def btn_font_reset(self):
        self.pushButton_sweep.setText('扫荡秘境')
        self.pushButton_task.setText('每日任务')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myw = MyMainForm()
    myw.show()
    sys.exit(app.exec())
