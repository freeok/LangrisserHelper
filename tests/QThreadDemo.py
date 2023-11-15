import time

from PyQt6 import QtGui
from PyQt6.QtCore import QSize, QThread
from PyQt6.QtWidgets import (QApplication, QPushButton, QVBoxLayout, QWidget)


class MyThread(QThread):
    def __init__(self, func1, func2):
        super().__init__()
        self.func1 = func1
        # 回调方法
        self.func2 = func2

    def run(self):
        # 任务完成前的方法
        self.func1()
        # do something
        print('扫荡完成！')
        # 任务完成后的方法
        self.func2()


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setup_ui()
        self.btn.clicked.connect(self.test)

    def setup_ui(self):
        self.setWindowTitle('demo')
        self.resize(QSize(250, 180))
        # 创建一个垂直布局
        layout = QVBoxLayout()
        # 创建一个按钮
        self.btn = QPushButton('扫荡秘境')
        # 按钮字体
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn.setFont(font)
        layout.addWidget(self.btn)
        # 将布局设置为主窗口的布局
        self.setLayout(layout)
        # 显示窗口
        self.show()

    def test(self):
        self.btn.setDisabled(True)
        self.btn.setText('扫荡中 ...')
        self.t = MyThread(self.callback_before, self.callback_after)
        self.t.start()

    def callback_before(self):
        time.sleep(1)
        self.btn.setText('扫荡中 .')
        time.sleep(1)
        self.btn.setText('扫荡中 . .')
        time.sleep(1)
        self.btn.setText('扫荡中 . . .')
        time.sleep(1)
        self.btn.setText('扫荡完毕')
        time.sleep(1)

    def callback_after(self):
        self.btn.setText('扫荡秘境')
        self.btn.setDisabled(False)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
