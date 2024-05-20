import aiogram
import asyncio
import logging

from aiogram import Bot,Dispatcher

from config import TOKEN
from app.handlers import router # из папки app файла handlers.py импортируем router

bot=Bot(token=TOKEN)  # бот приниммает параметры токен и инициализирует подключения к нему
dp = Dispatcher()     # основной роутер. обрабатывает входящие обновления



async def main():                # отправляет запрос на сервера. если ответ ест, то бот его обрабатывает
    dp.include_router(router)    # возвращает router
    await dp.start_polling(bot) 

if __name__ == '__main__':        # запускает функцию main()
    logging.basicConfig(level=logging.INFO)  # исполльзовать только в процессе разработке, на проде - выключать
    try:
         asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')