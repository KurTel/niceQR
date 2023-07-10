import os
import telebot
from telebot import types

BOT_TOKEN = os.environ.get('NICEQR_BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

url= ''
prompt=''

@bot.message_handler(commands = ['generate', 'g'])
def generate(message):
    send_message = bot.send_message(message.from_user.id, "Ведите URL")
    bot.register_next_step_handler(send_message, url_handler)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


def url_handler(message):
    url = message.text
    send_message = bot.send_message(message.from_user.id, "Введите описание")
    bot.register_next_step_handler(send_message, prompt_handler)


def prompt_handler(message):
    prompt = message.text
    bot.send_message(message.from_user.id, "Ваш url: " + url + ", ваш prompt: " + prompt)


bot.infinity_polling()
