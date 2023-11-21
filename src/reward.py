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
        PAGUtils.click_img(img_daily_path + 'task.png')

        # 进入任务界面的加载时间不确定，故用此方法
        PAGUtils.click_img(img_daily_path + 'title_task.png')
        # 有奖励可领取
        found = PAGUtils.img_exists(img_daily_path + 'receive.png')
        if found:
            PAGUtils.click_img(img_daily_path + 'collect_all.png')
            time.sleep(1)
            PAGUtils.screenshot('任务奖励领取内容')
            pyautogui.click(100, 100)
            PAGUtils.click_img(Consts.IMG_BACK)
        else:
            PAGUtils.click_img(Consts.IMG_BACK)

    # 一键领取邮件奖励
    def mail_reward(self):
        PAGUtils.click_img(img_daily_path + 'mail.png')
        time.sleep(2)
        found = PAGUtils.click_img(img_daily_path + 'collect_all.png', False)
        if found:
            # 等待奖励界面弹出
            time.sleep(1)
            PAGUtils.screenshot('邮件奖励领取内容')
            pyautogui.click(100, 100)
            time.sleep(1)
            pyautogui.click(100, 100)
        else:
            pyautogui.click(100, 100)

    # 赠送/领取友情点
    def friendship_reward(self):
        PAGUtils.click_img(img_daily_path + 'friends.png')
        PAGUtils.click_img(img_daily_path + 'friends_receive.png')
        # 等待领取成功的提示
        time.sleep(1)
        PAGUtils.click_img(img_daily_path + 'friends_give.png')
        PAGUtils.click_img(Consts.IMG_BACK)
