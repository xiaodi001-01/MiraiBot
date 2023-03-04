@echo off
echo MiraiBot 正在启动... 
cls
echo 正在启动MiraiBot需要的资源...(启动MiraiBot需要分两步，当前为第1/2步 启动MCL)
start .\Resource\jdk-17.0.2\bin\java.exe -jar .\Resource\mcl-2.1.2\mcl.jar
set EL=%ERRORLEVEL%
if %EL% NEQ 0 (
    echo MiraiBot资源启动失败，错误代码为： %EL%
    pause
)
echo 正在启动MiraiBot...(启动MiraiBot需要分两步，当前为第2/2步 启动MiraiBot本体)
.\Resource\Python36\python.exe Bot.py
set ELA=%ERRORLEVEL%
if %ELA% NEQ 0 (
    echo MiraiBot启动失败，错误代码为： %ELA%
    pause
)