import telebot

# Token of the bot in telegram
token = '1358105852:AAGTyGSjOksynswDARWNJAiH9uwKWRMsXws'


def keyboard(buttons: str) -> 'Keyboard':
    """It's the keyboard which appears for /start and /help commands"""
    current_keyboard = telebot.types.ReplyKeyboardMarkup(True)
    for button in buttons:
        current_keyboard.add(button)
    return current_keyboard


def check_the_list_for_matching(checked_list: list, phrase_to_match: str) -> bool:
    """The function checks whether the phrase from the user starts with any element
    in the list.
    """
    for word in checked_list:
        if phrase_to_match.startswith(word):
            return True
    return False
