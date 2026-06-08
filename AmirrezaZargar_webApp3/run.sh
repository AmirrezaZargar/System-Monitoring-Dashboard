@echo off
echo ================================
echo   System Monitor - Amirreza Zargar
echo ================================
echo.

if not exist venv (
    echo [1/3] Creating virtual environment...
    python -m venv venv
)

echo [2/3] Installing dependencies...
call venv\Scripts\activate
pip install -r requirements.txt --quiet

echo [3/3] Starting server...
echo.
echo Open your browser: http://localhost:5000
echo Press Ctrl+C to stop.
echo.
python app.py

pause
