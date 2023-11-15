import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from bin.secret_realm import SecretRealm
from ui.pyqt import Ui_MainWindow


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainForm, self).__init__()
        self.setupUi(self)
        # 测试按钮
        # self.pushButton_test.clicked.connect(self.btn_test)
        # 扫荡秘境按钮
        self.pushButton_sweep.clicked.connect(self.secret_realm_sweep)
        # 每日任务按钮
        self.pushButton_task.clicked.connect(self.daily_tasks)

    # def btn_test(self):
    #     self.pushButton_test.setDisabled(True)
    #     print('你点击了测试按钮')
    #     self.pushButton_test.setText('执行完毕！')

    def secret_realm_sweep(self):
        SecretRealm().sweep()

    def daily_tasks(self):
        # 这里不需要插入按钮类型
        QMessageBox.about(self, '信息', '功能开发中...')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myw = MyMainForm()
    myw.show()
    sys.exit(app.exec())
