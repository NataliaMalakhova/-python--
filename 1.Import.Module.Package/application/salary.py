def calculate_salary(employee_list, employee_id, coefficient=1.1):
    """
    Функция для вычисления зарплаты конкретного сотрудника с применением коэффициента.

    :param employee_list: Список сотрудников.
    :param employee_id: Идентификатор сотрудника.
    :param coefficient: Коэффициент для умножения зарплаты.
    :return: Данные о сотруднике с пересчитанной зарплатой или None, если сотрудник не найден.
    """
    for employee in employee_list:
        if employee['id'] == employee_id:
            updated_employee = employee.copy()  # Копируем словарь сотрудника, чтобы не изменять оригинал
            updated_employee['salary'] = round(employee['salary'] * coefficient, 2)
            return updated_employee
    return None  # Возвращаем None, если сотрудник с заданным id не найден


# print(calculate_salary([{'id': 1, 'name': 'Christina Rojas', 'position': 'Chief Strategy Officer', 'salary': 47365.69},
#                         {'id': 2, 'name': 'Gary Smith', 'position': 'Haematologist', 'salary': 99569.56},
#                         {'id': 3, 'name': 'Matthew Roth', 'position': 'Outdoor activities/education manager',
#                          'salary': 111292.5},
#                         {'id': 4, 'name': 'Danielle Carr', 'position': 'Secretary/administrator', 'salary': 79070.44},
#                         {'id': 5, 'name': 'Derrick Li', 'position': 'Call centre manager', 'salary': 105421.57},
#                         {'id': 6, 'name': 'Michelle Simmons', 'position': 'Television production assistant',
#                          'salary': 87273.47},
#                         {'id': 7, 'name': 'Steven Williamson', 'position': 'Lecturer, further education',
#                          'salary': 95753.83},
#                         {'id': 8, 'name': 'Michael Bell', 'position': 'Chartered legal executive (England and Wales)',
#                          'salary': 91599.1},
#                         {'id': 9, 'name': 'Travis Mcdonald', 'position': 'IT consultant', 'salary': 117254.99},
#                         {'id': 10, 'name': 'Gregory Vazquez', 'position': 'Designer, graphic', 'salary': 58419.94}], 3))
