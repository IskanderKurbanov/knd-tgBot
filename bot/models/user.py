from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from bot.core.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)  # ID пользователя
    user_id = Column(Integer, unique=True)  # Telegram ID пользователя
    username = Column(String(50))  # Имя пользователя в Telegram
    full_name = Column(String(100))  # Полное имя пользователя
    is_admin = Column(Boolean, default=False)  # Флаг администратора
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # Дата создания

    def __repr__(self):
        return f"<User {self.user_id} {self.username}>"