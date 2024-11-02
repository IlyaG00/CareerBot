import telebot
from config import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    send_welcome(bot, message)

@bot.message_handler(func=lambda message: message.text == "Список профессий")
def show_professions(message):
    handle_message(bot, message)

@bot.message_handler(commands=['details'])
def profession_details(message):
    send_profession_details(bot, message)

@bot.message_handler(commands=['menu'])
def menu(message):
    send_menu(bot, message)

# Запуск бота
bot.polling()