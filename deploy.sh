#rm -rf dist build

pyinstaller app.py \
--name=app \
--onefile \
--noconsole \
--icon=assets/logo.ico \
--clean

cp -r assets dist

cd dist

mkdir LangrisserHelper

cp -r assets LangrisserHelper
cp app.exe LangrisserHelper

# 打包目录
tar cvf LangrisserHelper.tar.gz LangrisserHelper

rm -rf LangrisserHelper

echo "打包完毕！"

pwd