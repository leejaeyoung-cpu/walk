@echo off
chcp 65001 > nul
echo 브라우저에서 성당 관리 시스템을 엽니다...
start http://localhost:8501
timeout /t 2 > nul
exit
