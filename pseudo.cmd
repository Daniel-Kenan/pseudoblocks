@echo OFF
echo.
if "%1" == "--help" ( goto commands-help goto terminate)
if "%1" == "view-date" ( goto date-view goto terminate )
if "%1" == "view-time" ( goto time-view goto terminate) 
if "%1" == "--version" ( goto version goto terminate) 
if "%1" == "view-basic" (goto basic-view goto terminate) 
if "%1" == "view-dev" (goto dev-view goto terminate) 
if "%2" == "--test"  goto testcase 
if "%2" == "--edit"  (notepad "./playground/%1" goto terminate) 
if "%1" == "" ( goto help ) else ( goto normal )

:: this function goes to the documentation dir and returns to the previous dir after printing from  a file 
:help
CD "./*tion/ " 
type "file" 
CD ".."
goto terminate

:normal
python "compile.py" "%1" 
goto terminate

:testcase
python "algo.py" "%3" "%1"
goto terminate

:basic-view
attrib +h +s *
attrib +h +s Documentation
attrib -h -s openblock.cmd
echo configuration files hidden for basic use
goto terminate

:dev-view
attrib -h -s *
attrib -h -s Documentation
echo Happy debugging ;-)
goto terminate

:time-view
echo %TIME%
goto terminate

:date-view
echo %DATE%
goto terminate

:commands-help
CD "./*tion/ "
type "commands"
CD ..
goto terminate

:version
echo version 1.0.0
:terminate
echo.