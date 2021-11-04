from aiogram import types, Dispatcher
from create_bot import dp
import json, string


# @ dp.message_handler()
async def echo_send(message: types.Message):
    if message.text == 'Привет':
        # await message.answer('И тебе привет (message.answer)')
        await message.reply('И тебе привет (message.reply)')
        # Для ответа на сообщение
        # await bot.send_message(message.from_user.id, 'И тебе привет (bot.send_message)')
        # #Для ответ на сообщение конкретно человеку который добавился к боту по его  ID

    # Регистрация хендлеров
def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
