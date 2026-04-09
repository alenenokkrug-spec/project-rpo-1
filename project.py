import asyncio
import aiogram
import logging
from idlelib.pyshell import usage_msg
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from commands import user
from callbackHandler import callback
from training import trainings
from information import info
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="8777465379:AAG2lyz_PgAod-4hLf752XCrd0OHiA5u6DI")
# Диспетчер
dp = Dispatcher()


# Запуск процесса поллинга новых апдейтов



async def main():
    dp.include_router(trainings)
    dp.include_router(user)
    dp.include_router(callback)
    dp.include_router(info)
    await dp.start_polling(bot)
if __name__ == "__main__":
    (asyncio.run(main()))

