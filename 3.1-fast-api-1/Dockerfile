# Базовый образ
FROM python:3.12-slim

# Установка рабочей директории
WORKDIR /app

# Копирование файлов
COPY . .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 80
EXPOSE 80

# Команда для запуска приложения
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
