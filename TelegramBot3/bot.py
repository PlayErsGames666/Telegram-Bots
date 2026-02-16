import telebot
import config
import requests

from config import TOKEN
from telebot import types


bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я калькулятор бот. Просто введите выражение для расчета.")

# Обработчик всех сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        result = eval(message.text)  # Вычисляем результат выражения
        bot.send_message(message.chat.id, f"Результат: {result}")
    except Exception as e:
        bot.send_message(message.chat.id, "Ошибка при вычислении. Пожалуйста, введите правильное выражение.")

# Запускаем бота
bot.polling(non_stop=True)
