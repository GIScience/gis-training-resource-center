@echo off
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\build_preview_book.ps1"
echo.
echo Press any key to close this window...
pause >nul
