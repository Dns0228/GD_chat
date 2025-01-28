from telegram import Update
from telegram.ext import ContextTypes
from config import MAX_LENGTH, TEMPERATURE
from models import generate_response

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой русскоязычный ИИ-чатбот. Напиши что-нибудь, и я отвечу!")

# Обработчик команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
    Доступные команды:
    /start - Начать диалог
    /help - Получить справку
    /info - Информация о боте
    """
    await update.message.reply_text(help_text)

# Обработчик команды /info
async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_text = """
    Я - ММ-чатбот, использующий модель GPT-3 от SberBank.
    Могу поддержать беседу на любую тему!
    """
    await update.message.reply_text(info_text)

# Обработчик текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = generate_response(user_input, MAX_LENGTH, TEMPERATURE)
    await update.message.reply_text(response)