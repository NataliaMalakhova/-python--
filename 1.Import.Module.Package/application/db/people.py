from faker import Faker
import random
from logger import logger


def generate_employee_list(num_employees):
    """
    Функция для генерации списка сотрудников с случайными данными.

    :param num_employees: Количество сотрудников, которые нужно сгенерировать.
    :return: Список сотрудников.
    """
    fake = Faker()
    employee_list = []

    for i in range(num_employees):
        employee = {
            'id': i + 1,
            'name': fake.name(),
            'position': fake.job(),
            'salary': round(random.uniform(30000, 120000), 2)
        }
        employee_list.append(employee)

    return employee_list


employee_list = generate_employee_list(10)
path_get_employees = 'get_employees.log'


@logger(path_get_employees)
def get_employees():
    return employee_list
