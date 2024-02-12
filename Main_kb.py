from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

kb_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
Raspisanie = KeyboardButton('📆Расписание')
Prepodi = KeyboardButton('👩‍🏫Преподаватели')
Meropriatia = KeyboardButton('💃Мероприятия')
Psiholog = KeyboardButton('⌛Психологическая помощь')
Svobodnii_kabi = KeyboardButton('🔎Свободные кабинеты')

kb_main.add(Raspisanie).insert(Svobodnii_kabi).add(Prepodi).insert(Meropriatia)
kb_main.add(Psiholog)

pic_btn = [
    InlineKeyboardButton(text='Эта', callback_data='this'),
    InlineKeyboardButton(text='Следующая', callback_data='next'),

]

pic_keyboard = InlineKeyboardMarkup().row(*pic_btn)

psychology_answer_btn = [
    InlineKeyboardButton(text='Отменить запись', callback_data='cancel_order'),
    InlineKeyboardButton(text='Сколько осталось бесплатных посещений?', callback_data='free_orders')
]

psychology_answer_kb = InlineKeyboardMarkup().add(psychology_answer_btn[0]).add(psychology_answer_btn[1])

psychology_order_confirmation_btn = [
    InlineKeyboardButton(text='Да, хочу отменить запись', callback_data='trully_cancel_order'),
    InlineKeyboardButton(text='Нет, случайно отменил запись', callback_data='accidentally_clicked')
]

psychology_order_confirmation_kb = InlineKeyboardMarkup().add(psychology_order_confirmation_btn[0]).add(
    psychology_order_confirmation_btn[1]
)