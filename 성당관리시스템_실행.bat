@echo off
chcp 65001 > nul
cls
echo ========================================
echo    성당 관리 시스템 시작 중...
echo ========================================
echo.

cd /d "%~dp0"

echo [1/2] 가상환경 활성화 중...
if exist .venv\Scripts\activate.bat (
    call .venv\Scripts\activate.bat
    echo ✓ 가상환경 활성화 완료
) else (
    echo ⚠ 가상환경을 찾을 수 없습니다. 전역 Python을 사용합니다.
)

echo.
echo [2/2] Streamlit 앱 실행 중...
echo.
echo ========================================
echo   브라우저가 자동으로 열립니다
echo   주소: http://localhost:8501
echo ========================================
echo.
echo 종료하려면 이 창을 닫으세요.
echo.

streamlit run app.py

pause
