from Json_data import data_all_teachers_and_mails
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
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



