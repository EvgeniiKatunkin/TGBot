import telebot
import config
import content

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def send_help(message):
    """The handler for /start and /help commands"""
    bot.send_message(message.chat.id, 'Привет! У меня есть меню для тебя:',
                     reply_markup=config.keyboard(content.main_menu))


@bot.message_handler(commands=['location'])
def send_location(message):
    """The handler for /location command"""
    bot.send_location(message.chat.id, 58.968060, 5.732880)


@bot.message_handler(content_types=['text'])
def send_text(message):
    """The handler for text messages"""
    message_from_user = message.text.lower()
    if message_from_user in content.hello:
        bot.send_message(message.chat.id, 'Hei, ' + message.from_user.first_name
                         + '! Рад тебя видеть! Чем могу помочь?')
        bot.send_sticker(message.chat.id, content.stickers(0))
    elif message_from_user in content.goodbye:
        bot.send_message(message.chat.id, 'Рад был помочь! Beste ønsker!')
        bot.send_sticker(message.chat.id, content.stickers(1))
    elif message_from_user == 'location':
        bot.send_location(message.chat.id, 58.968060, 5.732880)
    else:
        bot.send_message(message.chat.id, "Даже не знаю, что на это ответить...")


# The infinite bot execution
if __name__ == '__main__':
    bot.polling()
