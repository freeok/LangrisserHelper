rm -rf dist build

pyinstaller -F --icon=assets/logo.ico app.py

cp -r assets dist

cd dist

mkdir LangrisserHelper

cp -r assets LangrisserHelper
cp app.exe LangrisserHelper

# 打包目录
tar cvf LangrisserHelper.tar.gz LangrisserHelper

rm -rf LangrisserHelper

echo "打包完毕！"