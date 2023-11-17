# 奖励领取
import time

import pyautogui

from src.common.constants import Consts
from src.util.pyautogui_utils import PAGUtils

# 在 class 中运行的路径
img_daily_path = Consts.IMG_DAILY_PATH


# 不在 class 中运行的路径
# img_daily_path = '../assets/img/daily/'


class Reward:

    def __init__(self):
        super().__init__()

    # 一键领取任务奖励
    def task_reward(self):
        PAGUtils.click_gui2(img_daily_path + 'task1.png', img_daily_path + 'task2.png')
        PAGUtils.click_gui(img_daily_path + 'collect_all.png')
        time.sleep(1)
        pyautogui.click(100, 100)
        PAGUtils.click_gui(Consts.IMG_BACK)

    # 一键领取邮件奖励
    def mail_reward(self):
        PAGUtils.click_gui2(img_daily_path + 'mail1.png', img_daily_path + 'mail2.png')
        PAGUtils.click_gui(img_daily_path + 'collect_all.png')
        # 等待奖励界面弹出
        time.sleep(1)
        pyautogui.click(100, 100)
        pyautogui.click(100, 100)

    # 赠送/领取友情点
    def friendship_reward(self):
        PAGUtils.click_gui(img_daily_path + 'friends.png')
        PAGUtils.click_gui(img_daily_path + 'friends_receive.png')
        PAGUtils.click_gui(img_daily_path + 'friends_give.png')
        PAGUtils.click_gui(Consts.IMG_BACK)
