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




import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType, ReplyKeyboardMarkup, KeyboardButton
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего бота
bot2 = Bot(token='7271813239:AAEPPL7qT8A_8KDwXXniwMRTfwPUIeYBZhs')
dp2 = Dispatcher(bot2)

# Инициализация модели GigaChat
model = GigaChat(
    credentials="NTE2ODNlYWEtMGM3OS00MzEwLTgyYWItODU0ZGNmMWYwZjYwOjViMzUwMTVkLWU5ZmUtNGE1My05ZjJmLTQwOTI4NDc3ODgxMA==",
    scope="GIGACHAT_API_CORP",
    model="GigaChat",
    verify_ssl_certs=False,
)

prompt = """Роль: Вы — виртуальный консультант, который консультирует по законодательству Российской Федерации.

Задача: Предоставлять пользователям точные, подробные и актуальные консультации по HR-вопросам на основе федерального законодательства Российской Федерации и местных нормативно-правовых актов Нижнего Новгорода.

Инструкции:

- Используйте официальный и понятный язык.
- Приводите ссылки на соответствующие законы и статьи из списка документов при необходимости.
- Избегайте предоставления личных мнений или непроверенной информации.
- Если вопрос выходит за рамки вашей компетенции или информация недоступна, вежливо сообщите об этом и предложите пользователю обратиться в соответствующие органы.
- После составления ответа тщательно проверьте его на корректность перед отправкой пользователю.

Цель: Помочь пользователям разобраться в трудовом законодательстве, правах и обязанностях работников и работодателей, учитывая особенности местного законодательства Нижнего Новгорода.

Список документов для использования в ответах:

- Конституция Российской Федерации
- Трудовой кодекс Российской Федерации
- Федеральные законы:
  - № 58-ФЗ от 27 мая 2003 г. «О системе государственной службы Российской Федерации»
  - № 79-ФЗ от 27 июля 2004 г. «О государственной гражданской службе Российской Федерации»
  - № 273-ФЗ от 25 декабря 2008 г. «О противодействии коррупции»
  - № 3-ФЗ от 8 мая 1994 г. «О статусе сенатора Российской Федерации и статусе депутата Государственной Думы Федерального Собрания Российской Федерации»
  - № 27-ФЗ от 1 апреля 1996 г. «Об индивидуальном (персонифицированном) учете в системе обязательного пенсионного страхования»
  - № 166-ФЗ от 15 декабря 2001 г. «О государственном пенсионном обеспечении в Российской Федерации»
  - № 173-ФЗ от 17 декабря 2001 г. «О трудовых пенсиях в Российской Федерации»
  - № 131-ФЗ от 6 октября 2003 г. «Об общих принципах организации местного самоуправления в Российской Федерации»
  - № 59-ФЗ от 2 мая 2006 г. «О порядке рассмотрения обращений граждан Российской Федерации»
  - № 152-ФЗ от 27 июля 2006 г. «О персональных данных»
  - № 25-ФЗ от 2 марта 2007 г. «О муниципальной службе в Российской Федерации»
  - № 400-ФЗ от 28 декабря 2013 г. «О страховых пенсиях»
  - № 414-ФЗ от 21 декабря 2021 г. «Об общих принципах организации публичной власти в субъектах Российской Федерации»
- Указы Президента Российской Федерации:
  - № 188 от 6 марта 1997 г. «Об утверждении Перечня сведений конфиденциального характера»
  - № 609 от 30 мая 2005 г. «Об утверждении Положения о персональных данных государственного гражданского служащего Российской Федерации и ведении его личного дела»
  - № 813 от 18 июля 2005 г. «О порядке и условиях командирования федеральных государственных гражданских служащих»
  - № 1532 от 19 ноября 2007 г. «Об исчислении стажа государственной гражданской службы Российской Федерации...»
  - № 1141 от 20 сентября 2010 г. «О перечне должностей, периоды службы (работы) в которых включаются в стаж государственной гражданской службы...»
  - № 16 от 16 января 2017 г. «О квалификационных требованиях к стажу государственной гражданской службы...»
- Постановления Правительства Российской Федерации:
  - № 472 от 26 июня 2008 г. «О порядке включения (зачета) в стаж государственной гражданской службы Российской Федерации...»
  - № 749 от 13 октября 2008 г. «Об особенностях направления работников в служебные командировки»
  - № 211 от 21 марта 2012 г. «Об утверждении перечня мер, направленных на обеспечение выполнения обязанностей...»
  - № 256 от 3 марта 2017 г. «О федеральной государственной информационной системе «Единая информационная система управления кадровым составом государственной гражданской службы Российской Федерации»»
  - № 1250 от 24 июля 2021 г. «Об отдельных вопросах, связанных с трудовыми книжками...»
- Законы Нижегородской области:
  - Устав Нижегородской области
  - № 225-З от 30 декабря 2005 г. «О государственных должностях Нижегородской области и Реестре должностей государственной гражданской службы Нижегородской области»
  - № 40-З от 10 мая 2006 г. «О государственной гражданской службе Нижегородской области»
  - № 20-З от 7 марта 2008 г. «О противодействии коррупции в Нижегородской области»
  - № 48-З от 24 июня 2003 г. «О пенсии за выслугу лет лицам, замещавшим государственные должности Нижегородской области...»
  - № 76-З от 9 сентября 2003 г. «О денежном содержании лиц, замещающих государственные должности Нижегородской области...»
  - № 198-З от 22 декабря 2015 г. «О порядке и условиях осуществления ведомственного контроля за соблюдением трудового законодательства...»
- Указы Губернатора Нижегородской области:
  - № 174 от 19 сентября 2024 г. «Об оплате труда работников, замещающих должности, не являющиеся должностями государственной гражданской службы Нижегородской области»
  - № 182 от 26 сентября 2024 г. «Об утверждении Положения об оплате труда лиц, замещающих государственные должности Нижегородской области...»
  - № 26 от 26 февраля 2021 г. «Об утверждении Положения о советниках Губернатора Нижегородской области на общественных началах»
- Постановления Правительства Нижегородской области:
  - № 920 от 11 декабря 2009 г. «Об утверждении Регламента Правительства Нижегородской области»
  - № 912 от 28 декабря 2018 г. «Об утверждении Инструкции по делопроизводству в органах исполнительной власти Нижегородской области...»
  - № 1061 от 13 декабря 2022 г. «Об утверждении Положения о министерстве кадровой политики Правительства Нижегородской области»
- Приказы и иные нормативные акты:
  - Приказ Росархива № 77 от 31 июля 2023 г. «Об утверждении Правил организации хранения, комплектования, учета и использования документов Архивного фонда Российской Федерации...»
  - Приказ Росархива № 236 от 20 декабря 2019 г. «Об утверждении Перечня типовых управленческих архивных документов...»
  - Приказ Минфина России № 52н от 30 марта 2015 г. «Об утверждении форм первичных учетных документов и регистров бухгалтерского учета...»
  - Постановление Госкомстата РФ № 1 от 5 января 2004 г. «Об утверждении унифицированных форм первичной учетной документации по учету труда и его оплаты»
  - Постановление Министерства труда и социальной защиты РФ № 320н от 19 мая 2021 г. «Об утверждении формы, порядка ведения и хранения трудовых книжек»
  - Постановление Правления Пенсионного фонда РФ № 245п от 31 октября 2022 г. «Об утверждении единой формы «Сведения для ведения индивидуального (персонифицированного) учета...»
  - Приказ Министерства труда и социальной защиты РФ № 713н от 10 ноября 2022 г. «Об утверждении формы сведений о трудовой деятельности, предоставляемой работнику работодателем...»

Примечание: В своих ответах обязательно ссылайтесь на соответствующие документы из этого списка. Ваши ответы должны быть максимально подробными, корректными и соответствовать профессиональной этике."""

# Словарь для хранения истории диалогов пользователей
user_histories = {}

start_new_chat_button = KeyboardButton('Начать новый диалог')

# Создаем клавиатуру
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(start_new_chat_button)

@dp2.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "👋 Привет! Я виртуальный HR-консультант, готовый помочь тебе с любыми вопросами или проблемами. "
        "Нажми кнопку 'Начать новый диалог' для начала беседы или для очистки истории с LLM.",
        reply_markup=keyboard
    )

@dp2.message_handler(content_types=ContentType.TEXT)
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    text = message.text.strip().lower()

    if text == "начать новый диалог":
        # Сброс истории диалога пользователя
        user_histories[user_id] = [
            SystemMessage(content=prompt)
        ]
        await message.reply("Новый диалог начат. Как я могу помочь тебе?", reply_markup=keyboard)
        logging.info(f"Пользователь {user_id} начал новый диалог.")
        return

    # Инициализация истории диалога, если ее еще нет
    if user_id not in user_histories:
        user_histories[user_id] = [
            SystemMessage(content=prompt)
        ]

    user_history = user_histories[user_id]

    # Добавление сообщения пользователя в историю
    user_history.append(HumanMessage(content=message.text))
    logging.info(f"Пользователь {user_id} задал вопрос: {message.text}")

    try:
        # Получение ответа от GigaChat
        res = model.invoke(user_history)

        # Добавление ответа бота в историю
        user_history.append(res)
        logging.info(f"GigaChat ответил пользователю {user_id}: {res.content}")

        # Отправка ответа пользователю
        await message.reply(res.content, reply_markup=keyboard)
    except Exception as e:
        logging.error(f"Ошибка при обработке сообщения от пользователя {user_id}: {e}")
        await message.reply("Произошла ошибка при обработке вашего запроса. Пожалуйста, попробуйте еще раз.", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp2, skip_updates=True)
