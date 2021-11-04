from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button1 = KeyboardButton('📍Расположение на карте')
button2 = KeyboardButton('🕑Режим работы')
button3 = KeyboardButton('👟Каталог')
button4 = KeyboardButton('☎Контакты')
button5 = KeyboardButton('💸Оплата')
# Кнопки исключения
#button4 = KeyboardButton('Мой номер', request_contact=True)
#button5 = KeyboardButton('Отправить где я', request_location=True)

# Замещает обычнуюю клаву на нашу
# one_time_keyboard=True - чтобы клавиатура пропадала
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

# Здесь мы добавляем наши кнопки в клавиатуру. Для этого есть 3 способа
# 1. С помощью add
# kb_client.add(button1).add(button2).insert(button3)

# kb_client.row(button3,button2,button1)

kb_client.add(button1).row(button3, button2).row(button4, button5)