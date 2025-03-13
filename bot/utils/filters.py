from aiogram import Dispatcher
from aiogram.types import Message

class IsAdmin:
    async def __call__(self, message: Message):
        return message.from_user.id in config.ADMIN_IDS