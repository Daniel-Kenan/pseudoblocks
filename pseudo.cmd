@echo OFF
echo.
@REM set PYHOME=python-3.9.10-embed-amd64/

if NOT defined %PSEUDOENVIROMENT% ( set python3="%~sp0\python-3.9.10-embed-amd64\python.exe" && set "PSEUDOENVIROMENT=y") 

if "%1" == "--help" ( goto commands-help goto terminate)
if "%1" == "highlight" ( goto highlight goto terminate)
if "%1" == "view-date" ( goto date-view goto terminate )
if "%1" == "reload" ( goto reload goto terminate )
if "%1" == "view-time" ( goto time-view goto terminate) 
if "%1" == "--version" ( goto version goto terminate) 
if "%2" == "--test"  goto testcase 
if "%2" == "--edit"  ( notepad "%1" goto terminate) 
if "%1" == "" ( goto help ) else ( goto normal )



:: this function goes to the documentation dir and returns to the previous dir after printing from  a file 

:help
TYPE "%~sp0\Documentation\file" 
goto terminate

:highlight
set workingDIR=%CD%
CD "%~sp0\\clink"
clink inject --quiet
goto terminate

:normal
%python3% "%~sp0\compile.py" "%1"
goto terminate

:testcase
%python3% "%~sp0\algo.py" "%3" "%1"
goto terminate

:time-view
echo %TIME%
goto terminate

:date-view
echo %DATE%
goto terminate

:commands-help
TYPE "%~sp0\Documentation\commands"
goto terminate

:version
echo version 1.0.3

:reload
CHDIR %PSEUDOHOME% 
echo loaded
PseudoApp
goto terminate

:terminate
echo.

