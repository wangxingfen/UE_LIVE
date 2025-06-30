@echo off
:: 激活 Conda 环境
call conda activate gybot

:: 运行 Python 脚本
python move.py

:: 暂停以查看输出
pause