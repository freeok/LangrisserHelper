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
    def func(self, img_list, n):
        if len(img_list) == 1:
            PAGUtils.click_img(img_daily_path + img_list[0])
        # 兄贵，特殊处理
        elif len(img_list) > 1:
            PAGUtils.click_imgs(img_daily_path + img_list[0], img_daily_path + img_list[1])
        # 等待进入界面
        time.sleep(2)
        # 点击女神球
        PAGUtils.click_godless_ball()
        # 兄贵的扫荡图和其它的貌似不一样
        img_sweep = img_daily_path + ('sweep_xg.png' if len(img_list) > 1 else 'sweep1.png')
        # 点击扫荡，按钮默认为蓝色，消耗通行证时为黄色
        PAGUtils.click_imgs(img_sweep, img_daily_path + 'sweep2.png')
        # 截图保存奖励内容
        PAGUtils.screenshot('秘境扫荡奖励结果')
        # 点击确定
        PAGUtils.click_img(img_daily_path + 'confirm.png')
        # 再次扫荡
        for _ in range(n - 1):
            PAGUtils.click_img(img_daily_path + 'sweep_again.png')
            PAGUtils.screenshot('秘境扫荡奖励结果')
        # 取消
        PAGUtils.click_img(img_daily_path + 'cancel.png')
        PAGUtils.click_img(img_daily_path + 'back.png')

    # 扫荡秘境
    def sweep(self):
        # TODO 进入世界后操作，不要在浮空城操作，图片干扰因素多
        print('==> 开始扫荡秘境')

        # 进入秘境
        PAGUtils.click_img(img_daily_path + 'secret_realm.png')

        # 兄贵健身房（普通玩家2次，月卡玩家3次）（可全部开放），兄贵的图有两种情况，一大一小
        self.func(['dear_brother1.png', 'dear_brother2.png'], 2)

        # 女神的试炼（普通玩家1次，月卡玩家2次）
        self.func(['goddess.png'], 1)

        # 滚轮向下滚动n次
        PAGUtils.scroll(-1, 10)

        # 羁绊之地
        self.func(['bond.png'], 1)

        PAGUtils.scroll(-1, 25)

        # 永恒的神殿
        self.func(['temple.png'], 1)

        # TODO 律定之途（可全部开放）

        # 返回主界面
        PAGUtils.click_img(img_daily_path + 'back.png')

        print('<== 扫荡秘境结束')

        reward = Reward()
        reward.task_reward()

        return 0
