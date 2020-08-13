import telebot

# Token of the bot in telegram
token = '1358105852:AAGTyGSjOksynswDARWNJAiH9uwKWRMsXws'


def keyboard(buttons):
    """It's the keyboard which appears for /start and /help commands"""
    current_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    for button in buttons:
        current_keyboard.row(button)
    return current_keyboard
