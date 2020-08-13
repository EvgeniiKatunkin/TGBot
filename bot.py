import telebot
import config
import content

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def send_help(message):
    bot.send_message(message.chat.id, 'Hi! I have a menu if you need help:',
                         reply_markup=config.keyboard(content.main_menu))


@bot.message_handler(content_types=['text'])
def send_text(message):
    message_from_user = message.text.lower()
    if message_from_user == 'hi':
        bot.send_message(message.chat.id, 'Hei, ' + message.from_user.first_name + '!')
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAEBJ_xfLDu0qjM1nO_iVLcVJhMqzhuu1wAChgUAApb6EgXDE3t9v5CP8BoE')
    elif message_from_user == 'goodbye':
        bot.send_message(message.chat.id, 'See you later!')
    elif message_from_user == 'location':
        bot.send_location(message.chat.id, 58.968060, 5.732880)
    else:
        bot.send_message(message.chat.id, "I don't know what to say...")


if __name__ == '__main__':
    bot.polling()
