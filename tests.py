from Json_data import data_all_teachers_and_mails
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import json
from datetime import datetime, timedelta

teachers_name = []
teachers_mail = []
for i in range(len(data_all_teachers_and_mails)):
    if "mail" not in data_all_teachers_and_mails[i]:
        continue
    teachers_name.append(data_all_teachers_and_mails[i]['name'])
    teachers_mail.append(data_all_teachers_and_mails[i]['mail'])

teachers_dict = dict(zip(teachers_name, teachers_mail))

teachers_dict_1 = {}
for key, val in teachers_dict.items():
    if val is not None:
        teachers_dict_1[key] = val

teachers_name_test = []
teachers_mail_kb = InlineKeyboardMarkup()
for key, val in teachers_dict_1.items():
    btn = InlineKeyboardButton(text=f'{key}', callback_data=f'{val}')
    teachers_mail_kb.add(btn)
    teachers_name_test.append(key)


URL = 'https://my.econ.msu.ru/api/schedule'
current_date = datetime.now()


def get_json_data(url): ### Получение ссыолки на страницу для парсинга
    response = requests.get(url)
    if response.status_code == 200:
        try:
            json_data = response.json()
            return json_data
        except json.decoder.JSONDecodeError:
            print("Ошибка при декодировании данных в формате JSON.")
    else:
        print("Ошибка при получении данных. Код статуса:", response.status_code)


def convert_to_datetime(date_string): ### Функция для преобразования даты в нормальный формат
    try:
        datetime_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
        datetime_obj = datetime_obj.strftime("%Y-%m-%d")
        return datetime_obj
    except ValueError:
        print("Ошибка при преобразовании строки в формате даты и времени")


json_data = get_json_data(URL)
final_data_of_teachers_to_find = json_data['sched']
i = 0
while i < len(final_data_of_teachers_to_find):
    date = convert_to_datetime(final_data_of_teachers_to_find[i]['date'])
    formatted_date = datetime.now().strftime("%Y-%m-%d")
    if date == (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"):
        print('Ура блять')
    i += 1


def check_date_name(date: datetime):
    try:
        if datetime.now() == date:
            return date
        else:
            return None
    except ValueError:
        print(f'Ошибка со сравнением дат в коде')



dict_of_teachers = {}
counter = 0
for item in final_data_of_teachers_to_find: ### создаем список преподов
    try:
        if item['teachers'] not in dict_of_teachers.keys():
            counter += 1
            name = f'{counter}_teacher_to_find'
            dict_of_teachers[item['teachers']] = name
            sorted(dict_of_teachers)
        else:
            pass
    except IndentationError:
        print(f'Ошибка в проведении итерации списка')


teachers_to_find_kb = InlineKeyboardMarkup()
for key, val in dict_of_teachers.items():
    btn = InlineKeyboardButton(text=f'{key}', callback_data=f'{val}')
    teachers_to_find_kb.add(btn)

list_of_teachers_to_find = []
for item in final_data_of_teachers_to_find:
    try:
        if item['teachers'] not in list_of_teachers_to_find:
            list_of_teachers_to_find.append(item['teachers'])
        else:
            pass
    except IndentationError:
        print(f'Ошибка в проведении итерации списка')

counter = 0
counter_2 = 0
kb_new = InlineKeyboardMarkup()
lst = []
for i in sorted(list_of_teachers_to_find):
    try:
        counter += 1
        if counter < 29:
            lst.append(i)
        elif counter == 29:
            counter_2 += 1
            btn = InlineKeyboardButton(text=f'Фамилии на буквы {lst[0][0]}-{lst[-1][0]}',
                                       callback_data=f'teachers_second_name_to_find_{counter_2}')
            kb_new.add(btn)
            lst = []
            counter = 0
    except StopIteration:
        print(f'Ошибка во время итерации')

teacher = 'Иванов Владимир Владимирович'
# print(dict_of_teachers['348_teacher_to_find'])
# print(dict_of_teachers)


