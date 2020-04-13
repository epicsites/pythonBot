import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, text = 'Hello, {0.first_name}'.format(message.from_user))

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)
    print(message.text)
#RUN
bot.polling(none_stop=True)