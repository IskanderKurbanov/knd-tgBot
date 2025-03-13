import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

class Config:
    BOT_TOKEN = os.getenv('BOT_TOKEN')  # Токен бота
    ADMIN_IDS = ['522551359'] #list(map(int, os.getenv('ADMIN_IDS', '').split(',')))  # ID администраторов
    DB_URL = os.getenv('DB_URL', 'sqlite+aiosqlite:///database.db')  # URL базы данных

config = Config()