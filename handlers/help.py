from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from create_bot import dp
from keyboards.client_kb import kb_client


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку")

    await message.answer("\n".join(text))