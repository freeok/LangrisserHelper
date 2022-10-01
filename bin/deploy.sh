mkdir -p tmp
cp start.py ../res/logo.ico tmp
cd tmp || exit

# 使用Pyinstaller将.py打包成.exe，并且指定图标
pyinstaller -F --icon=logo.ico start.py

# 进入根目录
cd ../..
# 删除旧的打包目录
rm -rf dist
# 创建新的打包目录
mkdir -p dist/LangrisserRPA/bin dist/LangrisserRPA/res

# 入口文件拷贝
cp bin/tmp/dist/start.exe dist/LangrisserRPA/bin
# 示例图片拷贝
cp -r res/img dist/LangrisserRPA/res

cd dist || exit
# 打包目录
tar cvf LangrisserRPA.tar.gz LangrisserRPA

# 删除临时文件
rm -rf ../bin/tmp

echo "打包完毕！"
pwd