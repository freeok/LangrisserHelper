import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from src.task.CheckGameRunningTask import CheckGameRunningTask
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
        # 启动检查游戏是否运行的线程
        self.t3 = CheckGameRunningTask(self.pushButton_start)
        self.t3.start()

    # 秘境扫荡
    def secret_realm_sweep(self):
        self.t = SecretRealmSweepTask(self.sweep_pre_handle, self.sweep_post_handle)
        self.t.start()

    # 每日任务
    def daily_tasks(self):
        QMessageBox.information(self, '信息', '功能开发中')

    # 中止任务
    def abort_task(self):
        if self.t is not None and self.t.isRunning():
            self.t.terminate()
            self.set_btn_disable(False)
            self.btn_font_reset()
        else:
            QMessageBox.information(self, '信息', '无任务执行')

    # 启动/关闭 游戏
    def start_game(self):
        # self.pushButton_start.setWindowFlags(Qt.WindowType.WindowMaximizeButtonHint)
        # 关闭之前启动的线程
        if self.t2 is not None and self.t2.isRunning():
            self.t2.terminate()
        self.t2 = StartGameTask(self.pushButton_start.text())
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
