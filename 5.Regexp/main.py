import csv
import re
from pprint import pprint

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    headers = next(rows)  # пропускаем первую строку (заголовок)
    contacts_list = list(rows)
# pprint(contacts_list)

# Приведение телефонов к нужному формату
phone_pattern = re.compile(
    r"(\+7|8)?\s*\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})(?:\s*\(?доб\.?\s*(\d+)\)?)?"
)
phone_replacement = r"+7(\2)\3-\4-\5 доб.\6"

processed_contacts = []

for contact in contacts_list:
    # Объединяем первые три элемента и разделяем по пробелам, чтобы получить ФИО
    fio = ' '.join(contact[:3]).split()
    # Заполняем Фамилию, Имя и Отчество в соответствующие поля
    contact[:3] = fio + [None] * (3 - len(fio))
    # Приводим телефон к нужному формату
    if contact[5]:
        contact[5] = phone_pattern.sub(phone_replacement, contact[5]).replace(" доб.None", "")
    processed_contacts.append(contact)

# Объединение дублирующихся записей
contacts_dict = {}
for contact in processed_contacts:
    full_name = tuple(contact[:2])
    if full_name not in contacts_dict:
        contacts_dict[full_name] = contact
    else:
        for i in range(2, len(contact)):
            if not contacts_dict[full_name][i] and contact[i]:
                contacts_dict[full_name][i] = contact[i]

# Преобразование словаря обратно в список и добавление заголовка
contacts_list = [headers] + list(contacts_dict.values())

# Сохранение получившихся данных в другой файл
with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)

pprint(contacts_list)
