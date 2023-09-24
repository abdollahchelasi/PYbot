import telebot

bot = telebot.TeleBot('6590512531:AAHjC6A270nF9WCdntFhrTUuW5aJbbcVXus')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'سلام!')

bot.polling()
