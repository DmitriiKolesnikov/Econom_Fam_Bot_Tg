from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
Raspisanie = KeyboardButton('📆Расписание')
Prepodi = KeyboardButton('👩‍🏫Преподаватели')
Kafedri = KeyboardButton('Кафедры ЭФ МГУ')
Meropriatia = KeyboardButton('💃Мероприятия')
Staga = KeyboardButton('💰Помощь с работой')
Psiholog = KeyboardButton('⌛Психологическая помощь')
Svobodnii_kabi = KeyboardButton('🔎Свободные кабинеты')

kb_main.add(Raspisanie).insert(Svobodnii_kabi).add(Prepodi).insert(Meropriatia)
kb_main.add(Kafedri).insert(Staga).add(Psiholog)