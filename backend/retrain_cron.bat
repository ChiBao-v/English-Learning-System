@echo off
REM ============================================================
REM  Auto-retrain script cho Windows Task Scheduler
REM
REM  Cách thêm vào Task Scheduler (chạy hàng tuần):
REM    1. Mở "Task Scheduler" → "Create Basic Task"
REM    2. Trigger: Weekly, chọn ngày/giờ thích hợp (VD: Thứ 2 lúc 2:00)
REM    3. Action: Start a program
REM       Program: C:\path\to\this\retrain_cron.bat
REM    4. Finish
REM
REM  Hoặc chạy thủ công: retrain_cron.bat
REM ============================================================

cd /d "%~dp0"
python manage.py auto_retrain >> logs\retrain.log 2>&1
