from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from bot.core.bot import bot
from bot.core.database import async_session
from bot.models.user import User

scheduler = AsyncIOScheduler()  # Инициализация планировщика

async def send_notification():
    """Рассылка сообщений всем пользователям"""
    async with async_session() as session:
        users = await session.execute(select(User)) # FIXIT
        for user in users.scalars().all():
            await bot.send_message(
                chat_id=user.user_id,
                text="Ежедневное уведомление!"
            )

def setup_scheduler():
    """Настройка планировщика"""
    scheduler.add_job(
        send_notification,
        CronTrigger(hour=12, minute=0)  # Ежедневно в 12:00
    )
    scheduler.start()