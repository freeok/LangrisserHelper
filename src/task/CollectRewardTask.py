from PyQt6.QtCore import QThread

from src.reward import Reward


class CollectRewardTask(QThread):

    def __init__(self, func1, args1, func2, args2):
        super().__init__()
        self.func1 = func1
        self.args1 = args1
        # 回调方法
        self.func2 = func2
        self.args2 = args2

    def run(self):
        self.func1(self.args1[0], self.args1[1])

        reward = Reward()
        reward.task_reward()
        reward.friendship_reward()
        reward.mail_reward()

        self.func2(self.args2[0], self.args2[1])
