@echo OFF

set PSEUDOHOME=%CD%
set PYHOME=python-3.9.10-embed-amd64/
set python="%~sp0\python-3.9.10-embed-amd64\python.exe"
set python3="%~sp0\python-3.9.10-embed-amd64\python.exe"
setx /M PATH "%PATH%;%PSEUDOHOME%"
%python3% "%~sp0\intro.py"

CD clink
clink inject --quiet

echo.