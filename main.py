from aiogram import Bot, Dispatcher
import asyncio

from handlers import bot_messages, user_commands
from utils.token import TOKEN

async def main():
    bot = Bot(TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    dp.include_routers(
        user_commands.router,
        bot_messages.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())