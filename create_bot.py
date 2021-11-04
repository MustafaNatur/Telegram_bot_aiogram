from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)

# Теперь пришло время написать админку для бота. По задумке бот отпраляет рад вопросов
# и сохраняет на сервер ряд последущих ответов соответственно