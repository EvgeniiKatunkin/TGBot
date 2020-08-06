import telebot

# Token of the bot in telegram
token = '1358105852:AAGTyGSjOksynswDARWNJAiH9uwKWRMsXws'


# Keyboards
def keyboard(*args):
    current_keybooard = telebot.types.ReplyKeyboardMarkup(True, True)
    current_keybooard.row(*args)
    return current_keybooard
