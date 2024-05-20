import os
import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            # Записываем дату и время вызова функции
            call_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Имя функции
            func_name = old_function.__name__
            # Аргументы функции
            func_args = f"args: {args}, kwargs: {kwargs}"

            # Вызов оригинальной функции и получение результата
            result = old_function(*args, **kwargs)

            # Запись в лог
            with open(path, 'a') as log_file:
                log_file.write(f"{call_time} - {func_name} - {func_args} - result: {result}\n")

            return result

        return new_function

    return __logger
