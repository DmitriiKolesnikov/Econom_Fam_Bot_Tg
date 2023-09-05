from aiogram import Bot, executor, Dispatcher, types
from Main_kb import kb_main, pic_keyboard
from Kafedri_data import inline_kb_kafedri
from Take_user_name_inline_kb import take_user_name_kb
from Prepodi_inline_kb import prepodi_kb
from Free_room_kb import free_room_kb
from Meropriatia_kb import meropriatia_kb
from Json_data import sched_w_st, data_all_teachers_and_mails
from sercher_cacsa import get_schedule
from datetime import date
from kabs_data_and_logic import list_of_kabs_first_flour, list_of_kabs_second_flour, \
    list_of_kabs_third_flour, list_of_kabs_fourth_flour, list_of_kabs_fith_flour


TOKEN_API = '6431263054:AAG5luZr2VIGwYPIiBJ4QHxEAwSKH-iil70'


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


user_name = ''


async def on_startup(_):
    print('Bot started')


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
                                 'Не позволь им испортить твое пребывание в МГУ!!!',
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


@dp.message_handler(text='⌛Психологическая помощь')
async def psycho_help_command(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id,
                         caption='👩🏼 '+'‍К специалисту можно записаться и прийти на консультацию, чтобы поработать '
                                 'с внутренними переживаниями или поделиться накопившимися мыслями и эмоциями.'
                                 ' ⌛ '+'Продолжительность сеанса — около 50 минут '
                                 'Если вам нужна помощь в разрешении какой-либо возникшей проблемы и вы бы хотели '
                                 'получить психологическую поддержку, заполните, пожалуйста, гугл-форму'+' 👉🏻 '
                                 + 'https://forms.gle/8HzRmW1yX8Wq5MVx7',
                         photo='https://babr24.com/n2p/i/2021/1/21_1_5_2_05132453_b.jpg')
    await message.delete()


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


@dp.message_handler(text='📆Расписание')
async def time_table_command(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id,
                         caption='Чтобы получить свое заветное расписание, вам надо написать свое имя <b>прям '
                                 'как в паспорте</b> 🧐'+'.\n\n'
                                 'Например, <b>Пупкин Василий Сергеевич</b>.',
                         photo='https://cs14.pikabu.ru/post_img/big/2022/03/08/7/1646737740129559994.jpg',
                         parse_mode='HTML')
    await message.delete()


@dp.message_handler()
async def take_user_name(message: types.Message) -> user_name:
    global user_name
    global full_name
    user_name = message.text.split()
    if len(user_name) == 3 and message.text.istitle():
        full_name = message.text
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Я правильно понимаю, что вас зовут {message.text}',
                               reply_markup=take_user_name_kb)

    elif len(user_name) == 4 and user_name[0] == 'где':
        teachers_name = str(user_name[1] + ' ' + user_name[2] + ' ' + user_name[3])
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'{message.from_user.first_name}, вот, где сегодня будет находиться '
                                    f'<b>{teachers_name}</b>',
                               parse_mode='HTML')
        current_daatetime = str(date.today())
        i = 0
        while i < len(sched_w_st):
            if current_daatetime == sched_w_st[i]['date'] and teachers_name == sched_w_st[i]['teachers']:
                await bot.send_message(chat_id=message.from_user.id,
                                       text=f"<b>{sched_w_st[i]['place']}</b>\n<b>{sched_w_st[i]['time']}</b>",
                                       parse_mode="HTML")
            i += 1

    elif len(user_name) == 4 and user_name[0] == 'Где':
        teachers_name = str(user_name[1] + ' ' + user_name[2] + ' ' + user_name[3])
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'{message.from_user.first_name}, вот, где сегодня будет находиться '
                                    f'<b>{teachers_name}</b>',
                               parse_mode='HTML')
        current_daatetime = str(date.today())
        i = 0
        while i < len(sched_w_st):
            if current_daatetime == sched_w_st[i]['date'] and teachers_name == sched_w_st[i]['teachers']:
                await bot.send_message(chat_id=message.from_user.id,
                                       text=f"<b>{sched_w_st[i]['place']}</b>\n<b>{sched_w_st[i]['time']}</b>",
                                       parse_mode="HTML")
            i += 1

    elif len(user_name) == 4 and user_name[0] == 'почта':
        teachers_name = str(user_name[1] + ' ' + user_name[2] + ' ' + user_name[3])
        i = 0
        while i < len(data_all_teachers_and_mails):
            if teachers_name in data_all_teachers_and_mails[i].values():
                await bot.send_message(chat_id=message.from_user.id,
                                       text=f"{message.from_user.first_name}, вот почта"
                                            f": "
                                            f"<b>{data_all_teachers_and_mails[i]['mail']}</b>",
                                       parse_mode="HTML")
            i += 1

    elif len(user_name) == 4 and user_name[0] == 'Почта':
        teachers_name = str(user_name[1] + ' ' + user_name[2] + ' ' + user_name[3])
        i = 0
        while i < len(data_all_teachers_and_mails):
            if teachers_name in data_all_teachers_and_mails[i].values():
                await bot.send_message(chat_id=message.from_user.id,
                                       text=f"{message.from_user.first_name}, вот почта"
                                            f": "
                                            f"<b>{data_all_teachers_and_mails[i]['mail']}</b>",
                                       parse_mode="HTML")
            i += 1

    elif user_name[0] == "Эта":
        photo = open('1.png', 'rb')
        await get_schedule(full_name)
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Вот ваше расписание на эту неделю, {full_name}')
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo)

    elif user_name[0] == "Следующая":
        photo = open('2.png', 'rb')
        await get_schedule(full_name)
        await bot.send_message(chat_id=message.from_user.id,
                               text=f'Вот ваше расписание на следующую неделю, {full_name}')
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo)

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

        await callback.message.edit_text(text=f'{telegram_user_name}, вот список кабинетов, доступных на '
                                              f'<b>первой паре</b>:\n'
                                              f'СВОБОДНЫЕ КАБИНЕТЫ БУДУТ ДОСТУПНЫ В ВОСКРЕСЕНЬЕ В 20:00.',
                                         parse_mode='HTML')
    elif callback.data == 'second_pair':
        current_time = '10:40-12:10'
        current_date = str(date.today())
        for i in range(len(sched_w_st)):
            if sched_w_st[i]['date'] == current_date and sched_w_st[i]['time'] == current_time:
                if sched_w_st[i]['place'].startswith('1') and int(sched_w_st[i]['place']) in \
                            list_of_kabs_first_flour:
                    list_of_kabs_first_flour.remove(int(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('2') and int(sched_w_st[i]['place']) in \
                            list_of_kabs_second_flour:
                    list_of_kabs_second_flour.remove(int(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('3') and int(sched_w_st[i]['place']) in \
                            list_of_kabs_third_flour:
                    list_of_kabs_third_flour.remove(int(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('4') and int(sched_w_st[i]['place']) in \
                            list_of_kabs_fourth_flour:
                    list_of_kabs_fourth_flour.remove(int(sched_w_st[i]['place']))
                elif sched_w_st[i]['place'].startswith('5') and int(sched_w_st[i]['place']) in \
                            list_of_kabs_fith_flour:
                    list_of_kabs_fith_flour.remove(int(sched_w_st[i]['place']))

        await callback.message.edit_text(text=f"{telegram_user_name}, вот список кабинетов, доступных на <b>второй "
                                              f"паре</b>:"
                                              f"<b>Первый этаж</b>: {', '.join(list_of_kabs_first_flour)}\n",
                                         parse_mode='HTML')
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"<b>Второй этаж</b>: {', '.join(str(list_of_kabs_second_flour))}\n",
                               parse_mode="HTML")
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"<b>Третий этаж</b>: {', '.join(str(list_of_kabs_third_flour))}\n",
                               parse_mode="HTML")
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"<b>Четвертый этаж</b>: {', '.join(str(list_of_kabs_fourth_flour))}\n")
        await bot.send_message(chat_id=callback.from_user.id,
                               text=f"<b>Пятый этаж</b>: {', '.join(str(list_of_kabs_fith_flour))}\n",
                               parse_mode="HTML")

    elif callback.data == 'third_pair':
        time = '12:20-13:50'
        await callback.message.edit_text(text=f'{telegram_user_name}, вот список кабинетов, доступных на '
                                              f'<b>третьей паре</b>:\n'
                                              f'СВОБОДНЫЕ КАБИНЕТЫ БУДУТ ДОСТУПНЫ В ВОСКРЕСЕНЬЕ В 20:00.',
                                         parse_mode='HTML')
    elif callback.data == 'forth_pair':
        time = '14:00-15:30'
        await callback.message.edit_text(text=f'{telegram_user_name}, вот список кабинетов, доступных на '
                                              f'<b>четвертой паре</b>:\n'
                                              f'СВОБОДНЫЕ КАБИНЕТЫ БУДУТ ДОСТУПНЫ В ВОСКРЕСЕНЬЕ В 20:00.',
                                         parse_mode='HTML')
    elif callback.data == 'fifth_pair':
        time = '15:40-17:10'
        await callback.message.edit_text(text=f'{telegram_user_name}, вот список кабинетов, доступных на '
                                              f'<b>пятой паре</b>:\n'
                                              f'СВОБОДНЫЕ КАБИНЕТЫ БУДУТ ДОСТУПНЫ В ВОСКРЕСЕНЬЕ В 20:00.',
                                         parse_mode='HTML')
    elif callback.data == 'six_pair':
        time = '17:20-18:50'
        await callback.message.edit_text(text=f'{telegram_user_name}, вот список кабинетов, доступных на '
                                              f'<b>шестой паре</b>:\n'
                                              f'СВОБОДНЫЕ КАБИНЕТЫ БУДУТ ДОСТУПНЫ В ВОСКРЕСЕНЬЕ В 20:00.',
                                         parse_mode='HTML')
    elif callback.data == 'seventh_pair':
        time = '18:55-20:25'
        await callback.message.edit_text(text=f'{telegram_user_name}, вот список кабинетов, доступных на '
                                              f'<b>седьмой паре</b>:\n'
                                              f'СВОБОДНЫЕ КАБИНЕТЫ БУДУТ ДОСТУПНЫ В ВОСКРЕСЕНЬЕ В 20:00.',
                                         parse_mode='HTML')
    elif callback.data == 'eight_pair':
        time = '20:30-22:00'
        await callback.message.edit_text(text=f'{telegram_user_name}, вот список кабинетов, доступных на '
                                              f'<b>восьмой паре</b>:\n'
                                              f'СВОБОДНЫЕ КАБИНЕТЫ БУДУТ ДОСТУПНЫ В ВОСКРЕСЕНЬЕ В 20:00.',
                                         parse_mode='HTML')

    elif callback.data == 'official':
        await callback.message.answer(text=f'{telegram_user_name}, вот список мероприятий от <b>МГУ</b>: ',
                                      parse_mode='HTML')
        await callback.message.answer(text=f'ДЕНЬ ПЕРВОКУРСНИКА(1.09.2023):\n\n'
                                           f'15:40-17:10 – ЯРМАРКА СТУДЕНЧЕСКИХ ОРГАНИЗАЦИЙ, 2 этаж, овальный корпус\n'
                                           f'17:20-18:50 – ВСТРЕЧА ГРУПП С КУРАТОРАМИ\n'
                                           f'19:00 – МУЗЫКАЛЬНЫЙ ЧАС ,аудитория П5.\n\n'
                                           f'МУЗЫКАЛЬНЫЙ ЧАС(6.10.2023, 8.11.2023, 10.12.2023)\n'
                                           f'19:00, аудитория П5.\n\n'
                                           f'29 сентября - турнир по шахматам\n\n'
                                           f'20 октября - турнир по настольному теннису\n\n'
                                           f'26 ноября - второй кубок ЭФ по волейболу\n\n'
                                           f'10 декабря - турнир по баскетболу\n\n'
                                      )
        await callback.message.answer(text=f'ЭКОНОМ ГОВОРИТ\n\n'
                                           f'Дорогие друзья!\n\n 👋🏻'
                                           f'Новый учебный год уже на пороге, и мы надеемся, что вы провели лето '
                                           f'насыщенно и готовы встретить его с новыми силами и энергией.\n '
                                           f'«Эконом говорит», в свою очередь, очень ждёт встречи с теми, кто с ним уже '
                                           f'знаком, и, конечно же, с первокурсниками. 🤗\n'
                                           f'Уже 1 сентября в 15:40 мы приглашаем Вас на 2 этаж ЭФ '
                                           f'(точное место встречи в '
                                           f'комментариях), чтобы вместе начать новый учебный год.\n '
                                           f'Что же вас ждет?\n\n'
                                           f'⁃ наши организаторы, которые скучают и с нетерпением ждут встречи с '
                                           f'каждым из вас\n'
                                           f'⁃ интересные конкурсы и призы\n'
                                           f'⁃ артикуляционная гимнастика — упражнения на улучшение произношения '
                                           f'и звучания речи\n\n'
                                           f'До встречи на втором этаже ЭФ 🤝\n\n'
                                           f'Будь всегда с нами!!! -> https://vk.com/econ_talks')

    elif callback.data == 'unofficial':
        await callback.message.answer(text=f'{telegram_user_name}, вот список мероприятий, которые предлагают наши '
                                           f'<b>студенты</b>:',
                                      parse_mode='HTML')
        await callback.message.answer(text=f'NONDUM\n\n)'
                                           f'🎓 POSVYAT PARTY🎓\n'
                                           f'🤝🏼 Nondum & Сelonosov 🤝🏼\n'
                                           f'🔔 9.09.2023 - 10.09.23 🔔\n'
                                           f'🌘 23:00 - 05:00 🌒\n'
                                           f'🚇 Метро Бауманская 🚇\n'
                                           f'❓ Что вас ждёт? \n\n❓'
                                           f'🔥Море позитивных эмоций 🔥\n'
                                           f'💫 Отличная атмосфера 💫\n'
                                           f'👨🏽‍🎓 Новые знакомства 👩🏽‍🎓\n'
                                           f'🥃 Бесплатный безлимитный бар 🥃\n'
                                           f'🍹 Платный бар с новыми интересными коктейлями 🍹\n'
                                           f'🍕 Много еды 🍕\n'
                                           f'🎶 Профессиональный DJ 🎶\n'
                                           f'🔊 Невероятный sound 🔊\n'
                                           f'📸 Фотограф 📸\n'
                                           f'🤵🏽‍Замечательные бармены 🤵🏽‍\n'
                                           f'👮🏼‍♂ Профессиональная охрана 👮🏼‍♂\n'
                                           f'🍾 Незабываемые впечатления от студенческой тусовки 🍾\n\n'
                                           f'❗ Условия ❗\n\n'
                                           f'👕 No Dress Code 👔\n'
                                           f'🎟 Вход по билетам, количество мест ограничено, продажи '
                                           f'разделены на этапы 🎟\n'
                                           f'🎫 С 12.08.2023 до 03.09.2023 - 2 500₽\n\n'
                                           f'🎫 С 04.09.2022 по 09.09.2022 - 3 000₽\n\n'
                                           f'🍪 Скидки суммируются 🍪\n'
                                           f'✅ При наличии промокода Вы получаете скидку 10%\n'
                                           f'✅ Для всех первокурсников скидка 5%, при подтверждении статуса\n'
                                           f'✅ Подписка на нас, комментарий и лайк на пост дают скидку 5%\n'
                                           f'💳💬 За подробностями и по вопросам оплаты обращайтесь в личные сообщения '
                                           f'сообщества https://vk.com/nondum.party')

        await callback.message.answer(text=f'ЦЕЛОНОСОВ\n\n'
                                           f'⚡⚡⚡Как стать студентом: краткое пособие для первокура!\n\n'
                                           f'✅ Познакомиться со своими одногруппниками\n'
                                           f'✅ Пойти вместе с ними на самый крутой посвят от Celonocov x Nondum\n'
                                           f'✅ Попробовать вкуснейшие коктейли с оттенком студенчества\n'
                                           f'✅ Отжечь по полной под классные треки\n'
                                           f'✅ Получить фотки от профессиональных фотографов\n\n'
                                           f'🎡 Что вас ждёт крутого и необычного?\n'
                                           f'🥂 Система двух баров (бесплатный и платный) и крутые коктейль-мэйкеры\n'
                                           f'🎼 профессиональные диджеи и качественная звуковая аппаратураn\n'
                                           f'👮🏽 охрана и гарантированная безопасность мероприятия\n'
                                           f'🍕 еда, включённая в стоимость билета\n'
                                           f'🗓 Когда?\n\n'
                                           f'9-го сентября 2023\n\n'
                                           f'⏱ Со скольки и до скольки\n\n?'
                                           f'23.00-5.00\n\n'
                                           f'📍Локация\n\n'
                                           f'м. Бауманская\n\n'
                                           f'💴 How much?\n\n'
                                           f'🌊1 волна (12 авг - 3 сен 23:59) - 2500₽ (с учетом всех скидок 2000₽)\n'
                                           f'🌊2 волна (4 сен - 8 сен 23:59) - 3000₽ (с учетом всех скидок 2400₽)\n\n'
                                           f'🔗 Также у нас есть скидочная система:\n\n'
                                           f'✔5% за подписку на паблик + лайк и комментарий под посто\n'
                                           f'✔5% всем первокурсника\n'
                                           f'✔10% промокод от промоутера\n'
                                           f'❕Скидки суммируются❕\n'
                                           f'🧨 Продаём через наш паблик - пишите в лс сообщества!\n'
                                           f'❗Количество билетов ограничено\n\n'
                                           f'P.S. Если вы купили билет и не можете посетить мероприятие, то у вас есть ' \
                                           f'возможность вернуть 50% от стоимости билета или перепродать его другому ' \
                                           f'человеку (об этом вы должны будете сообщить нам в лс)\n'
                                           f'Паблик =》https://vk.com/celonocov')

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



