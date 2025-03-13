from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot.config import config
from bot.keyboards.menu_commands import bot_commands

# Инициализация бота и диспетчера
bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


async def setup_bot():
    """Настройка бота перед запуском"""
    #from bot.middlewares.admin_middleware import AdminMiddleware
    from bot.handlers import message_handlers, user_handlers #, admin_handlers

    # Подключение middleware
    #dp.message.middleware(AdminMiddleware())

    # Регистрация роутеров
    dp.include_router(user_handlers.router)
    #dp.include_router(admin_handlers.router)
    dp.include_router(message_handlers.router)

    # Установка команд бота
    await bot.set_my_commands(bot_commands)