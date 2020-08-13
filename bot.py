import telebot
import config
import content

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def send_help(message):
    """The handler for /start and /help commands"""
    bot.send_message(message.chat.id, 'Hei, ' + message.from_user.first_name +
                     '! Рад тебя видеть! Чем могу помочь?',
                     reply_markup=config.keyboard(content.main_menu))


@bot.message_handler(content_types=['text'])
def send_text(message):
    """The handler for text messages"""
    message_from_user = message.text.lower()
    if message_from_user in content.hello:
        bot.send_message(message.chat.id, 'Hei, ' + message.from_user.first_name + '!')
        bot.send_sticker(message.chat.id, content.stickers['hello'])
    elif message_from_user in content.goodbye:
        bot.send_message(message.chat.id, 'Рад был помочь! Beste ønsker!')
        bot.send_sticker(message.chat.id, content.stickers['goodbye'])
    elif message_from_user == 'где ты находишься?':
        bot.send_location(message.chat.id, 58.968060, 5.732880)
    elif message_from_user == 'о боте':
        bot.send_message(message.chat.id, 'Я здесь чтобы помочь тебе с наиболее часто '
                                          'задаваемыми вопросами. Что тебя интересует?')
    else:
        bot.send_message(message.chat.id, "Даже не знаю, что на это ответить...")
        bot.send_sticker(message.chat.id, content.stickers['i_dont_know'])


# The infinite bot execution
if __name__ == '__main__':
    bot.polling()
