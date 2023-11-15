import time

import pyautogui


class PyautoguiUtils:

    @staticmethod
    def click_gui(img):
        while True:
            # 获取图片定位，当grayscale=True时会使图像和屏幕截图中的颜色去饱和，解决由于显示器饱和度不同从而引起的颜色细微差异因而导致的图像定位失败问题。
            try:
                location = pyautogui.locateCenterOnScreen(img, confidence=0.8, grayscale=True)
                # 单击坐标位置，duration表示移动光标的耗时
                pyautogui.click(location.x, location.y, duration=0.3)
                return True
            # pyautogui 0.9.41 前，找不到图像返回 None，之后改为抛 ImageNotFoundException 异常
            except pyautogui.ImageNotFoundException:
                print('未匹配到样本图片%s，1秒后重试' % img)
                time.sleep(1)

    @staticmethod
    def click_gui2(img1, img2):
        while True:
            try:
                location = pyautogui.locateCenterOnScreen(img1)
                pyautogui.click(location.x, location.y, duration=0.2)
                return True
            except pyautogui.ImageNotFoundException:
                print('图片1未找到，开始匹配图片2')
                try:
                    location = pyautogui.locateCenterOnScreen(img2, confidence=0.8, grayscale=True)
                    pyautogui.click(location.x, location.y, duration=0.2)
                    return True
                except pyautogui.ImageNotFoundException:
                    print('未匹配到样本图片%s，1秒后重试' % img2)
                    time.sleep(1)

    @staticmethod
    def scroll(val, n):
        # 屏幕尺寸
        width, height = pyautogui.size()
        pyautogui.moveTo(width / 2, height / 2, duration=0.3)
        time.sleep(1)
        for i in range(n):
            pyautogui.scroll(val)

    @staticmethod
    def click_godless_ball():
        img_daily_path = '../resources/img/daily/'
        region_list = list(
            pyautogui.locateAllOnScreen(img_daily_path + 'bless_ball.png', confidence=0.7, grayscale=True))
        if len(region_list) != 0:
            region = region_list[-1]
            print(region.left, region.top)
            pyautogui.click(region.left, region.top, duration=0.3)
