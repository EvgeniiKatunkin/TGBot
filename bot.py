import config
import telebot

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi, you said /start', reply_markup=config.keyboard('Hi', 'Goodbye'))


@bot.message_handler(content_types=['text'])
def send_text(message):
    message_from_user = message.text.lower()
    if message_from_user == 'hi':
        bot.send_message(message.chat.id, 'Hello!')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBJ_xfLDu0qjM1nO_iVLcVJhMqzhuu1wAChgUAApb6EgXDE3t9v5CP8BoE')
    elif message_from_user == 'goodbye':
        bot.send_message(message.chat.id, 'See you later!')


if __name__ == '__main__':
    bot.polling()
