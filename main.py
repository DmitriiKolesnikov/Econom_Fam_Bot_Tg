import pandas as pd
from aiogram import Bot, executor, Dispatcher, types
from Main_kb import kb_main, pic_keyboard
from Kafedri_data import inline_kb_kafedri
from Take_user_name_inline_kb import take_user_name_kb
from Prepodi_inline_kb import prepodi_kb
from Free_room_kb import free_room_kb
from Meropriatia_kb import meropriatia_kb
from Json_data import sched_w_st, data_all_teachers_and_mails
from Google_sheet import *
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from sercher_cacsa import get_schedule
from datetime import date
from kabs_data_and_logic import list_of_kabs_first_flour, list_of_kabs_second_flour, \
    list_of_kabs_third_flour, list_of_kabs_fourth_flour, list_of_kabs_fith_flour

TOKEN_API = '6431263054:AAG5luZr2VIGwYPIiBJ4QHxEAwSKH-iil70'


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


user_name = ''

buttons = ['Среда 11 октября 2023, 14:00', 'Среда 11 октября 2023, 15:00',
           'Среда 11 октября 2023, 16:00', 'Среда 18 октября 2023, 14:00',
           'Среда 18 октября 2023, 15:00', 'Среда 18 октября 2023, 16:00',
           'Среда 25 октября 2023, 14:00', 'Среда 25 октября 2023, 15:00',
           'Среда 25 октября 2023, 16:00']
psychologist = ['Полина Чибисова', 'Записаться в лист ожидания']
list_for_google_sheet = []


async def on_startup(_):
    print('Bot started')



async def delay_reminder(chat_id: int):
    await bot.send_message(chat_id=chat_id,
                           text=f'Уважаемый пользователь, напоминаю вам о записи к психологу')


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
                                 '4. Помогу ознакомиться со всеми кафедрами экономического факультета, возможно, вам '
                                 'это '
                                 'поможет в дальнейшем.\n\n'
                                 '5. Совместными усилиями с нашим факультетом поможем вам устроиться на работу.\n\n'
                                 '6. Постараюсь не допустить депрессивных мыслей во время обучения в МГУ с помощью на'
                                 'шего '
                                 'психолога. Грустить - вредно!\n\n'
                                 'Что бы более подробно узнать о возможностях бота, нажмите \n/description',
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
                                    
                                 'С помощью кнопки «Кафедры ЭФ МГУ» вы познакомитесь со всеми кафедрами факультета. '
                                 'Это вам сильно поможет при написании курсовой работы и диплома))). \n\n'
                                    
                                 'С помощью кнопки «Помощь с работой» вы сможете найти себе официальную стажировку. '
                                 'В этом вам поможет сам ЭФ МГУ. \n\n'
                                    
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


@dp.message_handler(text='Кафедры ЭФ МГУ')
async def kafedri_command(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id,
                         caption='Здесь можно ознакомиться со списком кафедр,'
                                 'представленных на экономическом факультете.\n'
                                 'Чтобы узнать больше о каждой из них, достаточно '
                                 'нажать на понравившуюся вам!',
                         photo='https://www.msu.ru/info/map/images/46/photo4.jpg',
                         reply_markup=inline_kb_kafedri)
    await message.delete()


@dp.message_handler(text='💰Помощь с работой')
async def stagirovki_command(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id,
                         caption=f'Сегодня Служба содействия трудоустройству имеет широкие контакты с компаниями, '
                                 f'заинтересованными в выпускниках факультета. Список компаний и сфер их деятельности'
                                 f' постоянно расширяется - в экономистах и менеджерах нуждаются  компании практически'
                                 f' любого профиля. При этом наиболее активными партнерами Факультета являются '
                                 f'бухгалтерские/аудиторские компании, финансовые организации, страховые компании, '
                                 f'производители продуктов и товаров народного потребления, компании, специализирующиеся'
                                 f' на недвижимости, кадровые, телекоммуникационные компании, государственные и '
                                 f'научно-исследовательские структуры. Для более подробной информациии и помощи, '
                                 f'перейдите'
                                 f'по ссылке'+' https://www.econ.msu.ru/students/eas/',
                         photo='https://sravni-news-prod.storage.yandexcloud.net/uploads/2021/12/127523-n42lmrytsk5f'
                               '8acijhwp.jpg')
    await message.delete()
    

# метод для обработки команды гугл шит
@dp.message_handler(text='⌛Психологическая помощь')
async def google_sheet_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         caption='👩🏼 '+'‍К специалисту можно записаться и прийти на консультацию, чтобы поработать '
                                 'с внутренними переживаниями или поделиться накопившимися мыслями и эмоциями.'
                                 ' ⌛ '+'Продолжительность сеанса — около 50 минут '
                                 'Если вам нужна помощь в разрешении какой-либо возникшей проблемы и вы бы хотели '
                                 'получить психологическую поддержку, заполните, пожалуйста, анкету, которая будет '
                                 'предложена ниже.',
                         photo='https://babr24.com/n2p/i/2021/1/21_1_5_2_05132453_b.jpg')
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Прием осуществляется по средам с 14.00 до 17.00 (ауд 447)\n"
                                f"На беседу с каждым человеком выделено 50 минут.\n\n"
                                f"<b>ВАЖНО</b>: пока у нас только один психолог, Чибисова Полина. "
                                f"Если Вы знакомы с ней лично, она не сможет к сожалению с Вами работать. "
                                f"В этом случае <b>не надо</b> записываться на время, "
                                f"<b>запишитесь в лист ожидания</b>.\n\n"
                                f"У Вас есть возможность записаться на <b>2 бесплатные встречи</b>. "
                                f"Записаться на прием  можно не позже, чем за 48 часов до встречи."
                                f"Если Вам необходимо будет перенести или отменить встречу, "
                                f"пожалуйста, <b>напишите об этом за 48 часов до начала сессии</b> "
                                f"боту с помощью сообщения "
                                f"<b>'Удали мою запись'</b>, иначе встреча будет считаться состоявшейся "
                                f"(переносить/отменять встречи можно не более 1 раза). "
                                f"При опоздании встреча не продлевается. <b>Не опаздывайте!</b>",
                           parse_mode="HTML")
    psychologist_keaboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    psychologist_keaboard.add(*psychologist)
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Выберите психолога, с которым вы хотите встретиться',
                           parse_mode="HTML",
                           reply_markup=psychologist_keaboard)


@dp.message_handler(text="Полина Чибисова")
async def main_psychologist(message: types.Message):
    list_for_google_sheet.clear()
    list_for_google_sheet.append(message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*buttons[:4])
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


# Обработка нажатий на кнопки
@dp.message_handler(lambda message: message.text in buttons)
async def button_click(message: types.Message):
    buttons.remove(message.text)
    if len(buttons) >= 0:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(*buttons[:3])
        list_for_google_sheet.append(message.text)
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Для начала введите свое имя и номер группы в формате\n\n"
                                f"<b>Колесников Дмитрий Михайлович Э305</b>\n\n"
                                f"(каждое слово должно начинаться с заглавной буквы)",
                           parse_mode="HTML")

#
# @dp.message_handler()
# async def fill_name_and_group(m: types.Message):
#     user_name = m.text.split()
#
#     if len(user_name) == 4 and m.text.istitle() and len(user_name[3]) == 4:
#         user_tg_id = str(m.from_user.id)
#         clients_name = str(user_name[0] + ' ' + user_name[1] + ' ' + user_name[2])
#         group_number = str(user_name[3])
#         list_for_google_sheet.append(user_tg_id)
#         list_for_google_sheet.append(clients_name)
#         list_for_google_sheet.append(group_number)
#         await bot.send_message(chat_id=m.from_user.id,
#                                text=f"Укажите свою почту\n",
#                                parse_mode="HTML")
#
#     elif '@' in user_name[0] and '.' in user_name[0][user_name[0].find('@'):]:
#         client_mail = str(user_name[0])
#         current_time = datetime.now()
#         list_for_google_sheet.append(str(current_time))
#         list_for_google_sheet.append(client_mail)
#         await bot.send_message(chat_id=m.from_user.id,
#                                text=f"А теперь расскажите о своей проблеме.\n\n"
#                                     f"<b>Эту информацию увидит только психолог </b>.\n\n"
#                                     f"Описание проблемы должно содержать от 6 до 50 слов.",
#                                parse_mode="HTML")
#
#     elif len(user_name) > 5:
#         description_of_the_problem = ""
#         for i in range(0, len(user_name)):
#             description_of_the_problem += str(user_name[i] + ' ')
#         list_for_google_sheet.append(description_of_the_problem)
#         if len(list_for_google_sheet) > 7:
#             psychology_type = list_for_google_sheet[0]
#             time_and_data_type = list_for_google_sheet[1]
#             list_for_google_sheet.remove(psychology_type)
#             list_for_google_sheet.remove(time_and_data_type)
#             list_for_google_sheet.append(time_and_data_type)
#             list_for_google_sheet.append(psychology_type)
#         else:
#             psychology_type = list_for_google_sheet[0]
#             del list_for_google_sheet[0]
#             list_for_google_sheet.append('None')
#             list_for_google_sheet.append(psychology_type)
#         worksheet.append_row(list_for_google_sheet)
#         await bot.send_message(chat_id=m.from_user.id,
#                                text=f'Вы успешно зарегистрировались на прием!\n'
#                                     f'Вот ваши данные:')
#         await bot.send_message(chat_id=m.from_user.id,
#                                text=f'ФИО: {list_for_google_sheet[1]}\n'
#                                     f'Номер группы: {list_for_google_sheet[2]}\n'
#                                     f'Электронная почта: {list_for_google_sheet[4]}\n'
#                                     f'Проблема: {list_for_google_sheet[5]}\n'
#                                     f'Дата и время приема: {list_for_google_sheet[6]}')
#
#         if list_for_google_sheet[7] == 'Полина Чибисова':
#             await bot.send_message(chat_id=739380400,
#                                    text=f'Уважаемая Полина, к вам записался новый человек.\n'
#                                         f'Вот его данные:')
#             await bot.send_message(chat_id=739380400,
#                                    text=f'ФИО: {list_for_google_sheet[1]}\n'
#                                         f'Номер группы: {list_for_google_sheet[2]}\n'
#                                         f'Электронная почта: {list_for_google_sheet[4]}\n'
#                                         f'Проблема: {list_for_google_sheet[5]}\n'
#                                         f'Дата и время приема: {list_for_google_sheet[6]}')
#
#         if list_for_google_sheet[6] == 'Среда 11 октября 2023, 14:00' or list_for_google_sheet[
#             6] == 'Среда 11 октября 2023, 15:00' or list_for_google_sheet[6] == 'Среда 11 октября 2023, 16:00':
#             scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
#             scheduler.add_job(delay_reminder, trigger='cron', day_of_week='0, 1, 4', hour='18', minute='30',
#                               end_date='2023-10-11', kwargs={'chat_id': m.from_user.id})
#             scheduler.start()
#
#         if list_for_google_sheet[6] == 'Среда 18 октября 2023, 14:00' or list_for_google_sheet[
#             6] == 'Среда 18 октября 2023, 15:00' or list_for_google_sheet[6] == 'Среда 18 октября 2023, 16:00':
#             scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
#             scheduler.add_job(delay_reminder, trigger='cron', day_of_week='0, 1, 4', hour='18', minute='30',
#                               end_date='2023-10-18', kwargs={'chat_id': m.from_user.id})
#             scheduler.start()
#
#         if list_for_google_sheet[6] == 'Среда 25 октября 2023, 14:00' or list_for_google_sheet[
#             6] == 'Среда 25 октября 2023, 15:00' or list_for_google_sheet[6] == 'Среда 25 октября 2023, 16:00':
#             scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
#             scheduler.add_job(delay_reminder, trigger='cron', day_of_week='0, 1, 4', hour='18', minute='30',
#                               end_date='2023-10-25', kwargs={'chat_id': m.from_user.id})
#             scheduler.start()
#
#     elif user_name[0] == 'Удали' or user_name[0] == 'удали':
#         cell_list = worksheet.findall(str(m.from_user.id))
#         if cell_list is None:
#             await bot.send_message(chat_id=m.from_user.id,
#                                    text=f'Уважаемый пользователь, вы ранее не записовались на прием к психологу,'
#                                         f'поэтому невозможно удалить вашу запись')
#         else:
#             for i in cell_list:
#                 row_number = i.row
#                 column_number = i.col
#                 worksheet.update_cell(row_number, column_number + 8, f'Отмена записи произошла в {datetime.now()}')
#             await bot.send_message(chat_id=m.from_user.id,
#                                    text=f'Ваша запись успешно удалена.\n'
#                                         f'Психолог оповещен о данном происшествии')
#             await bot.send_message(chat_id=739380400,
#                                    text=f'Уважаемая Полина, данный человек <b>отказался</b> от встречи с вами.\n'
#                                         f'Вот его данные:')
#             await bot.send_message(chat_id=739380400,
#                                    text=f'ФИО: {list_for_google_sheet[1]}\n'
#                                         f'Номер группы: {list_for_google_sheet[2]}\n'
#                                         f'Электронная почта: {list_for_google_sheet[4]}\n'
#                                         f'Проблема: {list_for_google_sheet[5]}\n'
#                                         f'Дата и время приема: {list_for_google_sheet[6]}')


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
        current_daatetime = str(date.today())
        i = 0
        while i < len(sched_w_st):
            if current_daatetime == sched_w_st[i]['date'] and teachers_name == sched_w_st[i]['teachers']:
                await bot.send_message(chat_id=m.from_user.id,
                                       text=f"<b>{sched_w_st[i]['place']}</b>\n<b>{sched_w_st[i]['time']}</b>",
                                       parse_mode="HTML")
            i += 1

    elif len(user_name) == 4 and user_name[0] == 'Где':
        teachers_name = str(user_name[1] + ' ' + user_name[2] + ' ' + user_name[3])
        await bot.send_message(chat_id=m.from_user.id,
                               text=f'{m.from_user.first_name}, вот, где сегодня будет находиться '
                                    f'<b>{teachers_name}</b>',
                               parse_mode='HTML')
        current_daatetime = str(date.today())
        i = 0
        while i < len(sched_w_st):
            if current_daatetime == sched_w_st[i]['date'] and teachers_name == sched_w_st[i]['teachers']:
                await bot.send_message(chat_id=m.from_user.id,
                                       text=f"<b>{sched_w_st[i]['place']}</b>\n<b>{sched_w_st[i]['time']}</b>",
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
                                    f"<b>Эту информацию увидит только психолог </b>.\n\n"
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
        worksheet.append_row(list_for_google_sheet)
        await bot.send_message(chat_id=m.from_user.id,
                               text=f'Вы успешно зарегистрировались на прием!\n'
                                    f'Вот ваши данные:')
        await bot.send_message(chat_id=m.from_user.id,
                               text=f'ФИО: {list_for_google_sheet[1]}\n'
                                    f'Номер группы: {list_for_google_sheet[2]}\n'
                                    f'Электронная почта: {list_for_google_sheet[4]}\n'
                                    f'Проблема: {list_for_google_sheet[5]}\n'
                                    f'Дата и время приема: {list_for_google_sheet[6]}',
                               reply_markup=kb_main)

        if list_for_google_sheet[7] == 'Полина Чибисова':
            await bot.send_message(chat_id=739380400,
                                   text=f'Уважаемая Полина, к вам записался новый человек.\n'
                                        f'Вот его данные:')
            await bot.send_message(chat_id=739380400,
                                   text=f'ФИО: {list_for_google_sheet[1]}\n'
                                        f'Номер группы: {list_for_google_sheet[2]}\n'
                                        f'Электронная почта: {list_for_google_sheet[4]}\n'
                                        f'Проблема: {list_for_google_sheet[5]}\n'
                                        f'Дата и время приема: {list_for_google_sheet[6]}')

        if list_for_google_sheet[6] == 'Среда 11 октября 2023, 14:00' or list_for_google_sheet[
            6] == 'Среда 11 октября 2023, 15:00' or list_for_google_sheet[6] == 'Среда 11 октября 2023, 16:00':
            scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
            scheduler.add_job(delay_reminder, trigger='cron', day_of_week='0, 1, 4', hour='18', minute='30',
                              end_date='2023-10-11', kwargs={'chat_id': m.from_user.id})
            scheduler.start()

        if list_for_google_sheet[6] == 'Среда 18 октября 2023, 14:00' or list_for_google_sheet[
            6] == 'Среда 18 октября 2023, 15:00' or list_for_google_sheet[6] == 'Среда 18 октября 2023, 16:00':
            scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
            scheduler.add_job(delay_reminder, trigger='cron', day_of_week='0, 1, 4', hour='18', minute='30',
                              end_date='2023-10-18', kwargs={'chat_id': m.from_user.id})
            scheduler.start()

        if list_for_google_sheet[6] == 'Среда 25 октября 2023, 14:00' or list_for_google_sheet[
            6] == 'Среда 25 октября 2023, 15:00' or list_for_google_sheet[6] == 'Среда 25 октября 2023, 16:00':
            scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
            scheduler.add_job(delay_reminder, trigger='cron', day_of_week='0, 1, 4', hour='18', minute='30',
                              end_date='2023-10-25', kwargs={'chat_id': m.from_user.id})
            scheduler.start()

    elif user_name[0] == 'Удали' or user_name[0] == 'удали':
        cell_list = worksheet.findall(str(m.from_user.id))
        if cell_list is None:
            await bot.send_message(chat_id=m.from_user.id,
                                   text=f'Уважаемый пользователь, вы ранее не записовались на прием к психологу,'
                                        f'поэтому невозможно удалить вашу запись',
                                   reply_markup=kb_main)
        else:
            for i in cell_list:
                row_number = i.row
                column_number = i.col
                worksheet.update_cell(row_number, column_number + 8, f'Отмена записи произошла в {datetime.now()}')
            await bot.send_message(chat_id=m.from_user.id,
                                   text=f'Ваша запись успешно удалена.\n'
                                        f'Психолог оповещен о данном происшествии',
                                   reply_markup=kb_main)
            await bot.send_message(chat_id=739380400,
                                   text=f'Уважаемая Полина, данный человек <b>отказался</b> от встречи с вами.\n'
                                        f'Вот его данные:')
            await bot.send_message(chat_id=739380400,
                                   text=f'ФИО: {list_for_google_sheet[1]}\n'
                                        f'Номер группы: {list_for_google_sheet[2]}\n'
                                        f'Электронная почта: {list_for_google_sheet[4]}\n'
                                        f'Проблема: {list_for_google_sheet[5]}\n'
                                        f'Дата и время приема: {list_for_google_sheet[6]}')



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
                                              f" <b>'Эта'</b>.\n\n"
                                              f"Если вы хотите узнать расписание на следующую неделю, то достаточно "
                                              f"нажать на кнопку:\n<b>'Следующая'</b>.\n\n",
                                         parse_mode="HTML",
                                         reply_markup=pic_keyboard)

    elif callback.data == 'where_is_he':
        await callback.message.edit_text(text=f'{telegram_user_name}, чтобы узнать, где находится интересующий вас '
                                              f'преподаватель, достаточно указать его имя как в паспорте с '
                                              f" припиской «где»'.\n\n"
                                              f'Например, <b>«Где Иванов Владимир Владимирович»</b>',
                                         parse_mode='HTML')
    elif callback.data == 'prepod_email':
        await callback.message.edit_text(text=f'{telegram_user_name}, чтобы узнать почту интересующего вас '
                                              f'преподавателя, достаточно указать его имя как в паспорте с'
                                              f'припиской «почта».\n\n'
                                              f'Например, <b>«Почта Иванов Владимир Владимирович»</b>',
                                         parse_mode='HTML')

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


if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)



