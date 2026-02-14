import config
import telebot
import requests
import json
import os

from telebot import types
from config import  *

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sti = open(os.path.join(os.path.dirname(__file__), 'picture', 'sun.png'), 'rb')

    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Ташкент")
    item2 = types.KeyboardButton("Навои")
    item3 = types.KeyboardButton("Самарканд")
    item4 = types.KeyboardButton("Фергана")
    item5 = types.KeyboardButton("Джизак")
    item6 = types.KeyboardButton("Хива")
    item7 = types.KeyboardButton("Андижан")
    item8 = types.KeyboardButton("Бухара")
    item9 = types.KeyboardButton("Кашкадарья")
    item10 = types.KeyboardButton("Наманган")
    item11 = types.KeyboardButton("Surkhandarya")
    item12 = types.KeyboardButton("Sirdaryo")
    item13 = types.KeyboardButton("Нукус")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.\nНапишите название города и вам выйдет температура и погода.".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        tem = data['weather'][0]['description']
        bot.reply_to(message, f"Сейчас погода: {temp, tem}")


        image = 'picture/sun.png' if temp > 5.0 else 'picture/sunny.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f"Город указан не верно")




bot.polling(non_stop=True)


