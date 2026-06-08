FROM python:3.9-slim

WORKDIR /app

# نصب گواهی‌ها و ابزار لازم
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
 && update-ca-certificates \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "app.py"]








    # FROM python:3.9-slim
    # WORKDIR /app
    # COPY . .
    # RUN pip install -r requirements.txt
    # CMD ["python", "app.py"]
