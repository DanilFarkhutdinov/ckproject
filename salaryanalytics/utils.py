import telegram
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def send_telegram_message(message: str):
    try:
        bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
        chat_id = settings.TELEGRAM_CHAT_ID
        bot.send_message(chat_id=chat_id, text=message)
    except Exception as e:
        logger.error(f"Failed to send message: {e}")