import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from os import getenv
from dotenv import load_dotenv

from app.handllers import router
from app.DataBase.models import init_db


async def main():
    load_dotenv()
    await init_db()

    token = os.getenv("TOKEN")
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:    
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped by user")