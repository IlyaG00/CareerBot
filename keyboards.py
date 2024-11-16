from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = KeyboardButton("📜 List Professions")
    btn2 = KeyboardButton("🔍 Match My Interests")
    btn3 = KeyboardButton("🗺️ Professional Roadmap")
    btn4 = KeyboardButton("💬 Feedback")
    markup.add(btn1, btn2, btn3, btn4)
    return markup

def profession_details_buttons(profession):
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("Roadmap", callback_data=f"roadmap:{profession}")
    btn2 = InlineKeyboardButton("More Details", callback_data=f"details:{profession}")
    markup.add(btn1, btn2)
    return markup