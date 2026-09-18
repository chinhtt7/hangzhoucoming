@echo off
title Hangzhou 90 - Streamlit App
cd /d "%~dp0"
echo ========================================================
echo   HANGZHOU 90 - TIENG TRUNG TAC CHIEN (STREAMLIT)
echo ========================================================
echo Dang khoi dong server Streamlit...
start "" http://localhost:8501
python -m streamlit run app.py
pause
