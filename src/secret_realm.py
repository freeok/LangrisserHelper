import time

from src.common.constants import Consts
from src.reward import Reward
from src.util.pyautogui_utils import PAGUtils

img_dungeon_path = Consts.IMG_DUNGEON_PATH
img_daily_path = Consts.IMG_DAILY_PATH


# 秘境
class SecretRealm:

    def __init__(self):
        super().__init__()

    # img 图片 n 扫荡次数
    def fun(self, img_list, n):
        if len(img_list) == 1:
            PAGUtils.click_gui(img_daily_path + img_list[0])
        elif len(img_list) > 1:
            PAGUtils.click_gui2(img_daily_path + img_list[0], img_daily_path + img_list[1])
        time.sleep(2)
        # 点击女神球
        PAGUtils.click_godless_ball()
        # 点击扫荡，按钮默认为蓝色，消耗通行证时为黄色
        PAGUtils.click_gui2(img_daily_path + 'sweep1.png', img_daily_path + 'sweep2.png')
        # 点击确定
        PAGUtils.click_gui(img_daily_path + 'confirm.png')
        # 再次扫荡
        for _ in range(n - 1):
            PAGUtils.click_gui(img_daily_path + 'sweep_again.png')
        # 取消
        PAGUtils.click_gui(img_daily_path + 'cancel.png')
        PAGUtils.click_gui(img_daily_path + 'back.png')

    # 扫荡秘境
    def sweep(self):
        print('==> 开始扫荡秘境')

        # 进入秘境
        PAGUtils.click_gui2(img_daily_path + 'secret_realm1.png', img_daily_path + 'secret_realm2.png')

        # 兄贵健身房（普通玩家2次，月卡玩家3次）（可全部开放），兄贵的图有两种情况，一大一小
        self.fun(['dear_brother1.png', 'dear_brother2.png'], 2)

        # 女神的试炼（普通玩家1次，月卡玩家2次）
        self.fun(['goddess.png'], 1)

        # 滚轮向下滚动n次
        PAGUtils.scroll(-1, 10)

        # 羁绊之地
        self.fun(['bond.png'], 1)

        PAGUtils.scroll(-1, 25)

        # 永恒的神殿
        self.fun(['temple.png'], 1)

        # TODO 律定之途（可全部开放）

        # 返回主界面
        PAGUtils.click_gui(img_daily_path + 'back.png')

        print('<== 扫荡秘境结束')

        reward = Reward()
        reward.task_reward()

        return 0
