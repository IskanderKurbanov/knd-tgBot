from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.filters import Command

from bot.core.database import async_session
from bot.models.user import User
from bot.keyboards.user_keyboards import user_keyboard

router = Router()  # Создание роутера


# Обработчик команды /registr
@router.message(Command("registr"))
async def cmd_registr(message: Message):
    """Обработка команды /registr"""

    # Создание клавиатуры
    keyboard = ReplyKeyboardMarkup(
        keyboard=user_keyboard,
        resize_keyboard=True
    )

    async with async_session() as session:
        # Проверка существования пользователя в БД
        user = await session.get(User, message.from_user.id)
        if not user:
            # Создание нового пользователя
            new_user = User(
                user_id=message.from_user.id,
                username=message.from_user.username,
                full_name=message.from_user.full_name
            )
            session.add(new_user)
            await session.commit()
            await message.answer("Добро пожаловать в систему!", reply_markup=keyboard)
        else:
            await message.answer("Вы уже зарегестрированны в системе!", reply_markup=keyboard)