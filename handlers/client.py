from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client

from aiogram.types import ReplyKeyboardRemove

from data_base import sqlite_db



# @dp.message_handler(commands=["/help"])
async def commands_help(message: types.Message):
    await bot.send_message(message.from_user.id, 'Инструкция бота: ')

# @dp.message_handler(commands=['/Режим_работы'])
async def command_time(message: types.Message):
    await bot.send_message(message.from_user.id, 'Магазин работает ПН - ПТ с 8:00 до 23:00')

# @dp.message_handler(commands=['/Расположение_для_самовывоза'])
async def command_place(message: types.Message):
    await bot.send_message(message.from_user.id, 'Магазин находится по адресу: ул. Кузнецкий Мост, 14, Москва, 101701')
    await bot.send_location(message.chat.id, 55.7483879, 37.5654407)

# @dp.message_handler(commands=['/Контакты'])
async def command_contact(message: types.Message):
    await bot.send_message(message.from_user.id, 'Телефон для заказа: +7(985)123-45-67')

# @dp.message_handler(commands=['/Оплата'])
async def command_pay(message: types.Message):
    await bot.send_message(message.from_user.id, f'Оплата производиться после соглосования с менеджером по телефону \n'
                                                 'Способы оплаты:\n 1. Картой \n 2. Переводом на счет \n 3. Наличными')

# @dp.message_handler(commands=['/Каталог'])
async def command_menu(message: types.Message):
    await sqlite_db.sql_read(message)


# Регистрация хендлеров
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_help, text='/help')
    dp.register_message_handler(command_time, text='🕑Режим работы')
    dp.register_message_handler(command_place, text='📍Расположение на карте')
    dp.register_message_handler(command_menu, text='👟Каталог')
    dp.register_message_handler(command_contact, text='☎Контакты')
    dp.register_message_handler(command_pay, text='💸Оплата')

