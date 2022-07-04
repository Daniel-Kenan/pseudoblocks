@echo OFF
echo installing requirements for python
timeout /t 2 /nobreak > NUL
pip install -r requirements.txt
openblock