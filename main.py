import asyncio
from aiogram import Bot, Dispatcher
from config import load_config
from handlers import python_handlers


async def main():
    config = load_config()
    bot = Bot(token=config.tg_bot.token,
              parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(python_handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
