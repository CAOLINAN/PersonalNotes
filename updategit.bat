@echo off
set /p m=请输入提交信息:
git add .
git commit -m %m%
git push
rem 输入时记得自己加引号