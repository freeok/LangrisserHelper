# LangrisserRPA

## 简介
梦幻模拟战手游——Python自动化脚本（命令行交互方式）

:sparkles: 功能
1. 支持刷任意副本，并且可以指定次数

:monocle_face: 局限性（后期针对性优化）
1. 仅限Windows电脑端使用，不支持后台运行
2. 期间不能操作电脑、不能锁屏（但可以调低亮度）

<strong>目前游戏新增了自动吃汉堡功能，因此只要设置一次后续就不需要再考虑体力补充的问题（<del>前提是汉堡得管够</del>）</strong>

:computer: 原理：图像识别定位、编程控制鼠标和键盘。使用pyautogui库实现

## 使用说明
1. 下载发行版：https://github.com/pcdd-group/LangrisserRPA/releases/download/v0.1-beta.1/LangrisserRPA.tar.gz
2. 初次使用需要进入res/img目录，将示例图片替换为自己的（重新手动截图，尽量截成和示例图片一样的）
3. 以管理员身份运行bin目录下的start.exe
4. 根据提示输入对应指令，然后按回车

## 样本截图
![image](https://user-images.githubusercontent.com/51998152/193248606-44ff6cdd-80b7-4592-85fe-f1dc3ad593cf.png)

## 初始界面
![image](https://user-images.githubusercontent.com/51998152/193400016-bf158a83-ffe1-4978-aa63-0e00128dbc3e.png)

<strong style='color:#f56c6c'>不要修改目录名、截图文件名！会导致脚本执行出错</strong>

## 开发者安装教程
安装配置python3.4以上版本，个人用的3.11

安装依赖包，在终端中输入
```commandline
pip install pyperclip
pip install xlrd
pip install pyautogui
pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pillow
pip install pyinstaller
```
pip安装的包放在哪里？

使用 pip list 查看已安装的包名

然后用 pip show 包名，就可以看到安装到哪了

通常安装在python安装目录下的 lib/site-packages