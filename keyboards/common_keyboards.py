from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_start_keyboard():
    start_button = KeyboardButton(text='/start')
    help_button = KeyboardButton(text='/help')
    
    buttons = [
        [start_button, help_button]
    ]
    
    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return markup