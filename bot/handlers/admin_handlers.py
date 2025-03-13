from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

from bot.core.database import async_session
from bot.models.user import User

router = Router()  # Создание роутера для админских команд


# Обработчик команды /admin FIXIT!!!
@router.message(Command("admin"))
async def admin_panel(message: Message):
    """Панель администратора"""
    async with async_session() as session:
        users = await session.execute(User) # FIXIT
        users_list = users.scalars().all()

    # Создание клавиатуры с пользователями
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"User {user.user_id}", callback_data=f"edit_{user.user_id}")]
        for user in users_list
    ])

    await message.answer("Список пользователей:", reply_markup=keyboard)