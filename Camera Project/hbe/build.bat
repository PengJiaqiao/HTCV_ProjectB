@echo off
REM build the complete project
REM for further options see https://cmake.org/cmake/help/v3.9/manual/cmake.1.html#build-tool-mode
set CMAKE="C:\Users\aravi\Documents\Hella_Aglaia\WS1819\Base\HBE\tools\cmake\bin\cmake.exe"
%CMAKE% --build %~dp0..\build
set return=%errorlevel%
echo %cmdcmdline% | findstr /ic:"%~f0" >nul && pause
exit /b %return%
