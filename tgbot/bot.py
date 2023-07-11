import os
import telebot
from telebot import types
from generator import Generator

BOT_TOKEN = os.environ.get('NICEQR_BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Generator('123').generate(url='https://google.com', prompt='')

@bot.message_handler(commands = ['generate', 'g'])
def generate(message):
    send_message = bot.send_message(message.from_user.id, "Ведите URL")
    bot.register_next_step_handler(send_message, url_handler)


def url_handler(message):
    url = message.text
    send_message = bot.send_message(message.from_user.id, "Введите описание")
    bot.register_next_step_handler(send_message, prompt_handler, url)


def prompt_handler(message, url):
    prompt = message.text
    bot.send_message(message.from_user.id, "Ваш url: " + url + ", ваш prompt: " + prompt)
    generator = Generator(message.from_user.id)
    qrpath = generator.generate(url, prompt)
    decodeResult = generator.decodeQr(qrpath)
    qrimg = open(qrpath, 'rb')
    bot.send_message(message.from_user.id, "Ваш QR:")
    bot.send_photo(message.chat.id, qrimg)
    bot.send_message(message.chat.id, "Результат декодирования:")
    bot.send_message(message.chat.id, decodeResult)


bot.infinity_polling()
