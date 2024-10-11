import tensorflow as tf
import numpy as np
import cv2
from io import BytesIO

# Модель загружается 1 раз глобально
model = None


def load_model():
    global model
    if model is None:
        model = tf.saved_model.load("EDSR_x2.pb")
    return model


def upscale(image_bytes):
    load_model()

    # Чтение изображения из памяти (без сохранения на диск)
    np_img = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    # Предобработка изображения для модели (расширение размерности и т.д.)
    input_img = np.expand_dims(img.astype(np.float32), axis=0)

    # Прогнозирование с помощью модели
    output_img = model(input_img)

    # Постобработка выходного изображения
    output_img = np.squeeze(output_img, axis=0)

    # Запись результата в память
    _, buffer = cv2.imencode('.png', output_img)
    io_buf = BytesIO(buffer)

    return io_buf.getvalue()
