import telebot
from whoid import *
from tokens import TOKEN, BOT_TAG

bot = telebot.TeleBot(TOKEN)
tg_auth = WhoID_TG()

@bot.message_handler(commands=['start'])
def start(message):
    status = tg_auth.link_message(bot, message)
    print(status)

@bot.message_handler(commands=['go'])
def go(message):
    chat_id = message.chat.id
    keyboard = tg_auth.create_button(BOT_TAG)
    bot.send_message(chat_id, 'Войти', reply_markup=keyboard)

bot.polling()