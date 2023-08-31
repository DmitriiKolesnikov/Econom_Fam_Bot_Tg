from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

prepodi_kb = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton(text='Где находится', callback_data='where_is_he')
btn2 = InlineKeyboardButton(text='Почта', callback_data='prepod_email')
prepodi_kb.add(btn1).insert(btn2)