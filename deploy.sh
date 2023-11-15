rm -rf dist build

pyinstaller -F --icon=assets/logo.ico app.py

cp -r assets dist

cd dist

mkdir Langrisser-Helper

cp -r assets Langrisser-Helper
cp app.exe Langrisser-Helper

# 打包目录
tar cvf Langrisser-Helper.tar.gz Langrisser-Helper

rm -rf Langrisser-Helper