import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from src.task.CheckGameRunningTask import CheckGameRunningTask
from src.task.CollectRewardTask import CollectRewardTask
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
        # 禁止调整窗口大小
        self.setFixedSize(self.width(), self.height())
        # 显示最小化和关闭按钮
        self.setWindowFlags(Qt.WindowType.WindowMinimizeButtonHint | Qt.WindowType.WindowCloseButtonHint)

        # 扫荡秘境按钮
        self.pushButton_sweep.clicked.connect(self.secret_realm_sweep)
        # 每日任务按钮
        self.pushButton_task.clicked.connect(self.daily_tasks)
        self.pushButton_reward.clicked.connect(self.collect_reward)
        # 终止任务按钮
        self.pushButton_abort.clicked.connect(self.abort_task)
        # 启动游戏按钮
        self.pushButton_start.clicked.connect(self.start_game)

        # 启动检查游戏是否运行的线程
        self.t3 = CheckGameRunningTask(self.pushButton_start)
        self.t3.start()

    # 秘境扫荡
    def secret_realm_sweep(self):
        self.t = SecretRealmSweepTask(self.btn_pre_handle, [self.pushButton_sweep, '扫荡中 ...'],
                                      self.btn_post_handle, [self.pushButton_sweep, '扫荡秘境'])
        self.t.start()

    # 每日任务
    def daily_tasks(self):
        QMessageBox.information(self, '信息', '功能开发中')

    # 领取奖励（任务、邮件、好友、众神的遗物、极星的国度、助教、浮空城）
    def collect_reward(self):
        self.t = CollectRewardTask(self.btn_pre_handle, [self.pushButton_reward, '领取中 ...'],
                                   self.btn_post_handle, [self.pushButton_reward, '领取奖励'])
        self.t.start()

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
        # 关闭之前启动的线程
        if self.t2 is not None and self.t2.isRunning():
            self.t2.terminate()
        self.t2 = StartGameTask(self.pushButton_start.text())
        self.t2.start()

    # 线程任务执行前调用
    def btn_pre_handle(self, obj, text):
        self.set_btn_disable(True)
        obj.setText(text)

    # 线程任务执行后调用
    def btn_post_handle(self, obj, text):
        self.set_btn_disable(False)
        obj.setText(text)

    def set_btn_disable(self, flag):
        self.pushButton_sweep.setDisabled(flag)
        self.pushButton_task.setDisabled(flag)
        self.pushButton_reward.setDisabled(flag)

    def btn_font_reset(self):
        self.pushButton_sweep.setText('扫荡秘境')
        self.pushButton_task.setText('每日任务')
        self.pushButton_reward.setText('领取奖励')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myw = MyMainForm()
    myw.show()
    sys.exit(app.exec())
