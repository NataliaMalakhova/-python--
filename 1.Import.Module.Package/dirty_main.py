from application.salary import *
from application.db.people import *
from datetime import datetime

if __name__ == "__main__":
    num_employees = 10  # Генерация списка из 10 сотрудников
    employees = get_employees()  # Предполагается, что get_employees вернет список сотрудников

    # Вывод оригинального списка сотрудников
    print("Оригинальный список сотрудников:")
    for emp in employees:
        print(emp)

    # Указание идентификатора сотрудника и коэффициента
    employee_id = 5  # Укажите id сотрудника
    coefficient = 1.1  # Укажите коэффициент

    # Получение данных о сотруднике с пересчитанной зарплатой
    updated_employee = calculate_salary(employees, employee_id, coefficient)

    if updated_employee:
        print("\nДанные о сотруднике с пересчитанной зарплатой:")
        print(updated_employee)
    else:
        print(f"\nСотрудник с id {employee_id} не найден.")
