from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from bot.config import config

# Базовый класс для моделей SQLAlchemy
Base = declarative_base()

# Инициализация асинхронного движка БД
engine = create_async_engine(config.DB_URL, echo=True)

# Создание фабрики асинхронных сессий
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def init_db():
    """Инициализация базы данных (создание таблиц)"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)