from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

meropriatia_kb = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton(text='От МГУ', callback_data='official')
btn2 = InlineKeyboardButton(text='От студентов', callback_data='unofficial')
meropriatia_kb.add(btn1).insert(btn2)