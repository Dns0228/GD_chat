from telegram import Update
from telegram.ext import CallbackContext
from transformers import pipeline

# Инициализация модели
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я твой чат-бот. Напиши мне что-нибудь!')

def reply(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    response = chatbot(user_message)[0]['generated_text']
    update.message.reply_text(response)