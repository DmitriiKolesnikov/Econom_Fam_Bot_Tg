import pandas as pd
from aiogram import Bot, executor, Dispatcher, types
from Main_kb import kb_main, pic_keyboard, psychology_answer_kb, psychology_order_confirmation_kb
from Take_user_name_inline_kb import take_user_name_kb
from Prepodi_inline_kb import prepodi_kb
from Free_room_kb import *
from Meropriatia_kb import meropriatia_kb
from Json_data import sched_w_st, data_all_teachers_and_mails
from Google_sheet import *
from tests import teachers_dict_1, dict_of_teachers, final_data_of_teachers_to_find
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from sercher_cacsa import get_schedule
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import date
from kabs_data_and_logic import list_of_kabs_first_flour, list_of_kabs_second_flour, \
    list_of_kabs_third_flour, list_of_kabs_fourth_flour, list_of_kabs_fith_flour

TOKEN_API = '6431263054:AAEhJ6tGq0YTFBHFQf_8sIpMMiEJycYU_Dg'


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


user_name = ''

buttons_keys = [
    'Среда 27 ноября 2024, 12:00', 'Среда 27 ноября 2024, 13:00',
    'Среда 4 декабря 2024, 12:00', 'Среда 4 декабря 2024, 13:00',
    'Среда 11 декабря 2024, 12:00', 'Среда 11 декабря 2024, 13:00',
    'Среда 18 декабря 2024, 12:00', 'Среда 18 декабря 2024, 13:00',
    'Среда 25 декабря 2024, 12:00', 'Среда 25 декабря 2024, 13:00'
]
buttons_values = [
    datetime.strptime('2024-11-27', '%Y-%m-%d'), datetime.strptime('2024-11-27', '%Y-%m-%d'),
    datetime.strptime('2024-12-04', '%Y-%m-%d'), datetime.strptime('2024-12-04', '%Y-%m-%d'),
    datetime.strptime('2024-12-11', '%Y-%m-%d'), datetime.strptime('2024-12-11', '%Y-%m-%d'),
    datetime.strptime('2024-12-18', '%Y-%m-%d'), datetime.strptime('2024-11-18', '%Y-%m-%d'),
    datetime.strptime('2024-12-25', '%Y-%m-%d'), datetime.strptime('2024-12-25', '%Y-%m-%d')    
]
buttons_dict = dict(zip(buttons_keys, buttons_values))
buttons_dict_copy = buttons_dict.copy()
psychologist = ['Полина Чибисова', 'Записаться в лист ожидания']
list_for_google_sheet = []
list_for_das = []


async def on_startup(_):
    print('Bot started')


async def feedback_message(chat_id, users_name, kb):
    await bot.send_message(chat_id=739380400,
                           text=f'Уважаемая Полина, {users_name} сегодня должен был придти на занятие . Пожалуйста, '
                                f'нажмите на кнопку «Завершить сеанс».\n\n'
                                f'<b>Только в данном</b> случае ваша запись <b>завершится официально</b>!',
                           parse_mode="HTML",
                           reply_markup=kb)




async def job(chat_id, users_name, session_date, kb):
    await bot.send_message(chat_id=chat_id,
                           text=f'Уважаемый <b>{users_name}</b>, \nнапоминаю вам о записи к психологу.\n\n'
                                f'Дата записи <b>{session_date}</b>, \nждем вас в <b>321 кабинете</b> 😊😊😊.',
                           parse_mode="HTML",
                           reply_markup=kb)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    telegram_user_name = message.from_user.full_name
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://www.econ.msu.ru/sys/raw.php?o=65079&p=attachment',
                         caption=f'Привет, {telegram_user_name}, мне очень приятно, что вы решили мною воспользоватьс'
                                 f'я!\n\n'
                                 'Давай приступим к нашему знакомству и продуктивному пребыванию на факультете!\n\n'
                                 'Как я могу вам помочь:\n\n' 
                                 '1. Помогу узнать ваше расписание.\n\n' 
                                 '2. Помогу найти преподавателя и его контактные данные.\n\n' 
                                 '3. Помогу быть в курсе всех событий факультета: официальных и не очень).\n\n'
                                 '4. Помогу найти свободные кабинеты на факультете для приятного досуга.\n\n'
                                 '5. Постараюсь не допустить депрессивных мыслей во время обучения в МГУ с помощью на'
                                 'шего '
                                 'психолога. Грустить - вредно!\n\n'
                                 'Что бы более подробно узнать о возможностях бота, нажмите \n/description',
                         reply_markup=kb_main)
    await message.delete()


@dp.message_handler(text='Вернуться в главное меню')
async def main_menu_command(message: types.Message) -> None:
    telegram_user_name = message.from_user.full_name
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://www.econ.msu.ru/sys/raw.php?o=65079&p=attachment',
                         caption=f'<b>{telegram_user_name}</b>, еще раз здравствуйте. Напомню, чем смогу вам '
                                 f'помочь:\n\n'
                                 '1. Помогу узнать ваше расписание.\n\n' 
                                 '2. Помогу найти преподавателя и его контактные данные.\n\n' 
                                 '3. Помогу быть в курсе всех событий факультета: официальных и не очень).\n\n'
                                 '4. Помогу найти свободные кабинеты на факультете для приятного досуга.\n\n'
                                 '5. Постараюсь не допустить депрессивных мыслей во время обучения в МГУ с помощью на'
                                 'шего '
                                 'психолога. Грустить - вредно!\n\n'
                                 'Что бы более подробно узнать о возможностях бота, нажмите \n/description',
                         parse_mode="HTML",
                         reply_markup=kb_main)

    await message.delete()


@dp.message_handler(commands=['description'])
async def help_command(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id,
                         caption='В данном разделе вы сможете понять, как со мной взаимодействовать.\n\n' 
                         
                                 'Кнопка «Расписания» позволит вам узнать расписание предметов. \n\n'
                                
                                 'С помощью кнопки «Свободные кабинеты» вы сможете узнать, где можно отдохнуть или '
                                 'заняться своими делами во время окон между парами. \n\n'
                                    
                                 'С помощью кнопки «Контакты преподавателей» можно связаться с преподавателем по почте '
                                 'или узнать, где он находится на факультете для личного разговора.\n\n '
                                    
                                 'С помощью кнопки «Мероприятия» вы станете активным участником жизни ВУЗа, найдете '
                                 'себе новых друзей с общими интересами.\n\n'
                                    
                                 'Кнопка «Психологическая помощь» - забота а вашем здоровье. Не пренебрегайте помощью '
                                 'специалистов. Совмещать успешную учебу, друзей и проблемы очень сложно. '
                                 'Не позвольте им испортить ваше пребывание в МГУ!!!',
                         photo='https://kartinkof.club/uploads/posts/2022-06/1656094468_3-kartinkof-club-p-kartinki-s'
                               '-nadpisyu-pomogi-mne-3.jpg')
    await message.delete()


@dp.message_handler(text='👩‍🏫Преподаватели')
async def prep_command(message: types.Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'{message.from_user.first_name}, '
                                f'в данном разделе вы сможете узнать, где находится преподаватель в течение всего '
                                f'дня или узнать его/ее почту, чтобы договориться о встрече и дальнейшего обсуждения '
                                f'вашего вопроса',
                           reply_markup=prepodi_kb)
    await message.delete()


@dp.message_handler(text='📆Расписание')
async def time_table_command(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id,
                         caption='Чтобы получить свое заветное расписание, вам надо написать свое имя <b>прям '
                                 'как в паспорте</b> 🧐'+'.\n\n'
                                 'Например, <b>Пупкин Василий Сергеевич</b>.',
                         photo='https://cs14.pikabu.ru/post_img/big/2022/03/08/7/1646737740129559994.jpg',
                         parse_mode='HTML')
    await message.delete()


@dp.message_handler(text='🔎Свободные кабинеты')
async def free_rooms_command(message: types.Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'{message.from_user.first_name}, в данном разделе вы сможете узнать, какие кабинеты '
                                f'свободны в данный момент.\nВедь свободный кабинет-место, где вы сможете провести '
                                f'время со своими друзьями между парами, занимаясь полезными вещами.\n\n'
                                f'Для начала нужно выбрать пару, в течение которой вы хотите найти пустой кабинет',
                           parse_mode='HTML',
                           reply_markup=free_room_kb)
    await message.delete()


@dp.message_handler(text='💃Мероприятия')
async def meropriatia_command(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id,
                         caption=f'{message.from_user.first_name}, в данном разделе вы сможете познакомиться со всеми '
                                 f'мероприятиями, которые будут проводиться как от лица нашего любимого '
                                 f'ЭФ МГУ, так и от лица студентов.',
                         photo='https://static.tildacdn.com/tild6138-3431-4134-a566-393364393663/EFMSU_mag_edita'
                               'ble_G.jpg',
                         reply_markup=meropriatia_kb)
    await message.delete()


@dp.message_handler(text='🏠Заявка в ДАС')
async def das_command(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(*psychologist)
    kb.add('Вернуться в главное меню')
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Данная кнопка сделана для записи в дас',
                           parse_mode="HTML",
                           reply_markup=kb)


# метод для обработки команды гугл шит
@dp.message_handler(text='⌛Психологическая помощь')
async def google_sheet_command(message: types.Message):
    for val in buttons_values:
        if datetime.now() - timedelta(hours=16) > val:
            position_number = buttons_values.index(val)
            del buttons_keys[position_number]
            del buttons_values[position_number]
    await bot.send_photo(chat_id=message.from_user.id,
                         caption=f"👩🏼 Прием осуществляется по средам с 12:00 до 14:00 (ауд 321)\n"
                                 f"На беседу с каждым человеком выделено 50 минут.\n\n"
                                 f"<b>ВАЖНО</b>: пока у нас только один психолог, Чибисова Полина. "
                                 f"Если Вы знакомы с ней лично, она не сможет к сожалению с Вами работать. "
                                 f"В этом случае <b>не надо</b> записываться на время, "
                                 f"<b>запишитесь в лист ожидания</b>.\n\n"
                                 f"У Вас есть возможность записаться на <b>2 бесплатные встречи</b>. "
                                 f"Записаться на прием  можно не позже, чем за 24 часа до встречи."
                                 f"Если Вам необходимо будет перенести или отменить встречу, "
                                 f"пожалуйста, <b>напишите об этом за 24 часа до начала сессии</b> "
                                 f"для этого надо будет нажать на кнопку <b>«Отменить запись»</b>"
                                 f", иначе встреча будет считаться состоявшейся "
                                 f"(переносить/отменять встречи можно не более 1 раза). "
                                 f"При опоздании встреча не продлевается. <b>Не опаздывайте!</b>",
                         photo='https://babr24.com/n2p/i/2021/1/21_1_5_2_05132453_b.jpg',
                         parse_mode="HTML")

    psychologist_keaboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    psychologist_keaboard.add(*psychologist)
    psychologist_keaboard.add('Вернуться в главное меню')
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Выберите психолога, с которым вы хотите встретиться',
                           parse_mode="HTML",
                           reply_markup=psychologist_keaboard)

    await message.delete()


@dp.message_handler(text="Полина Чибисова")
async def main_psychologist(message: types.Message):
    cell_list = worksheet.findall(str(message.from_user.id))
    amount_of_orders = len(cell_list)
    if amount_of_orders == 3:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Уважаемый(ая) {message.from_user.full_name}, две сессии в рамках '
                                    f'бесплатного консультирования состоялись.\n\n'
                                    f'Для продолжения работы со специалистом пишите на '
                                    f'почту <b>chibisova.polina@mail.ru</b>.',
                               parse_mode="HTML")
        list_for_google_sheet.clear()
        list_for_google_sheet.append(message.text)
        for key in list(buttons_dict.keys()):
            if datetime.now() - timedelta(hours=16) > buttons_dict[key]:
                del buttons_dict[key]
        keys = list(buttons_dict.keys())
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        if len(keys) > 5:
            for i in range(0, 6):
                keyboard.add(keys[i])
        else:
            for i in range(0, len(keys)):
                keyboard.add(keys[i])
        keyboard.add('Вернуться в главное меню')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Выберите время, в которое вам удобно встретиться",
                               parse_mode="HTML",
                               reply_markup=keyboard)

    else:
        list_for_google_sheet.clear()
        list_for_google_sheet.append(message.text)
        for key in list(buttons_dict.keys()):
            if datetime.now() - timedelta(hours=16) > buttons_dict[key]:
                del buttons_dict[key]
        keys = list(buttons_dict.keys())
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        if len(keys) > 5:
            for i in range(0, 6):
                keyboard.add(keys[i])
        else:
            for i in range(0, len(keys)):
                keyboard.add(keys[i])
        keyboard.add('Вернуться в главное меню')
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Выберите время, в которое вам удобно встретиться",
                               parse_mode="HTML",
                               reply_markup=keyboard)


@dp.message_handler(text='Записаться в лист ожидания')
async def extra_pscychologist(message: types.Message):
    list_for_google_sheet.clear()
    list_for_google_sheet.append(message.text)
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Для начала введите свое имя и номер группы в формате\n\n"
                           f"<b>Колесников Дмитрий Михайлович Э305</b>\n\n"
                           f"(каждое слово должно начинаться с заглавной буквы)",
                           parse_mode="HTML")

    await message.delete()


# Обработка нажатий на кнопку
@dp.message_handler(lambda message: message.text in buttons_dict.keys())
async def button_click(message: types.Message):
    end_date = str(buttons_dict[message.text]).split()[0]
    end_date_to_confirm = str(buttons_dict[message.text] + timedelta(hours=16))
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(job, trigger='cron', day_of_week='1,3,5',
                      hour=18, minute=30, end_date=end_date,
                      kwargs={'chat_id': message.from_user.id, 'users_name': message.from_user.full_name,
                              'session_date': message.text, 'kb': psychology_answer_kb})
    kb = InlineKeyboardMarkup().add(InlineKeyboardButton(text='Завершить сеанс', callback_data='end_my_session'))
    scheduler1 = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler1.add_job(feedback_message, trigger='date', run_date=end_date_to_confirm,
                       kwargs={'chat_id': message.from_user.id, 'users_name': message.from_user.full_name,
                               'kb': kb})
    scheduler.start()
    scheduler1.start()
    del buttons_dict[message.text]
    keys = list(buttons_dict.keys())
    if len(keys) >= 0:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        for i in range(0, 6):
            if len(keys) - 1 >= 5:
                keyboard.add(keys[i])
            else:
                pass
        keyboard.add('Вернуться в главное меню')
        list_for_google_sheet.append(message.text)
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Для начала введите свое имя и номер группы в формате\n\n"
                                f"<b>Колесников Дмитрий Михайлович Э305</b>\n\n"
                                f"(каждое слово должно начинаться с заглавной буквы)",
                           parse_mode="HTML")

    await message.delete()


@dp.message_handler()
async def take_user_name(m: types.Message) -> user_name:
    global user_name
    global full_name
    user_name = m.text.split()

    if len(user_name) == 3 and m.text.istitle():
        full_name = m.text
        await bot.send_message(chat_id=m.from_user.id,
                               text=f'Я правильно понимаю, что вас зовут {m.text}',
                               reply_markup=take_user_name_kb)

    elif len(user_name) == 4 and user_name[0] == 'где':
        teachers_name = str(user_name[1] + ' ' + user_name[2] + ' ' + user_name[3])
        await bot.send_message(chat_id=m.from_user.id,
                               text=f'{m.from_user.first_name}, вот, где сегодня будет находиться '
                                    f'<b>{teachers_name}</b>',
                               parse_mode='HTML')
        current_datetime = str(date.today())
        i = 0
        while i < len(sched_w_st):
            if current_datetime == sched_w_st[i]['date'] and teachers_name == sched_w_st[i]['teachers']:
                await bot.send_message(chat_id=m.from_user.id,
                                       text=f"<b>{sched_w_st[i]['place']}</b>\n<b>{sched_w_st[i]['time']}</b>\n"
                                            f"",
                                       parse_mode="HTML")
            i += 1

    elif len(user_name) == 4 and user_name[0] == 'Где':
        teachers_name = str(user_name[1] + ' ' + user_name[2] + ' ' + user_name[3])
        await bot.send_message(chat_id=m.from_user.id,
                               text=f'{m.from_user.first_name}, вот, где сегодня будет находиться '
                                    f'<b>{teachers_name}</b>',
                               parse_mode='HTML')
        current_datetime = str(date.today())
        i = 0
        while i < len(sched_w_st):
            if current_datetime == sched_w_st[i]['date'] and teachers_name == sched_w_st[i]['teachers']:
                await bot.send_message(chat_id=m.from_user.id,
                                       text=f"<b>{sched_w_st[i]['place']}</b>\n<b>{sched_w_st[i]['time']}</b>\n"
                                            f"",
                                       parse_mode="HTML")
            i += 1

    elif len(user_name) == 4 and user_name[0] == 'почта':
        teachers_name = str(user_name[1] + ' ' + user_name[2] + ' ' + user_name[3])
        i = 0
        while i < len(data_all_teachers_and_mails):
            if teachers_name in data_all_teachers_and_mails[i].values():
                await bot.send_message(chat_id=m.from_user.id,
                                       text=f"{m.from_user.first_name}, вот почта"
                                            f": "
                                            f"<b>{data_all_teachers_and_mails[i]['mail']}</b>",
                                       parse_mode="HTML")
            i += 1

    elif len(user_name) == 4 and user_name[0] == 'Почта':
        teachers_name = str(user_name[1] + ' ' + user_name[2] + ' ' + user_name[3])
        i = 0
        while i < len(data_all_teachers_and_mails):
            if teachers_name in data_all_teachers_and_mails[i].values():
                await bot.send_message(chat_id=m.from_user.id,
                                       text=f"{m.from_user.first_name}, вот почта"
                                            f": "
                                            f"<b>{data_all_teachers_and_mails[i]['mail']}</b>",
                                       parse_mode="HTML")
            i += 1

    elif user_name[0] == "Эта":
        photo = open('1.png', 'rb')
        await get_schedule(full_name)
        await bot.send_message(chat_id=m.from_user.id,
                               text=f'Вот ваше расписание на эту неделю, {full_name}')
        await bot.send_photo(chat_id=m.from_user.id,
                             photo=photo)

    elif user_name[0] == "Следующая":
        photo = open('2.png', 'rb')
        await get_schedule(full_name)
        await bot.send_message(chat_id=m.from_user.id,
                               text=f'Вот ваше расписание на следующую неделю, {full_name}')
        await bot.send_photo(chat_id=m.from_user.id,
                             photo=photo)

    elif len(user_name) == 4 and m.text.istitle() and len(user_name[3]) == 4:
        user_tg_id = str(m.from_user.id)
        clients_name = str(user_name[0] + ' ' + user_name[1] + ' ' + user_name[2])
        group_number = str(user_name[3])
        list_for_google_sheet.append(user_tg_id)
        list_for_google_sheet.append(clients_name)
        list_for_google_sheet.append(group_number)
        await bot.send_message(chat_id=m.from_user.id,
                               text=f"Укажите свою почту\n",
                               parse_mode="HTML")

    elif '@' in user_name[0] and '.' in user_name[0][user_name[0].find('@'):]:
        client_mail = str(user_name[0])
        current_time = datetime.now()
        list_for_google_sheet.append(str(current_time))
        list_for_google_sheet.append(client_mail)
        await bot.send_message(chat_id=m.from_user.id,
                               text=f"А теперь расскажите о своей проблеме.\n\n"
                                    f"<b>Эту информацию увидит только психолог</b>.\n\n"
                                    f"Описание проблемы должно содержать от 6 до 50 слов.",
                               parse_mode="HTML")

    elif len(user_name) > 5:
        description_of_the_problem = ""
        for i in range(0, len(user_name)):
            description_of_the_problem += str(user_name[i] + ' ')
        list_for_google_sheet.append(description_of_the_problem)
        if len(list_for_google_sheet) > 7:
            psychology_type = list_for_google_sheet[0]
            time_and_data_type = list_for_google_sheet[1]
            list_for_google_sheet.remove(psychology_type)
            list_for_google_sheet.remove(time_and_data_type)
            list_for_google_sheet.append(time_and_data_type)
            list_for_google_sheet.append(psychology_type)
        else:
            psychology_type = list_for_google_sheet[0]
            del list_for_google_sheet[0]
            list_for_google_sheet.append('None')
            list_for_google_sheet.append(psychology_type)
        list_for_google_sheet.append('.')
        list_for_google_sheet.append(int(1))
        worksheet.append_row(list_for_google_sheet)
        await bot.send_message(chat_id=m.from_user.id,
                               text=f'Вы успешно зарегистрировались на прием!\n'
                                    f'Вот ваши данные:')
        await bot.send_message(chat_id=m.from_user.id,
                               text=f'<b>ФИО</b>: {list_for_google_sheet[1]}\n'
                                    f'<b>Номер группы</b>: {list_for_google_sheet[2]}\n'
                                    f'<b>Электронная почта</b>: {list_for_google_sheet[4]}\n'
                                    f'<b>Проблема</b>: {list_for_google_sheet[5]}\n'
                                    f'<b>Дата и время приема</b>: {list_for_google_sheet[6]}',
                               parse_mode="HTML",
                               reply_markup=psychology_answer_kb)

        await bot.send_message(chat_id=683092826,
                               text=f'<b>ФИО</b>: {list_for_google_sheet[1]}\n'
                                    f'<b>Номер группы</b>: {list_for_google_sheet[2]}\n'
                                    f'<b>Электронная почта</b>: {list_for_google_sheet[4]}\n'
                                    f'<b>Проблема</b>: {list_for_google_sheet[5]}\n'
                                    f'<b>Дата и время приема</b>: {list_for_google_sheet[6]}',
                               parse_mode="HTML")

        if list_for_google_sheet[7] == 'Полина Чибисова':
            await bot.send_message(chat_id=739380400,
                                   text=f'Уважаемая Полина, к вам записался новый человек.\n'
                                        f'Вот его данные:')
            await bot.send_message(chat_id=739380400,
                                   text=f'<b>ФИО</b>: {list_for_google_sheet[1]}\n'
                                        f'<b>Номер группы</b>: {list_for_google_sheet[2]}\n'
                                        f'<b>Электронная почта</b>: {list_for_google_sheet[4]}\n'
                                        f'<b>Проблема</b>: {list_for_google_sheet[5]}\n'
                                        f'<b>Дата и время приема</b>: {list_for_google_sheet[6]}',
                                   parse_mode="HTML")

    return user_name


@dp.callback_query_handler()
async def incorrect_name_func(callback: types.CallbackQuery) -> None:
    telegram_user_name = callback.from_user.first_name
    if callback.data == 'incorrect_name':
        await callback.message.edit_text(text='Попробуй  ввести свое имя еще раз, только давай без ошибок в этот раз\n' +
                                              '👉👈')
    elif callback.data == 'correct_name':
        await callback.message.edit_text(text=f"Если вы хотите узнать расписание на эту неделю, то достаточно нажать на "
                                              f"кнопку:\n"
                                              f" <b>«Эта»</b>.\n\n"
                                              f"Если вы хотите узнать расписание на следующую неделю, то достаточно "
                                              f"нажать на кнопку:\n<b>«Следующая»</b>.\n\n",
                                         parse_mode="HTML",
                                         reply_markup=pic_keyboard)

    elif callback.data == 'where_is_he':
        list_of_teachers_to_find = []
        for item in final_data_of_teachers_to_find:
            try:
                if item['teachers'] not in list_of_teachers_to_find:
                    list_of_teachers_to_find.append(item['teachers'])
                else:
                    pass
            except IndentationError:
                print(f'Ошибка в проведении итерации списка')

        counter_1 = 0
        counter_2 = 0
        kb = InlineKeyboardMarkup()
        lst = []
        for i in sorted(list_of_teachers_to_find):
            try:
                counter_1 += 1
                if counter_1 < 29:
                    lst.append(i)
                elif counter_1 == 29:
                    counter_2 += 1
                    if lst[0][0] != lst[-1][0]:
                        btn = InlineKeyboardButton(text=f'Фамилии на буквы {lst[0][0]}-{lst[-1][0]}',
                                                   callback_data=f'teachers_second_name_to_find_{counter_2}')
                        kb.add(btn)
                        lst = []
                        counter_1 = 0
                    elif lst[0][0] == lst[-1][0]:
                        btn = InlineKeyboardButton(text=f'Фамилии на букву {lst[0][0]}',
                                                   callback_data=f'teachers_second_name_to_find_{counter_2}')
                        kb.add(btn)
                        lst = []
                        counter_1 = 0
            except StopIteration:
                print(f'Ошибка во время итерации')

        await callback.message.edit_text(text=f'Уважаемый(ая) {telegram_user_name}, чтобы узнать, где находится '
                                              f'интересующий вас '
                                              f'преподаватель, достаточно выбрать букву, на '
                                              f'которую начинается его фамилия.',
                                         parse_mode='HTML',
                                         reply_markup=kb)

    elif 'teachers_second_name_to_find_' in callback.data:
        kb = InlineKeyboardMarkup()
        list_of_teachers_to_find = []
        for item in final_data_of_teachers_to_find:
            try:
                if item['teachers'] not in list_of_teachers_to_find:
                    list_of_teachers_to_find.append(item['teachers'])
                else:
                    pass
            except StopIteration:
                print(f'Ошибка в проведении итерации списка')

        list_of_teachers_to_find = sorted(list_of_teachers_to_find)

        try:
            if callback.data[-1] == str(1):
                for name in list_of_teachers_to_find[:29]:
                    btn = InlineKeyboardButton(text=f'{name}', callback_data=f'{dict_of_teachers[name]}')
                    kb.add(btn)
            elif callback.data[-1] != 1 and len(callback.data) == 30:
                i = int(callback.data[-1])
                for name in list_of_teachers_to_find[29 * (i - 1):29 * i]:
                    btn = InlineKeyboardButton(text=f'{name}', callback_data=f'{dict_of_teachers[name]}')
                    kb.add(btn)
            else:
                i = int(callback.data[29:31])
                for name in list_of_teachers_to_find[29 * (i - 1):29 * i]:
                    btn = InlineKeyboardButton(text=f'{name}', callback_data=f'{dict_of_teachers[name]}')
                    kb.add(btn)
        except StopIteration:
            print(f'Ошибка во время итерации')

        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) {callback.from_user.full_name}, теперь выберете имя конкретного '
                                    f'преподавателя, который вас интересует.',
                               parse_mode="HTML",
                               reply_markup=kb)

    elif callback.data in dict_of_teachers.values():
        reversed_dict = {}
        for key, val in dict_of_teachers.items():
            reversed_dict[val] = key
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) {callback.from_user.first_name}, вот, где сегодня будет находиться '
                                    f'<b>{reversed_dict[callback.data]}</b>\n\n'
                                    f'<b>Если не пришло сообщение с местоположением, то преподавателя сегодня нет на '
                                    f'факультете</b>.',
                               parse_mode='HTML')

        def convert_to_datetime(date_string):  ### Функция для преобразования даты в нормальный формат
            try:
                datetime_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
                datetime_obj = datetime_obj.strftime("%Y-%m-%d")
                return datetime_obj
            except ValueError:
                print("Ошибка при преобразовании строки в формате даты и времени")

        teachers_name = reversed_dict[callback.data]
        print(teachers_name)
        current_date = datetime.now().strftime("%Y-%m-%d")
        counter = 0
        try:
            while counter < len(final_data_of_teachers_to_find):
                if teachers_name == final_data_of_teachers_to_find[counter]['teachers']:
                    if current_date == convert_to_datetime(final_data_of_teachers_to_find[counter]['date']):
                        if final_data_of_teachers_to_find[counter]['place'] is not None \
                                and final_data_of_teachers_to_find[counter]['time'] is not None:
                            await bot.send_message(chat_id=callback.from_user.id,
                                                   text=f"<b>{final_data_of_teachers_to_find[counter]['place']}"
                                                        f"</b>\n<b>{final_data_of_teachers_to_find[counter]['time']}"
                                                        f"</b>\n"
                                                        f"",
                                                   parse_mode="HTML")
                        else:
                            await bot.send_message(chat_id=callback.from_user.id,
                                                   text=f'Уважаемый(ая) {callback.from_user.full_name}, к сожалению, '
                                                        f'{reversed_dict[callback.data]} не присутствует на факультете.')
                            print(f"{final_data_of_teachers_to_find[counter]['place']}, "
                                  f"{final_data_of_teachers_to_find[counter]['time']}")
                counter += 1

        except StopIteration:
            print(f'Ошибка во время итерации')

    elif callback.data == 'prepod_email':
        btn = [
            InlineKeyboardButton(text="Фамилии на буквы А-В", callback_data='second_name_A'), ### перввые 21 элемениов
            InlineKeyboardButton(text="Фамилии на буквы В-И", callback_data='second_name_BV'), ### с 21 по 50
            InlineKeyboardButton(text="Фамилии на буквы И-К", callback_data='second_name_GD'), ### с 51 по 80
            InlineKeyboardButton(text="Фамилии на буквы К-М", callback_data='second_name_EI'), ### с 81 по 105
            InlineKeyboardButton(text="Фамилии на буквы М-П", callback_data='second_name_K'), ### с 106 по 135
            InlineKeyboardButton(text="Фамилии на буквы П-С", callback_data='second_name_KL'), ### `с 136 по 165
            InlineKeyboardButton(text='Фамилии на буквы С-Ч', callback_data='second_name_LM'), ### с 166 по 195
            InlineKeyboardButton(text='Фамилии на буквы Ч-Э', callback_data='second_name_M') ###с 196 по 202
        ]
        kb = InlineKeyboardMarkup()
        for i in range(len(btn)):
            kb.add(btn[i])
        await callback.message.edit_text(text=f'Уважаемый(ая) {telegram_user_name}, чтобы узнать '
                                              f'почту интересующего вас '
                                              f'преподавателя, достаточно выбрать букву, на '
                                              f'которую начинается его фамилия.',
                                         parse_mode='HTML',
                                         reply_markup=kb)

    elif callback.data == 'second_name_A':
        counter = 0
        kb = InlineKeyboardMarkup()
        for key, val in teachers_dict_1.items():
            if counter <= 21:
                btn = InlineKeyboardButton(text=f'{key}', callback_data=f'{val}')
                kb.add(btn)
                counter += 1

        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) {callback.from_user.full_name}, для того, чтобы узнать почту '
                                    f'интересующего вас преподавателя, достаточно нажать на его имя.',
                               reply_markup=kb)

    elif callback.data == 'second_name_BV':
        counter = 0
        kb = InlineKeyboardMarkup()
        for key, val in teachers_dict_1.items():
            counter += 1
            if counter > 21 and counter <= 50:
                btn = InlineKeyboardButton(text=f'{key}', callback_data=f'{val}')
                kb.add(btn)

        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) {callback.from_user.full_name}, для того, чтобы узнать почту '
                                    f'интересующего вас преподавателя, достаточно нажать на его имя.',
                               reply_markup=kb)

    elif callback.data == 'second_name_GD':
        counter = 0
        kb = InlineKeyboardMarkup()
        for key, val in teachers_dict_1.items():
            counter += 1
            if counter > 51 and counter <= 80:
                btn = InlineKeyboardButton(text=f'{key}', callback_data=f'{val}')
                kb.add(btn)

        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) {callback.from_user.full_name}, для того, чтобы узнать почту '
                                    f'интересующего вас преподавателя, достаточно нажать на его имя.',
                               reply_markup=kb)

    elif callback.data == 'second_name_EI':
        counter = 0
        kb = InlineKeyboardMarkup()
        for key, val in teachers_dict_1.items():
            counter += 1
            if counter > 80 and counter <= 105:
                btn = InlineKeyboardButton(text=f'{key}', callback_data=f'{val}')
                kb.add(btn)

        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) {callback.from_user.full_name}, для того, чтобы узнать почту '
                                    f'интересующего вас преподавателя, достаточно нажать на его имя.',
                               reply_markup=kb)

    elif callback.data == 'second_name_K':
        counter = 0
        kb = InlineKeyboardMarkup()
        for key, val in teachers_dict_1.items():
            counter += 1
            if counter > 105 and counter <= 135:
                btn = InlineKeyboardButton(text=f'{key}', callback_data=f'{val}')
                kb.add(btn)

        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) {callback.from_user.full_name}, для того, чтобы узнать почту '
                                    f'интересующего вас преподавателя, достаточно нажать на его имя.',
                               reply_markup=kb)

    elif callback.data == 'second_name_KL':
        counter = 0
        kb = InlineKeyboardMarkup()
        for key, val in teachers_dict_1.items():
            counter += 1
            if counter > 135 and counter <= 165:
                btn = InlineKeyboardButton(text=f'{key}', callback_data=f'{val}')
                kb.add(btn)

        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) {callback.from_user.full_name}, для того, чтобы узнать почту '
                                    f'интересующего вас преподавателя, достаточно нажать на его имя.',
                               reply_markup=kb)

    elif callback.data == 'second_name_LM':
        counter = 0
        kb = InlineKeyboardMarkup()
        for key, val in teachers_dict_1.items():
            counter += 1
            if counter > 165 and counter <= 191:
                btn = InlineKeyboardButton(text=f'{key}', callback_data=f'{val}')
                kb.add(btn)

        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) {callback.from_user.full_name}, для того, чтобы узнать почту '
                                    f'интересующего вас преподавателя, достаточно нажать на его имя.',
                               reply_markup=kb)

    elif callback.data == 'second_name_M':
        counter = 0
        kb = InlineKeyboardMarkup()
        for key, val in teachers_dict_1.items():
            counter += 1
            if counter > 191 and counter <= 202:
                btn = InlineKeyboardButton(text=f'{key}', callback_data=f'{val}')
                kb.add(btn)

        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) {callback.from_user.full_name}, для того, чтобы узнать почту '
                                    f'интересующего вас преподавателя, достаточно нажать на его имя.',
                               reply_markup=kb)

    elif callback.data in teachers_dict_1.values():
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) {callback.from_user.full_name}, вот <b>контактные данные</b>, '
                                    f'интересующего вас '
                                    f'преподавателя: <b>{callback.data}</b>.\n\n'
                                    f'Будьте <b>воспитанными</b> студентами и <b>не пишите</b> преподавателям'
                                    f' <b>в ночи</b>!',
                               parse_mode="HTML",
                               reply_markup=kb_main)

    elif callback.data == 'first_pair':
        current_time = '09:00-10:30'
        current_date = str(date.today())
        for i in range(len(sched_w_st)):
            if sched_w_st[i]['date'] == current_date and sched_w_st[i]['time'] == current_time:
                if sched_w_st[i]['place'].startswith('1') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_first_flour:
                    list_of_kabs_first_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('2') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_second_flour:
                    list_of_kabs_second_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('3') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_third_flour:
                    list_of_kabs_third_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('4') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_fourth_flour:
                    list_of_kabs_fourth_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('5') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_fith_flour:
                    list_of_kabs_fith_flour.remove(str(sched_w_st[i]['place']))

        await callback.message.edit_text(text=f"{telegram_user_name}, вот список кабинетов, доступных на <b>первой "
                                              f"паре</b>: \n\n"
                                              f"<b>Первый этаж</b>: \n{', '.join(map(str, list_of_kabs_first_flour))}\n",
                                         parse_mode='HTML')
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Второй этаж: \n{', '.join(map(str, list_of_kabs_second_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Третий этаж: \n{', '.join(map(str, list_of_kabs_third_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Четвертый этаж: \n{', '.join(map(str, list_of_kabs_fourth_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Пятый этаж: \n{', '.join(map(str, list_of_kabs_fith_flour))}\n",
                               )

    elif callback.data == 'second_pair':
        current_time = '10:40-12:10'
        current_date = str(date.today())
        for i in range(len(sched_w_st)):
            if sched_w_st[i]['date'] == current_date and sched_w_st[i]['time'] == current_time:
                if sched_w_st[i]['place'].startswith('1') and str(sched_w_st[i]['place']) in \
                            list_of_kabs_first_flour:
                    list_of_kabs_first_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('2') and str(sched_w_st[i]['place']) in \
                            list_of_kabs_second_flour:
                    list_of_kabs_second_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('3') and str(sched_w_st[i]['place']) in \
                            list_of_kabs_third_flour:
                    list_of_kabs_third_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('4') and str(sched_w_st[i]['place']) in \
                            list_of_kabs_fourth_flour:
                    list_of_kabs_fourth_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('5') and str(sched_w_st[i]['place']) in \
                            list_of_kabs_fith_flour:
                    list_of_kabs_fith_flour.remove(str(sched_w_st[i]['place']))

        await callback.message.edit_text(text=f"{telegram_user_name}, вот список кабинетов, доступных на <b>второй "
                                              f"паре</b>:\n\n"
                                              f"<b>Первый этаж</b>: \n{', '.join(map(str, list_of_kabs_first_flour))}\n",
                                         parse_mode='HTML')
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Второй этаж: \n{', '.join(map(str, list_of_kabs_second_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Третий этаж: \n{', '.join(map(str, list_of_kabs_third_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Четвертый этаж: \n{', '.join(map(str, list_of_kabs_fourth_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Пятый этаж: \n{', '.join(map(str, list_of_kabs_fith_flour))}\n",
                              )

    elif callback.data == 'third_pair':
        current_time = '12:20-13:50'
        current_date = str(date.today())
        for i in range(len(sched_w_st)):
            if sched_w_st[i]['date'] == current_date and sched_w_st[i]['time'] == current_time:
                if sched_w_st[i]['place'].startswith('1') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_first_flour:
                    list_of_kabs_first_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('2') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_second_flour:
                    list_of_kabs_second_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('3') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_third_flour:
                    list_of_kabs_third_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('4') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_fourth_flour:
                    list_of_kabs_fourth_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('5') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_fith_flour:
                    list_of_kabs_fith_flour.remove(str(sched_w_st[i]['place']))

        await callback.message.edit_text(text=f"{telegram_user_name}, вот список кабинетов, доступных на <b>третьей "
                                              f"паре</b>:\n\n"
                                              f"<b>Первый этаж</b>: \n{', '.join(map(str, list_of_kabs_first_flour))}\n",
                                         parse_mode='HTML')
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Второй этаж: \n{', '.join(map(str, list_of_kabs_second_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Третий этаж: \n{', '.join(map(str, list_of_kabs_third_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Четвертый этаж: \n{', '.join(map(str, list_of_kabs_fourth_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Пятый этаж: \n{', '.join(map(str, list_of_kabs_fith_flour))}\n",
                               )

    elif callback.data == 'forth_pair':
        current_time = '14:00-15:30'
        current_date = str(date.today())
        for i in range(len(sched_w_st)):
            if sched_w_st[i]['date'] == current_date and sched_w_st[i]['time'] == current_time:
                if sched_w_st[i]['place'].startswith('1') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_first_flour:
                    list_of_kabs_first_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('2') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_second_flour:
                    list_of_kabs_second_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('3') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_third_flour:
                    list_of_kabs_third_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('4') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_fourth_flour:
                    list_of_kabs_fourth_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('5') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_fith_flour:
                    list_of_kabs_fith_flour.remove(str(sched_w_st[i]['place']))

        await callback.message.edit_text(text=f"{telegram_user_name}, вот список кабинетов, доступных на <b>четвертой "
                                              f"паре</b>:\n\n"
                                              f"<b>Первый этаж</b>: \n{', '.join(map(str, list_of_kabs_first_flour))}\n",
                                         parse_mode='HTML')
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Второй этаж: \n{', '.join(map(str, list_of_kabs_second_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Третий этаж: \n{', '.join(map(str, list_of_kabs_third_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Четвертый этаж: \n{', '.join(map(str, list_of_kabs_fourth_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Пятый этаж: \n{', '.join(map(str, list_of_kabs_fith_flour))}\n",
                               )

    elif callback.data == 'fifth_pair':
        current_time = '15:40-17:10'
        current_date = str(date.today())
        for i in range(len(sched_w_st)):
            if sched_w_st[i]['date'] == current_date and sched_w_st[i]['time'] == current_time:
                if sched_w_st[i]['place'].startswith('1') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_first_flour:
                    list_of_kabs_first_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('2') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_second_flour:
                    list_of_kabs_second_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('3') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_third_flour:
                    list_of_kabs_third_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('4') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_fourth_flour:
                    list_of_kabs_fourth_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('5') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_fith_flour:
                    list_of_kabs_fith_flour.remove(str(sched_w_st[i]['place']))

        await callback.message.edit_text(text=f"{telegram_user_name}, вот список кабинетов, доступных на <b>пятой "
                                              f"паре</b>:\n\n"
                                              f"<b>Первый этаж</b>: \n{', '.join(map(str, list_of_kabs_first_flour))}\n",
                                         parse_mode='HTML')
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Второй этаж: \n{', '.join(map(str, list_of_kabs_second_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Третий этаж: \n{', '.join(map(str, list_of_kabs_third_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Четвертый этаж: \n{', '.join(map(str, list_of_kabs_fourth_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Пятый этаж: \n{', '.join(map(str, list_of_kabs_fith_flour))}\n",
                               )

    elif callback.data == 'six_pair':
        current_time = '17:20-18:50'
        current_date = str(date.today())
        for i in range(len(sched_w_st)):
            if sched_w_st[i]['date'] == current_date and sched_w_st[i]['time'] == current_time:
                if sched_w_st[i]['place'].startswith('1') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_first_flour:
                    list_of_kabs_first_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('2') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_second_flour:
                    list_of_kabs_second_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('3') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_third_flour:
                    list_of_kabs_third_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('4') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_fourth_flour:
                    list_of_kabs_fourth_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('5') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_fith_flour:
                    list_of_kabs_fith_flour.remove(str(sched_w_st[i]['place']))

        await callback.message.edit_text(text=f"{telegram_user_name}, вот список кабинетов, доступных на <b>шестой "
                                              f"паре</b>:\n\n"
                                              f"<b>Первый этаж</b>: \n{', '.join(map(str, list_of_kabs_first_flour))}\n",
                                         parse_mode='HTML')
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Второй этаж: \n{', '.join(map(str, list_of_kabs_second_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Третий этаж: \n{', '.join(map(str, list_of_kabs_third_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Четвертый этаж: \n{', '.join(map(str, list_of_kabs_fourth_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Пятый этаж: \n{', '.join(map(str, list_of_kabs_fith_flour))}\n",
                               )

    elif callback.data == 'seventh_pair':
        current_time = '18:55-20:25'
        current_date = str(date.today())
        for i in range(len(sched_w_st)):
            if sched_w_st[i]['date'] == current_date and sched_w_st[i]['time'] == current_time:
                if sched_w_st[i]['place'].startswith('1') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_first_flour:
                    list_of_kabs_first_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('2') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_second_flour:
                    list_of_kabs_second_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('3') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_third_flour:
                    list_of_kabs_third_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('4') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_fourth_flour:
                    list_of_kabs_fourth_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('5') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_fith_flour:
                    list_of_kabs_fith_flour.remove(str(sched_w_st[i]['place']))

        await callback.message.edit_text(text=f"{telegram_user_name}, вот список кабинетов, доступных на <b>седьмой "
                                              f"паре</b>:\n\n"
                                              f"<b>Первый этаж</b>: \n{', '.join(map(str, list_of_kabs_first_flour))}\n",
                                         parse_mode='HTML')
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Второй этаж: \n{', '.join(map(str, list_of_kabs_second_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Третий этаж: \n{', '.join(map(str, list_of_kabs_third_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Четвертый этаж: \n{', '.join(map(str, list_of_kabs_fourth_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Пятый этаж: \n{', '.join(map(str, list_of_kabs_fith_flour))}\n",
                               )

    elif callback.data == 'eight_pair':
        current_time = '20:30-22:00'
        current_date = str(date.today())
        for i in range(len(sched_w_st)):
            if sched_w_st[i]['date'] == current_date and sched_w_st[i]['time'] == current_time:
                if sched_w_st[i]['place'].startswith('1') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_first_flour:
                    list_of_kabs_first_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('2') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_second_flour:
                    list_of_kabs_second_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('3') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_third_flour:
                    list_of_kabs_third_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('4') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_fourth_flour:
                    list_of_kabs_fourth_flour.remove(str(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('5') and str(sched_w_st[i]['place']) in \
                        list_of_kabs_fith_flour:
                    list_of_kabs_fith_flour.remove(str(sched_w_st[i]['place']))

        await callback.message.edit_text(text=f"{telegram_user_name}, вот список кабинетов, доступных на <b>восьмой "
                                              f"паре</b>:\n\n"
                                              f"<b>Первый этаж</b>: \n{', '.join(map(str, list_of_kabs_first_flour))}\n",
                                         parse_mode='HTML')
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Второй этаж: \n{', '.join(map(str, list_of_kabs_second_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Третий этаж: \n{', '.join(map(str, list_of_kabs_third_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Четвертый этаж: \n{', '.join(map(str, list_of_kabs_fourth_flour))}\n",
                               )
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"Пятый этаж: \n{', '.join(map(str, list_of_kabs_fith_flour))}\n",
                               )

    elif callback.data == 'official':
        await callback.message.answer(text=f'{telegram_user_name}, вот список мероприятий, которые предлагают '
                                           f'<b>МГУ</b>:',
                                      parse_mode='HTML')
        df = pd.read_excel('Chill_timetable.xlsx', sheet_name='Лист1')
        for i, row in df.iterrows():
            if row['Activity'] != 'Nothing':
                await bot.send_message(chat_id=callback.from_user.id,
                                       text=f"{row['Data']} ({row['Weekday']}) - {row['Activity']}")

    elif callback.data == 'unofficial':
        await callback.message.answer(text=f'{telegram_user_name}, вот список мероприятий, которые предлагают наши '
                                           f'<b>студенты</b>:',
                                      parse_mode='HTML')
        await callback.message.answer(text=f'Пока ничего нового нет')

    elif callback.data == 'this':
        await callback.message.edit_reply_markup(reply_markup=None)

        photo = open('1.png', 'rb')
        await get_schedule(full_name)
        await bot.send_message(chat_id=callback.message.chat.id,
                               text=f'Вот ваше расписание на эту неделю, {full_name}')
        await bot.send_photo(chat_id=callback.message.chat.id,
                             photo=photo)

    elif callback.data == 'next':
        await callback.message.edit_reply_markup(reply_markup=None)

        photo = open('2.png', 'rb')
        await get_schedule(full_name)
        await bot.send_message(chat_id=callback.message.chat.id,
                               text=f'Вот ваше расписание на следующую неделю, {full_name}')
        await bot.send_photo(chat_id=callback.message.chat.id,
                             photo=photo)

    elif callback.data == 'cancel_order':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) {callback.from_user.full_name}, вы уверены, что хотите отменить '
                                    f'встречу с психологом?',
                               parse_mode="HTML",
                               reply_markup=psychology_order_confirmation_kb)

    elif callback.data == 'free_orders':
        cell_list = worksheet.findall(str(callback.from_user.id))
        amount_of_orders = len(cell_list)
        if amount_of_orders == 1:
            await bot.send_message(chat_id=callback.from_user.id,
                                   text=f'Увважвемый(ая) {callback.from_user.full_name}, у вас осталась ровно '
                                        f'<b>{amount_of_orders}</b> бесплатная встреча с психологом.',
                                   parse_mode="HTML")
        else:
            await bot.send_message(chat_id=callback.from_user.id,
                                   text=f'Уважаемый(ая) {callback.from_user.full_name}, у вас <b>не осталось</b> '
                                        f'бесплатных попыток.',
                                   parse_mode="HTML")
            await bot.send_message(chat_id=callback.from_user.id,
                                   text=f'Уважаемый(ая) {callback.from_user.full_name}, две сессии в рамках '
                                        f'бесплатного консультирования состоялись, '
                                        f'для продолжения работы со специалистом пишите на '
                                        f'почту <b>chibisova.polina@mail.ru</b>',
                                   parse_mode="HTML",
                                   reply_markup=kb_main)

        await callback.message.delete()

    elif callback.data == 'accidentally_clicked':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(а) <b>{callback.from_user.full_name}</b>, ваша запись'
                                    f' к психологу сохранилась',
                               parse_mode="HTML",
                               reply_markup=kb_main)
        await callback.message.delete()

    elif callback.data == 'trully_cancel_order':
        await callback.message.delete()
        cell_list = worksheet.findall(str(callback.from_user.id))
        row_number = cell_list[-1].row
        column_number = cell_list[-1].col
        student_name = worksheet.cell(row_number, column_number + 1).value
        student_group = worksheet.cell(row_number, column_number + 2).value
        student_email = worksheet.cell(row_number, column_number + 4).value
        student_problem = worksheet.cell(row_number, column_number + 5).value
        student_meeting_data = str(worksheet.cell(row_number, column_number + 6).value)
        if datetime.now() <= buttons_dict_copy[student_meeting_data] - timedelta(hours=24):
            worksheet.update_cell(row_number, column_number + 8, f'Отмена записи произошла в {datetime.now()} раньше, '
                                                                 f'чем за 24 часа до встречи. Никаких штрафов нет.')
            await bot.send_message(chat_id=callback.from_user.id,
                                   text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, вы отменили '
                                        f'встречу.\n\n'
                                        f'Штрафов за отмену у вас <b>нет</b>. \n\n'
                                        f'Психолог получил уведомление об отмене.',
                                   parse_mode="HTML",
                                   reply_markup=kb_main)

            await bot.send_message(chat_id=739380400,
                                   text=f'Уважаемая Полина, данный человек <b>отказался</b> от встречи с вами.\n'
                                        f'Штрафов за отмену у человека нет, так как отмена произошла за 24 часа до '
                                        f'встречи с вами\n'
                                        f'Вот его данные:',
                                   parse_mode="HTML")
            await bot.send_message(chat_id=739380400,
                                   text=f'<b>ФИО</b>: {student_name}\n'
                                        f'<b>Номер группы</b>: {student_group}\n'
                                        f'<b>Электронная почта</b>: {student_email}\n'
                                        f'<b>Проблема</b>: {student_problem}\n'
                                        f'<b>Дата и время приема</b>: {student_meeting_data}',
                                   parse_mode="HTML")
            await bot.send_message(chat_id=683092826,
                                   text=f'Уважаемый Дмитрий, данный человек <b>отказался</b> от встречи с вами.\n'
                                        f'Штрафов за отмену у человека нет, так как отмена произошла за 24 часа до '
                                        f'встречи с вами\n'
                                        f'Вот его данные:',
                                   parse_mode="HTML")
            await bot.send_message(chat_id=683092826,
                                   text=f'<b>ФИО</b>: {student_name}\n'
                                        f'<b>Номер группы</b>: {student_group}\n'
                                        f'<b>Электронная почта</b>: {student_email}\n'
                                        f'<b>Проблема</b>: {student_problem}\n'
                                        f'<b>Дата и время приема</b>: {student_meeting_data}',
                                   parse_mode="HTML")

            for i in range(0, 10):
                worksheet.update_cell(row_number, column_number + i, '')

        else:
            worksheet.update_cell(row_number, column_number + 8, f'Отмена записи произошла в {datetime.now()} позже, '
                                                                 f'чем за 24 часа до встречи. Есть штраф')

            await bot.send_message(chat_id=callback.from_user.id,
                                   text=f'Уважаемый(ая) <b>{callback.from_user.full_name}</b>, вы отменили '
                                        f'встречу.\n\n'
                                        f'У вас <b>есть</b> штраф за отмену встречи, потому что отмену надо '
                                        f'производить не позднее, чем за 24 часа! \n\n'
                                        f'Психолог получил уведомление об отмене.',
                                   parse_mode="HTML",
                                   reply_markup=kb_main)

            await bot.send_message(chat_id=739380400,
                                   text=f'Уважаемая Полина, данный человек <b>отказался</b> от встречи с вами.\n'
                                        f'У человека есть штраф за отмену, так как отмена произошла позднее чем за 24 '
                                        f'часа до '
                                        f'встречи с вами\n'
                                        f'Вот его данные:',
                                   parse_mode="HTML")
            await bot.send_message(chat_id=739380400,
                                   text=f'<b>ФИО</b>: {student_name}\n'
                                        f'<b>Номер группы</b>: {student_group}\n'
                                        f'<b>Электронная почта</b>: {student_email}\n'
                                        f'<b>Проблема</b>: {student_problem}\n'
                                        f'<b>Дата и время приема</b>: {student_meeting_data}',
                                   parse_mode="HTML")

            await bot.send_message(chat_id=683092826,
                                   text=f'Уважаемый Дмитрий, данный человек <b>отказался</b> от встречи с вами.\n'
                                        f'У человека есть штраф за отмену, так как отмена произошла позднее чем за 24 '
                                        f'часа до '
                                        f'встречи с вами\n'
                                        f'Вот его данные:',
                                   parse_mode="HTML")
            await bot.send_message(chat_id=683092826,
                                   text=f'<b>ФИО</b>: {student_name}\n'
                                        f'<b>Номер группы</b>: {student_group}\n'
                                        f'<b>Электронная почта</b>: {student_email}\n'
                                        f'<b>Проблема</b>: {student_problem}\n'
                                        f'<b>Дата и время приема</b>: {student_meeting_data}',
                                   parse_mode="HTML")

    elif callback.data == 'end_my_session':
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f'Уважаемый(ая) {callback.from_user.full_name}, вы <b>завершили '
                                    f'встречу</b> с психологом.\n\n'
                                    f'Мы надеемся вам все понравилось и <b>желаем хорошего дня!</b>',
                               parse_mode="HTML",
                               reply_markup=kb_main)

        await callback.message.delete()


if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)


