# LangrisserHelper

## 简介

梦幻模拟战手游助手

:sparkles: 主要功能

1. <del>支持刷任意副本，并且可以指定次数，宝箱奖励截图</del>(GUI 版待移植)
2. 秘境扫荡

:monocle_face: 局限性（后期针对性优化）

1. 仅限 Windows 使用，不支持后台运行
2. 执行功能期间不能操作电脑、不能锁屏（可以调低亮度）

:computer: 原理：图像识别定位、编程控制鼠标和键盘。pyautogui 实现

## 使用说明

1. 下载最新发行版：https://github.com/pcdd-group/LangrisserHelper/releases
2. 初次使用需要进入 assets/img 目录，将示例图片替换为自己的（在全屏状态下截图，尽量和示例图片一致）
3. 以管理员身份运行 app.exe
4. 点击“启动游戏”按钮
5. 点击相关功能按钮（游戏窗口需全屏）

## 样本截图

![back.png](assets%2Fimg%2Fdaily%2Fback.png)
![confirm.png](assets%2Fimg%2Fdaily%2Fconfirm.png)
![sweep.png](assets%2Fimg%2Fdaily%2Fsweep.png)
![sweep_again.png](assets%2Fimg%2Fdaily%2Fsweep_again.png)
![sweep2.png](assets%2Fimg%2Fdaily%2Fsweep2.png)

## 初始界面

![gui.png](assets%2Fimg%2Fgui.png)

<strong style='color:#f56c6c'>禁止修改目录名、截图文件名！会导致脚本执行出错</strong>

## 开发者

安装配置 python 3.4 以上版本，个人用的 3.10

设置 pip 源，加速下载

```commandline
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple 
pip config set install.trusted-host mirrors.aliyun.com
```

安装依赖

```commandline
pip install pyautogui
pip install opencv-python
pip install pygetwindow
pip install pyqt6
pip install pyqt6-tools
pip install pyinstaller
```

pip 安装的包放在哪里？

使用 pip list 查看已安装的包名

然后用 pip show 包名，就可以看到安装到哪了

通常安装在 python 安装目录下的 lib/site-packages

**运行 .sh 文件要配置 bash 解释器（git 目录下有）**
