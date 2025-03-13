from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()  # Создание роутера


# Обработчик команды /start
@router.message(Command("start"))
async def cmd_start(message: Message):
    """Обработка команды /start"""

    await message.answer("Добро пожаловать!")


# Обработчик команды /help
@router.message(Command("help"))
async def cmd_help(message: Message):
    """Обработка команды /help"""

    await message.answer("Этот бот является шаблоном для проектов!")


@router.message()
async def handle_message(message: Message):
    """Обработка всех сообщений"""
    await message.answer("Ваше сообщение получено!")