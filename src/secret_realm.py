import time

from src.pyautogui_utils import PyautoguiUtils

img_dungeon_path = 'assets/img/dungeon/'
img_daily_path = 'assets/img/daily/'


# 秘境
class SecretRealm:

    def __init__(self):
        super().__init__()

    # img 图片 n 扫荡次数
    def fun(self, img, n):
        PyautoguiUtils.click_gui(img_daily_path + img)
        time.sleep(2)
        # 点击女神球
        PyautoguiUtils.click_godless_ball()
        # 点击扫荡，按钮默认为蓝色，消耗通行证时为黄色
        PyautoguiUtils.click_gui2(img_daily_path + 'sweep.png', img_daily_path + 'sweep2.png')
        # 点击确定
        PyautoguiUtils.click_gui(img_daily_path + 'confirm.png')
        # 再次扫荡
        for i in range(n - 1):
            PyautoguiUtils.click_gui(img_daily_path + 'sweep_again.png')
        # 取消
        PyautoguiUtils.click_gui(img_daily_path + 'cancel.png')
        PyautoguiUtils.click_gui(img_daily_path + 'back.png')

    # 扫荡秘境
    def sweep(self):
        print('==> 开始扫荡秘境')

        # 进入秘境
        PyautoguiUtils.click_gui2(img_daily_path + 'secret_realm1.png', img_daily_path + 'secret_realm2.png')

        # 兄贵健身房（普通玩家2次，月卡玩家3次）（可全部开放）
        self.fun('dear_brother.png', 2)

        # 女神的试炼（普通玩家1次，月卡玩家2次）
        self.fun('goddess.png', 1)

        # 滚轮向下滚动n次
        PyautoguiUtils.scroll(-1, 10)

        # 羁绊之地
        self.fun('bond.png', 1)

        PyautoguiUtils.scroll(-1, 25)

        # 永恒的神殿
        self.fun('temple.png', 1)

        # TODO 律定之途（可全部开放）

        # 返回主界面
        PyautoguiUtils.click_gui(img_daily_path + 'back.png')

        print('<== 扫荡秘境结束')

        return 0
