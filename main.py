import asyncio
from bot.core import bot as core_bot, database, scheduler


async def main():
    await database.init_db()  # Инициализация БД
    await core_bot.setup_bot()  # Настройка бота
    #scheduler.setup_scheduler()  # Запуск планировщика FIXIT

    await core_bot.dp.start_polling(core_bot.bot)  # Запуск бота


if __name__ == "__main__":
    asyncio.run(main())