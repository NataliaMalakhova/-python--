from flask import Flask, request, jsonify, send_file
from celery import Celery
from upscale import upscale
from io import BytesIO
import os

app = Flask(__name__)

# Конфигурация Celery
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# Хранение обработанных файлов в памяти
processed_files = {}


@celery.task(bind=True)
def upscale_task(self, image_bytes):
    try:
        result = upscale(image_bytes)
        task_id = self.request.id
        processed_files[task_id] = result
        return task_id
    except Exception as e:
        return str(e)


@app.route('/upscale', methods=['POST'])
def upscale_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    task = upscale_task.delay(file.read())
    return jsonify({"task_id": task.id}), 202


@app.route('/tasks/<task_id>', methods=['GET'])
def get_task_status(task_id):
    task = upscale_task.AsyncResult(task_id)

    if task.state == 'PENDING':
        return jsonify({"status": "Pending"}), 200
    elif task.state == 'SUCCESS':
        return jsonify({"status": "Completed", "file_url": f"/processed/{task_id}"}), 200
    else:
        return jsonify({"status": "Failed", "error": str(task.info)}), 400


@app.route('/processed/<task_id>', methods=['GET'])
def get_processed_file(task_id):
    if task_id in processed_files:
        return send_file(BytesIO(processed_files[task_id]), mimetype='image/png')
    else:
        return jsonify({"error": "File not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
