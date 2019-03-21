@echo off
REM Call run_hbe.bat directly
call ..\..\..\Base\HBE\run_hbe.bat %~dp0hbe.ini %*
set return=%errorlevel%
echo %cmdcmdline% | findstr /ic:"%~f0" >nul && pause
exit /b %return%
