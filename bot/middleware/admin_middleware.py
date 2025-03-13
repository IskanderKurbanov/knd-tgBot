from aiogram import Dispatcher
from aiogram.types import Message
from bot.config import config

class AdminMiddleware:
    async def __call__(self, handler, event: Message, data):
        # Проверка, является ли пользователь администратором
        if event.from_user.id in config.ADMIN_IDS:
            return await handler(event, data)
        await event.answer("У вас нет доступа к этой команде.")