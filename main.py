# импортируем все неоходимые модули
# Bot - это класс (ясен пень потом создадим объект), к которому мы обращаемся для отправки сообщений и тд
# types - для работы с сообщением, данными от инлайновых кнопок и тд
# Dispatcher - класс, на основе которого создадим объект, нужен для создание хэндлеров
# executor - для поллинга, т е чтобы бот работал постоянно

from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other
from data_base import sqlite_db

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()

# что происходит при запуске
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)