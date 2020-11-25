# подлключение библиотек
# -*- coding: utf8 -*-
import telebot
from telebot import types
bot = telebot.TeleBot("1338510205:AAHDYcKWg64hvFOpadA8cvvHn6bUwAb3ReQ")
# клавиатура бота
@bot.message_handler(commands=["start"])
def cmd_start(message):
    start_key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text = 'Робоквантум', callback_data='Робоквантум')
    but_2 = types.InlineKeyboardButton(text='Промдизайн', callback_data='Промдизайн')
    but_3 = types.InlineKeyboardButton(text='IT-квантум', callback_data='IT-квантум')
    but_4 = types.InlineKeyboardButton(text='Хайтек', callback_data='Хайтек')
    but_5 = types.InlineKeyboardButton(text='Аэроквантум', callback_data='Аэроквантум')
    but_6 = types.InlineKeyboardButton(text='Наноквантум', callback_data='Наноквантум')
    but_7 = types.InlineKeyboardButton(text='Связь', callback_data='Связь')
    but_8 = types.InlineKeyboardButton(text='Руководство', callback_data='Руководство')
    but_10 = types.InlineKeyboardButton(text='Расписание', callback_data='Расписание')
    but_9 = types.InlineKeyboardButton(text='Запись на занятия', callback_data="Запись на занятия")
    start_key.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_10, but_9)
    # встречающее сообщение после команды /start
    bot.send_message(message.chat.id, "Добро пожаловать. Обучение в детских технопарках «Кванториум» происходит в квантумах,"
                                           " каждый из которых соответствует ключевому направлению инновационного развития Российской Федерации."
                                           " Всего квантумов 6: Промдизайн, Робоквантум, Наноквантум, Аэроквантум, IT-квантум, и Хайтек."
                                           " Кванторианцы с помощью наставников разрабатывают реальные проекты на высокотехнологичном и современном оборудовании,"
                                           " учатся работать в команде и применять полученные знания на практике. "
                                           " Наш сайт: [Кванториум62.рф](https://xn--62-6kch5ajrgjuup.xn--p1ai/)", parse_mode='Markdown', reply_markup=start_key)
    start = telebot.types.ReplyKeyboardMarkup(True)
    start.row('Фото')
    bot.send_message(message.from_user.id, 'Выбери квантум или сервис.', reply_markup=start)
# заполнение клавиатуры
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Фото':
        bot.send_photo(message.from_user.id, 'https://cdn.discordapp.com/attachments/778504942758395924/778512998313492510/IMG_20201118_093052.jpg')
        bot.send_photo(message.from_user.id, 'https://cdn.discordapp.com/attachments/778504942758395924/778510521170264075/IMG_20201118_093914.jpg')
        bot.send_photo(message.from_user.id, 'https://cdn.discordapp.com/attachments/778504942758395924/778510561830371338/IMG_20201118_093538.jpg')
        bot.send_photo(message.from_user.id, 'https://cdn.discordapp.com/attachments/778504942758395924/778510490959347742/IMG_20201118_094103.jpg')
        bot.send_photo(message.from_user.id, 'https://cdn.discordapp.com/attachments/778504942758395924/778510490351042560/IMG_20201118_094040.jpg')

@bot.callback_query_handler(func=lambda c:True)
def inline(c):
    if c.data == 'Связь':
        keyboard = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='Робоквантум', callback_data='Робоквантум')
        but_2 = types.InlineKeyboardButton(text='Промдизайн', callback_data='Промдизайн')
        but_3 = types.InlineKeyboardButton(text='IT-квантум', callback_data='IT-квантум')
        but_4 = types.InlineKeyboardButton(text='Хайтек', callback_data='Хайтек')
        but_5 = types.InlineKeyboardButton(text='Аэроквантум', callback_data='Аэроквантум')
        but_6 = types.InlineKeyboardButton(text='Наноквантум', callback_data='Наноквантум')
        but_7 = types.InlineKeyboardButton(text='Расписание', callback_data='Расписание')
        but_8 = types.InlineKeyboardButton(text='Запись на занятия', callback_data='Запись на занятия')
        but_9 = types.InlineKeyboardButton(text='Руководство', callback_data='Руководство')
        keyboard.add(but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9, but_1)
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Адрес: 390013, г. Рязань, ул. Дзержинского, 6.\n Телефоны: +7 (4912) 55-92-80.\n E-mail: mail@кванториум62.рф', parse_mode='Markdown', reply_markup=keyboard)
    if c.data == 'Руководство':
        keyboard = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='Робоквантум', callback_data='Робоквантум')
        but_2 = types.InlineKeyboardButton(text='Промдизайн', callback_data='Промдизайн')
        but_3 = types.InlineKeyboardButton(text='IT-квантум', callback_data='IT-квантум')
        but_4 = types.InlineKeyboardButton(text='Хайтек', callback_data='Хайтек')
        but_5 = types.InlineKeyboardButton(text='Аэроквантум', callback_data='Аэроквантум')
        but_6 = types.InlineKeyboardButton(text='Наноквантум', callback_data='Наноквантум')
        but_7 = types.InlineKeyboardButton(text='Расписание', callback_data='Расписание')
        but_8 = types.InlineKeyboardButton(text='Запись на занятия', callback_data='Запись на занятия')
        but_9 = types.InlineKeyboardButton(text='Связь', callback_data='Связь')
        keyboard.add(but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9, but_1)
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text="[Руководство Кванториума](https://xn--62-6kch5ajrgjuup.xn--p1ai/guide)", parse_mode='Markdown', reply_markup=keyboard)
    if c.data == 'Расписание':
        keyboard = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='Робоквантум', callback_data='Робоквантум')
        but_2 = types.InlineKeyboardButton(text='Промдизайн', callback_data='Промдизайн')
        but_3 = types.InlineKeyboardButton(text='IT-квантум', callback_data='IT-квантум')
        but_4 = types.InlineKeyboardButton(text='Хайтек', callback_data='Хайтек')
        but_5 = types.InlineKeyboardButton(text='Аэроквантум', callback_data='Аэроквантум')
        but_6 = types.InlineKeyboardButton(text='Наноквантум', callback_data='Наноквантум')
        but_7 = types.InlineKeyboardButton(text='Руководство', callback_data='Руководство')
        but_8 = types.InlineKeyboardButton(text='Запись на занятия', callback_data='Запись на занятия')
        but_9 = types.InlineKeyboardButton(text='Связь', callback_data='Связь')
        keyboard.add(but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9, but_1)
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text='Расписание работы:\n Понедельник-пятница - с 9:00 до 20:00.\n Суббота-воскресенье - в соответствии с расписанием.\n(Изменения расписания НЕ ОТОБРАЖАЮТСЯ)', reply_markup=keyboard)
    if c.data == 'Запись на занятия':
        keyboard = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='Робоквантум', callback_data='Робоквантум')
        but_2 = types.InlineKeyboardButton(text='Промдизайн', callback_data='Промдизайн')
        but_3 = types.InlineKeyboardButton(text='IT-квантум', callback_data='IT-квантум')
        but_4 = types.InlineKeyboardButton(text='Хайтек', callback_data='Хайтек')
        but_5 = types.InlineKeyboardButton(text='Аэроквантум', callback_data='Аэроквантум')
        but_6 = types.InlineKeyboardButton(text='Наноквантум', callback_data='Наноквантум')
        but_7 = types.InlineKeyboardButton(text='Расписание', callback_data='Расписание')
        but_8 = types.InlineKeyboardButton(text='Руководство', callback_data="Руководство")
        but_9 = types.InlineKeyboardButton(text='Связь', callback_data='Связь')
        keyboard.add(but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9, but_1)
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text="[Запись на занятия в Кванториум](https://xn--62-6kch5ajrgjuup.xn--p1ai/enrollment)", parse_mode='Markdown', reply_markup=keyboard)

    if c.data == 'Робоквантум':
        bot.send_photo(c.message.chat.id, "https://cdn.discordapp.com/attachments/778504942758395924/778512998313492510/IMG_20201118_093052.jpg")
        keyboard = types.InlineKeyboardMarkup()
        but_2 = types.InlineKeyboardButton(text='Промдизайн', callback_data='Промдизайн')
        but_3 = types.InlineKeyboardButton(text='IT-квантум', callback_data='IT-квантум')
        but_4 = types.InlineKeyboardButton(text='Хайтек', callback_data='Хайтек')
        but_5 = types.InlineKeyboardButton(text='Аэроквантум', callback_data='Аэроквантум')
        but_6 = types.InlineKeyboardButton(text='Наноквантум', callback_data='Наноквантум')
        but_7 = types.InlineKeyboardButton(text='Руководство', callback_data='Руководство')
        but_8 = types.InlineKeyboardButton(text='Запись на занятия', callback_data='Запись на занятия')
        but_9 = types.InlineKeyboardButton(text='Связь', callback_data='Связь')
        but_10 = types.InlineKeyboardButton(text='Расписание', callback_data='Расписание')
        keyboard.add(but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9, but_10)
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text="Мультипредметность промышленной робототехники погружает кванторианцев в такие научные и инженерные дисциплины как механика,"
                                          " электроника, электротехника, физика, информатика (машинное обучение, техническое зрение, операционные системы),"
                                          " математическое моделирование и др. Проектная деятельность, направленная на создание интеллектуальных систем для различных сфер"
                                          " человеческой деятельности, в частности производства, позволяет формировать системное мышление как в инженерном,"
                                          " так и в мировоззренческом смысле. Преподаватели: Костин Роман Сергеевич, Мордвинов Андрей Олегович, Петаева Виктория Александровна, Реутова Ольга Викторовна, Феклушкин Михаил Михайлович."
                                          " Подробнее на сайте: [Кванториум62.рф](https://xn--62-6kch5ajrgjuup.xn--p1ai/promrobokantum)", parse_mode='Markdown', reply_markup=keyboard)


    if c.data == 'Промдизайн':
        keyboard = types.InlineKeyboardMarkup()
        but_2 = types.InlineKeyboardButton(text='Робоквантум', callback_data='Робоквантум')
        but_3 = types.InlineKeyboardButton(text='IT-квантум', callback_data='IT-квантум')
        but_4 = types.InlineKeyboardButton(text='Хайтек', callback_data='Хайтек')
        but_5 = types.InlineKeyboardButton(text='Аэроквантум', callback_data='Аэроквантум')
        but_6 = types.InlineKeyboardButton(text='Наноквантум', callback_data='Наноквантум')
        but_7 = types.InlineKeyboardButton(text='Руководство', callback_data='Руководство')
        but_8 = types.InlineKeyboardButton(text='Запись на занятия', callback_data='Запись на занятия')
        but_9 = types.InlineKeyboardButton(text='Связь', callback_data='Связь')
        but_10 = types.InlineKeyboardButton(text='Расписание', callback_data='Расписание')
        #but_0 = types.InlineKeyboardButton(text='Фото', callback_data='Фото')
        keyboard.add(but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9, but_10)
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text="На занятиях промдизайнквантума ребята погрузятся в изобретательский процесс, целью которого"
                                          " является разработка нового, ранее не существовавшего, объекта. Пройдут все этапы создания объекта промышленного дизайна от генерации идеи"
                                          " до создания прототипа и разработки программы его внедрения, получат навыки 3D-моделирования и визуализации,"
                                          " изучат специфику профессии промышленного дизайнера. Преподаватели: Тюрин Владимир Валерьевич, Тюрин Владимир Валерьевич. Подробнее на сайте: [Кванториум62.рф](https://xn--62-6kch5ajrgjuup.xn--p1ai/industrialdesignquanta)", parse_mode='Markdown', reply_markup=keyboard)



    if c.data == 'IT-квантум':
        keyboard = types.InlineKeyboardMarkup()
        but_2 = types.InlineKeyboardButton(text='Промдизайн', callback_data='Промдизайн')
        but_3 = types.InlineKeyboardButton(text='Робоквантум', callback_data='Робоквантум')
        but_4 = types.InlineKeyboardButton(text='Хайтек', callback_data='Хайтек')
        but_5 = types.InlineKeyboardButton(text='Аэроквантум', callback_data='Аэроквантум')
        but_6 = types.InlineKeyboardButton(text='Наноквантум', callback_data='Наноквантум')
        but_7 = types.InlineKeyboardButton(text='Руководство', callback_data='Руководство')
        but_8 = types.InlineKeyboardButton(text='Запись на занятия', callback_data='Запись на занятия')
        but_9 = types.InlineKeyboardButton(text='Связь', callback_data='Связь')
        but_10 = types.InlineKeyboardButton(text='Расписание', callback_data='Расписание')
        keyboard.add(but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9, but_10)
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text="В IT-Квантуме учащиеся смогут освоить программирование на актуальных высокоуровневых языках, "
                                          "получить знания в областях защиты информации, криптографии, информационно-коммуникационных технологиях. Преподаватели: Федин Никита Алексеевич, "
                                          "Вилков Денис Эдуардович, Иванов Владимир Сергеевич,Ануров Иван Сергеевич."
                                          " Подробнее можно ознакомиться на сайте: [Кванториум62.рф](https://xn--62-6kch5ajrgjuup.xn--p1ai/itquantum)", parse_mode='Markdown', reply_markup=keyboard)
    if c.data == 'Хайтек':
        keyboard = types.InlineKeyboardMarkup()
        but_2 = types.InlineKeyboardButton(text='Промдизайн', callback_data='Промдизайн')
        but_3 = types.InlineKeyboardButton(text='IT-квантум', callback_data='IT-квантум')
        but_4 = types.InlineKeyboardButton(text='Робоквантум', callback_data='Робокванум')
        but_5 = types.InlineKeyboardButton(text='Аэроквантум', callback_data='Аэроквантум')
        but_6 = types.InlineKeyboardButton(text='Наноквантум', callback_data='Наноквантум')
        but_7 = types.InlineKeyboardButton(text='Руководство', callback_data='Руководство')
        but_8 = types.InlineKeyboardButton(text='Запись на занятия', callback_data='Запись на занятия')
        but_9 = types.InlineKeyboardButton(text='Связь', callback_data='Связь')
        but_10 = types.InlineKeyboardButton(text='Расписание', callback_data='Расписание')
        keyboard.add(but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9, but_10)
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text="Хайтек-цех – особая часть Кванториума. Здесь все задуманные идеи превращаются в реальные, осязаемые вещи."
                                          " Это мастерская, оснащенная высокотехнологичным оборудованием:"
                                          " 3D-принтерами, станками с ЧПУ, лазерным, паяльным и другим современным оборудованием."
                                          "В проектной зоне Хай-тек цеха располагаются компьютеры с современным программным обеспечением для проектирования изделий,"
                                          " 3D-моделирования, составления документации и создания управляющих программ для станков с ЧПУ и 3D-принтеров."
                                          "В Хайтек лаборатории находится паяльное оборудование, измерительные приборы, слесарный инструмент, оборудование для резки, сверления,"
                                          " шлифовки материалов – все то, что может понадобится для воплощения своей мечты в реальность.В отдельной зоне, экранизирующей пыль и шум,"
                                          " находятся фрезерно-гравировальные станки с ЧПУ и станок для лазерной резки листового материала."
                                          " Подробнее на сайте: [Кванториум62.рф](https://xn--62-6kch5ajrgjuup.xn--p1ai/hightech)", parse_mode='Markdown', reply_markup=keyboard)
    if c.data == 'Аэроквантум':
        keyboard = types.InlineKeyboardMarkup()
        but_2 = types.InlineKeyboardButton(text='Промдизайн', callback_data='Промдизайн')
        but_3 = types.InlineKeyboardButton(text='IT-квантум', callback_data='IT-квантум')
        but_4 = types.InlineKeyboardButton(text='Хайтек', callback_data='Хайтек')
        but_5 = types.InlineKeyboardButton(text='Робоквантум', callback_data='Робоквантум')
        but_6 = types.InlineKeyboardButton(text='Наноквантум', callback_data='Наноквантум')
        but_7 = types.InlineKeyboardButton(text='Руководство', callback_data='Руководство')
        but_8 = types.InlineKeyboardButton(text='Запись на занятия', callback_data='Запись на занятия')
        but_9 = types.InlineKeyboardButton(text='Связь', callback_data='Связь')
        but_10 = types.InlineKeyboardButton(text='Расписание', callback_data='Расписание')
        keyboard.add(but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9, but_10)
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text="В аэроквантуме ученики смогут сформировать устойчивые знания и навыки по таким направлениям,"
                                          " как аэродинамика и конструирование беспилотных летательных аппаратов, радиоэлектроника и схемотехника,"
                                          " программирование микроконтроллеров, лётная эксплуатация беспилотных авиационные систем (БАС), развить интерес к проектной,"
                                          " конструкторской и предпринимательской деятельности, значительно расширяющей кругозор и образованность. Преподаватели: Заборов Дмитрий Борисович."
                                          " Подробнее на сайте: [Кванториум62.рф](https://xn--62-6kch5ajrgjuup.xn--p1ai/aeroquantum)", parse_mode='Markdown', reply_markup=keyboard)
    if c.data == 'Наноквантум':
        keyboard = types.InlineKeyboardMarkup()
        but_2 = types.InlineKeyboardButton(text='Промдизайн', callback_data='Промдизайн')
        but_3 = types.InlineKeyboardButton(text='IT-квантум', callback_data='IT-квантум')
        but_4 = types.InlineKeyboardButton(text='Хайтек', callback_data='Хайтек')
        but_5 = types.InlineKeyboardButton(text='Аэроквантум', callback_data='Аэроквантум')
        but_6 = types.InlineKeyboardButton(text='Робоквантум', callback_data='Робоквантум')
        but_7 = types.InlineKeyboardButton(text='Руководство', callback_data='Руководство')
        but_8 = types.InlineKeyboardButton(text='Запись на занятия', callback_data='Запись на занятия')
        but_9 = types.InlineKeyboardButton(text='Связь', callback_data='Связь')
        but_10 = types.InlineKeyboardButton(text='Расписание', callback_data='Расписание')
        keyboard.add(but_2, but_3, but_4, but_5, but_6, but_7, but_8, but_9, but_10)
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text="Наноквантум представляет современную инженерную отрасль, направленную на изучение материаловедения"
                                          " на микро- и наноуровнях. Программа квантума призвана побудить интерес к современному естествознанию и новейшим технологиям,"
                                          " повысить качество образования и мотивацию к целостному изучению предметов естественнонаучного цикла."
                                          " Подробнее на сайте: [Кванториум62.рф](https://xn--62-6kch5ajrgjuup.xn--p1ai/nanocantum)", parse_mode='Markdown', reply_markup=keyboard)
        # цикл бота
if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)