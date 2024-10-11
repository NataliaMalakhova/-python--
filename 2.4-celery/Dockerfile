FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Install Redis
RUN apt-get update && apt-get install -y redis-server

# Expose Flask and Redis ports
EXPOSE 5000 6379

# Start Redis server, Celery worker, and Flask app
CMD redis-server & \
    celery -A app.celery worker --loglevel=info & \
    python app.py
