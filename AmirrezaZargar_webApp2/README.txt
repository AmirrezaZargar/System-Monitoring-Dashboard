 System Monitor Web App
  Developer: Amirreza Zargar

## Run Project

To run this project locally, follow the steps below:
```bash
# 1. Go to the project directory
cd AmirrezaZargar_webApp

# 2. Create a virtual environment
py -m venv venv

# 3. Activate the virtual environment
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Start the application
py app.py


A lightweight Flask web application that displays real-time system metrics.

 Features
- Real-time CPU & RAM usage with visual progress bars
- Random background color on each refresh
- `/health` endpoint for health checks
- `/metrics` endpoint returning JSON system data
- Fully Dockerized with health checks and auto-restart
- CI/CD pipeline via GitHub Actions

 Project Structure
