@echo OFF
echo installing requirements for python
timeout /t 2 /nobreak > NUL
python --version >nul 2>&1 && ( pip install -r requirements.txt && goto normal_ ) || ( goto terminate_)

:normal_
cls
goto exit_

:terminate_
echo 'python3 is not installed'
echo 'close the program and install python first'

:exit_
echo.