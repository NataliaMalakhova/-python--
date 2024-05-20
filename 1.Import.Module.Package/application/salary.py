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
