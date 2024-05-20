from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime


def print_current_date():
    """
    Функция для вывода текущей даты.
    """
    current_date = datetime.now().strftime("%Y.%m.%d")
    print(f"Текущая дата: {current_date}")


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

    print_current_date()  # Вывод текущей даты перед расчетом зарплаты

    if updated_employee:
        print("\nДанные о сотруднике с пересчитанной зарплатой:")
        print(updated_employee)
    else:
        print(f"\nСотрудник с id {employee_id} не найден.")
