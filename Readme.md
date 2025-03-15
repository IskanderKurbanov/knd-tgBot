# Aiogram template bot


libs: aiogram, aiosqlite, apscheduler, pydantic, sqlalchemy, loguru, pytest


## Project tree
~~~
project-root/
│
├── bot/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── bot.py
│   │   ├── database.py
│   │   ├── logs.py
│   │   └── scheduler.py
│   │
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── admin_handlers.py
│   │   ├── user_handlers.py
│   │   └── message_handlers.py
│   │
│   ├── middlewares/
│   │   ├── __init__.py
│   │   └── admin_middleware.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   └── filters.py
│   │
│   └── config.py
│
├── tests/
│   ├── __init__.py
│   └── tests_1.py
│
├── requirements.txt
├── main.py
└── .env
~~~

## Run project

1. Install requirements
```commandline
pip install -r requirements.txt
```
2. create and edit .env file
```commandline
BOT_TOKEN="your telegram bot token"
ADMIN_IDS=["some int id"]
#DB_URL="sqlite:///database.db"
```
3. run main.py
```commandline
python main.py
```