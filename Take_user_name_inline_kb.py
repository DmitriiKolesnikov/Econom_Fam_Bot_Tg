from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

take_user_name_kb = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton(text='Да, все верно', callback_data='correct_name')
btn2 = InlineKeyboardButton(text='Нет, надо исправить ', callback_data='incorrect_name')
take_user_name_kb.add(btn1).insert(btn2)
