import telebot
from config import TOKEN
from telebot.types import Message, CallbackQuery
from handlers import handle_interests, handle_feedback, handle_roadmap
from keyboards import main_menu
from database import init_db, get_all_professions

init_db()
professions = get_all_professions()

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message: Message):
    bot.send_message(message.chat.id, "Welcome to the Career Bot! Choose an option:", reply_markup=main_menu())

@bot.message_handler(func=lambda m: m.text == "🔍 Match My Interests")
def match_interests(message: Message):
    bot.send_message(message.chat.id, "What are you interested in? (e.g., technology, art, business)")

@bot.message_handler(func=lambda m: m.text == "💬 Feedback")
def feedback(message: Message):
    bot.send_message(message.chat.id, "We'd love to hear your thoughts! Type your feedback:")
    bot.register_next_step_handler(message, handle_feedback)

@bot.callback_query_handler(func=lambda call: call.data.startswith("roadmap"))
def roadmap_callback(call: CallbackQuery):
    handle_roadmap(bot, call)

@bot.message_handler(func=lambda m: m.text)
def interests_handler(message: Message):
    handle_interests(bot, message)

if __name__ == "__main__":
    bot.polling()
