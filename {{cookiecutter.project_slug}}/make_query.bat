@echo off

call D:\Users\*\radioconda\Scripts\activate.bat
call conda activate NLP

call streamlit run app.py

pause