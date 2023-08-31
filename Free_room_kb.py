from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

free_room_kb = InlineKeyboardMarkup(row_width=2)
btn1 = InlineKeyboardButton(text='Первая пара', callback_data='first_pair')
btn2 = InlineKeyboardButton(text='Вторая пара', callback_data='second_pair')
btn3 = InlineKeyboardButton(text='Третья пара', callback_data='third_pair')
btn4 = InlineKeyboardButton(text='Четвертая пара', callback_data='forth_pair')
btn5 = InlineKeyboardButton(text='Пятая пара', callback_data="fifth_pair")
btn6 = InlineKeyboardButton(text='Шестая пара', callback_data='six_pair')
btn7 = InlineKeyboardMarkup(text='Седьмая пара', callback_data='seventh_pair')
btn8 = InlineKeyboardButton(text='Восьмая пара', callback_data='eight_pair')
free_room_kb.add(btn1).insert(btn2).add(btn3).insert(btn4)
free_room_kb.add(btn5).insert(btn6).add(btn7).insert(btn8)