from keyboards import main_menu, profession_details_buttons
from logger import log_user_action
from database import get_professions_by_interest, get_profession_roadmap

def handle_interests(bot, message):
    log_user_action(message.chat.id, f"Interest search: {message.text}")
    results = get_professions_by_interest(message.text)
    if results:
        bot.send_message(
            message.chat.id,
            "Here are some professions based on your interest:",
            reply_markup=main_menu(),
        )
        for profession in results:
            bot.send_message(
                message.chat.id, profession, reply_markup=profession_details_buttons(profession)
            )
    else:
        bot.send_message(message.chat.id, "No matching professions found. Try another interest.")

def handle_feedback(bot, message):
    bot.send_message(message.chat.id, "Thank you for your feedback! We'll improve.")

def handle_roadmap(bot, call):
    profession = call.data.split(":")[1]
    roadmap = get_profession_roadmap(profession)
    bot.send_message(call.message.chat.id, f"Roadmap for {profession}:\n{roadmap}")