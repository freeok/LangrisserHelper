# 奖励领取
import time

import pyautogui

from src.pyautogui_utils import PyautoguiUtils

# 在 class 中运行的路径
img_daily_path = 'assets/img/daily/'

# 不在 class 中运行的路径
# img_daily_path = '../assets/img/daily/'


class RewardCollection:

    def __init__(self):
        super().__init__()

    # 一键领取任务奖励
    def task_reward(self):
        PyautoguiUtils.click_gui2(img_daily_path + 'task1.png', img_daily_path + 'task2.png')
        PyautoguiUtils.click_gui(img_daily_path + 'collect_all.png')
        time.sleep(1)
        pyautogui.click(100, 100)
        PyautoguiUtils.click_gui(img_daily_path + 'back.png')

    # 一键领取邮件奖励
    def mail_reward(self):
        PyautoguiUtils.click_gui2(img_daily_path + 'mail1.png', img_daily_path + 'mail2.png')
        PyautoguiUtils.click_gui(img_daily_path + 'collect_all.png')
        time.sleep(1)
        pyautogui.click(100, 100)
