from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from create_bot import dp
from keyboards.client_kb import kb_client

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! Выбери пункт из меню или пропиши /",reply_markup=kb_client)
    name = message.from_user.full_name
