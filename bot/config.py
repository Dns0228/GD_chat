import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("Токен Telegram-бота не найден. Убедитесь, что он указан в .env.")

# Настройки модели
MODEL_NAME = "ai-forever/ruGPT-3"
MAX_LENGTH = 750  # Максимальная длина ответа
TEMPERATURE = 0.5  # Креативность модели (от 0 до 1)