FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["gunicorn","-w","4","-b","0.0.0.0:8000","app:app"]
