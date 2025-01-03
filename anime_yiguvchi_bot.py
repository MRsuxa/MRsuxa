from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Anime ma'lumotlari
anime_data = {
    "romantik": ["Anime 1", "Anime 2"],
    "fantastik": ["Anime 3", "Anime 4"],
    "detektiv": ["Anime 5", "Anime 6"],
    "kundalik_hayot": ["Anime 7", "Anime 8"],
    "sport": ["Anime 9", "Anime 10"],
    "yillar": {
        "2023": ["Anime 3", "Anime 9"],
        "2022": ["Anime 1", "Anime 5"],
    }
}

# Boshlang'ich menyu
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Janr", callback_data="janr")],
        [InlineKeyboardButton("Barcha Animelar", callback_data="barcha")],
        [InlineKeyboardButton("YIL", callback_data="yil")],
        [InlineKeyboardButton("Buyurtma", callback_data="buyurtma")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Tanlang:", reply_markup=reply_markup)

# Callback tugmalar
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "janr":
        keyboard = [
            [InlineKeyboardButton("Romantik", callback_data="romantik")],
            [InlineKeyboardButton("Fantastik", callback_data="fantastik")],
            [InlineKeyboardButton("Detektiv", callback_data="detektiv")],
            [InlineKeyboardButton("Kundalik Hayot", callback_data="kundalik_hayot")],
            [InlineKeyboardButton("Sport", callback_data="sport")],
        ]
        query.edit_message_text("Janrni tanlang:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data in anime_data:
        animelar = anime_data[query.data]
        buttons = [[InlineKeyboardButton(anime, callback_data=f"anime_{anime}")] for anime in animelar]
        query.edit_message_text("Animelar:", reply_markup=InlineKeyboardMarkup(buttons))

    elif query.data == "barcha":
        animelar = sum(anime_data.values(), [])
        buttons = [[InlineKeyboardButton(anime, callback_data=f"anime_{anime}")] for anime in animelar]
        query.edit_message_text("Barcha animelar:", reply_markup=InlineKeyboardMarkup(buttons))

    elif query.data == "yil":
        keyboard = [
            [InlineKeyboardButton("2023", callback_data="2023")],
            [InlineKeyboardButton("2022", callback_data="2022")],
        ]
        query.edit_message_text("Yilni tanlang:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data in anime_data["yillar"]:
        animelar = anime_data["yillar"][query.data]
        buttons = [[InlineKeyboardButton(anime, callback_data=f"anime_{anime}")] for anime in animelar]
        query.edit_message_text(f"{query.data}-yildagi animelar:", reply_markup=InlineKeyboardMarkup(buttons))

    elif query.data.startswith("anime_"):
        anime = query.data.replace("anime_", "")
        query.edit_message_text(f"Tanlangan anime: {anime}")

# Asosiy kod
def main():
    updater = Updater("7528734568:AAHi2nzikqx8yY1DPzYR9V74TfoxCJS5om4")  # Tokeningiz kiritildi
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if name == "main":
    main()
