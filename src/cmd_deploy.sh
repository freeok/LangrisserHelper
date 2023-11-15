mkdir -p tmp
cp start_cmd.py ../assets/logo.ico tmp
cd tmp || exit

# 使用Pyinstaller将.py打包成.exe，并且指定图标
pyinstaller -F --icon=logo.ico start_cmd.py

# 进入根目录
cd ../..
# 删除旧的打包目录
rm -rf dist
# 创建新的打包目录
mkdir -p dist/LangrisserRPA/src dist/LangrisserRPA/assets

# 入口文件拷贝
cp src/tmp/dist/start_cmd.exe dist/LangrisserRPA/src
# 示例图片拷贝
cp -r assets/img dist/LangrisserRPA/assets

cd dist || exit
# 打包目录
tar cvf LangrisserRPA.tar.gz LangrisserRPA

# 删除临时文件
rm -rf ../src/tmp

echo "打包完毕！"
pwd