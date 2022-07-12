@echo OFF

set PSEUDOHOME=%CD%
set PYHOME=python-3.9.10-embed-amd64/
set python="python-3.9.10-embed-amd64\python.exe"
set python3="python-3.9.10-embed-amd64\python.exe"

%python3% "intro.py"


CD clink
clink inject --quiet


echo.