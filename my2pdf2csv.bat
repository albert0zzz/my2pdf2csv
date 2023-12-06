@echo off

REM Changing dir
cd "%~dp0.venv\Scripts"

REM Activating virtual enviroment
call activate.bat

REM Сalling pdf_to_txt.bat script 
python %~dp0misc\pdf_to_txt.py

REM Сalling txt_to_csv.py script 
python %~dp0misc\txt_to_csv.py

echo Convertion from .pdf to .csv complete.
pause
