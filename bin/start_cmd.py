import datetime
import os
import time

import pyautogui

img_dungeon_path = '../res/img/dungeon/'
img_daily_path = '../res/img/daily/'
# 屏幕尺寸
width, height = pyautogui.size()


# 连续滚动
def scroll(val, n):
    pyautogui.moveTo(width / 2, height / 2, duration=0.3)
    time.sleep(1)
    for i in range(n):
        pyautogui.scroll(val)


# TODO 秘境扫荡
def sweep():
    # 秘境
    click_gui2(img_daily_path + 'secret_realm1.png', img_daily_path + 'secret_realm2.png')

    # 兄贵健身房
    click_gui(img_daily_path + 'dear_brother.png')
    time.sleep(2)
    click_gui(img_daily_path + 'back.png')
    # TODO 扫荡按钮

    # 女神的试炼
    click_gui(img_daily_path + 'goddess.png')
    time.sleep(2)
    click_gui(img_daily_path + 'back.png')
    # 移动光标，向下滚动10次
    scroll(-1, 10)

    # 羁绊之地
    click_gui(img_daily_path + 'bond.png')
    time.sleep(2)
    click_gui(img_daily_path + 'back.png')
    scroll(-1, 25)

    # 永恒的神殿
    click_gui(img_daily_path + 'temple.png')
    time.sleep(2)
    click_gui(img_daily_path + 'back.png')

    # 返回主界面
    click_gui(img_daily_path + 'back.png')


# TODO 每日任务


# TODO 日常操作：扫荡秘境 + 每日任务 + 命运之扉 + 友情点赠送/领取 + 邮件一键领取


# 刷副本
def dungeon(tag, num):
    auto_once = True
    always_count = 1
    n = num
    flag = num > 0  # 是否指定次数

    print('最后请完成下步骤')
    print('1. 进入要刷的秘境副本')
    print('2. 配置好英雄、行动顺序，点“出击”按钮')
    code = input('您是否完成以上步骤？确认请输入y，然后按回车即可执行脚本\n')
    if code.upper() == 'Y':
        while n if flag else True:
            i = num - n + 1 if flag else always_count  # 第几次执行
            print('【%s】第%s次执行' % (tag, i))
            if auto_once:
                click_gui(img_dungeon_path + 'auto.png')  # 只开一次自动
                auto_once = False
            click_gui(img_dungeon_path + 'end1.png')  # 战斗结算界面点击
            click_gui(img_dungeon_path + 'end2.png')  # 开宝箱动画点击
            screenshot(tag, i)
            click_gui(img_dungeon_path + 'restart.png')  # 点击左下方“再次战斗”按钮
            if flag:
                if i != num:  # 最后一次不执行
                    click_gui(img_dungeon_path + 'attack.png')  # 点击“出击”按钮
                n -= 1
            else:
                click_gui(img_dungeon_path + 'attack.png')  # 点击“出击”按钮
                always_count += 1
        print('【%s】连刷%s次完毕！' % (tag, num))
    else:
        print('操作取消')


# 鼠标左键单击指定图片所在位置
def click_gui(img):
    while True:
        try:
            # 获取图片定位，当grayscale=True时会使图像和屏幕截图中的颜色去饱和，解决由于显示器饱和度不同从而引起的颜色细微差异因而导致的图像定位失败问题。
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9, grayscale=True)
            # 单击坐标位置，duration表示移动光标的耗时
            pyautogui.click(location.x, location.y, duration=0.3)
            return True
        except pyautogui.ImageNotFoundException:
            print('未匹配到样本图片%s，1秒后重试' % img)
            time.sleep(1)


# click_gui 重载
def click_gui2(img1, img2):
    while True:
        try:
            # 获取图片定位，当grayscale=True时会使图像和屏幕截图中的颜色去饱和，解决由于显示器饱和度不同从而引起的颜色细微差异因而导致的图像定位失败问题。
            location = pyautogui.locateCenterOnScreen(img1, confidence=0.9, grayscale=True)
            # 单击坐标位置，duration表示移动光标的耗时（秒）
            pyautogui.click(location.x, location.y, duration=0.2)
            return True
        except pyautogui.ImageNotFoundException:
            print('开始匹配图片2')
            try:
                location = pyautogui.locateCenterOnScreen(img2, confidence=0.9, grayscale=True)
                pyautogui.click(location.x, location.y, duration=0.2)
                return True
            except pyautogui.ImageNotFoundException:
                print('未匹配到样本图片%s，1秒后重试' % img2)
                time.sleep(1)


def screenshot(tag, num):
    time.sleep(3)  # 等宝箱开完了再截图
    path = 'screenshot/%s【%s】' % (datetime.datetime.now().strftime('%Y-%m-%d'), tag)
    if not os.path.exists(path):
        os.makedirs(path)
    im1 = pyautogui.screenshot()  # 奖励截图保存
    im1.save('%s/第%s次奖励.png' % (path, num))


def check_tag(tag):
    path = 'screenshot/%s【%s】' % (datetime.datetime.now().strftime('%Y-%m-%d'), tag)
    if not os.path.exists(path):
        return True
    else:
        print('该备注已存在，请换一个')
        return False


if __name__ == '__main__':
    print('🎉 欢迎使用梦战手游RPA~')
    print('✨ 当前版本：0.1-beta.1')

    while True:
        print('\n请选择功能:')
        print('1.秘境扫荡')
        print('2.刷秘境副本')
        print('3.使用须知')
        code = input('请输入：')
        if code == '1':
            sweep()
            continue
        if code == '2':
            while True:
                print('1.无限刷(体力耗尽为止) 2.指定次数')
                key = input('请输入：')
                if key == '1' or key == '2':
                    break
            while True:
                tag = input('请为此次流程加上备注(便于查看奖励截图)：')
                if check_tag(tag):
                    break
            if key == '1':
                dungeon(tag, -1)
            if key == '2':
                dungeon(tag, int(input('请输入次数：')))
            continue
        if code == '3':
            print('【使用须知】')
            print(
                '1. 核心原理是利用图片识别定位实现的，因此该脚本不支持后台运行，也就是说运行期间必须保证游戏窗口完整的置于最上层以及显示器常亮(锁屏也不行)。')
            print('2. 使用风险由使用者自己承担。')
            continue
        else:
            print('您输入的指令有误，请按提示输入！')
            continue
