from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Init your keyboard

keyboard_b = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bitcoin 💰"),
            KeyboardButton(text="Ethereum 🔥"),

        ],
    ],
    resize_keyboard=True
)