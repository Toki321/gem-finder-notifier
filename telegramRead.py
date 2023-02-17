import os

import telebot

BOT_TOKEN = os.environ.get("5661039372:AAHQS5AcSAHk8HYaxZ_H4A3Y_Gj2wQjHQEs")

bot = telebot.TeleBot(BOT_TOKEN)

while True:

    @bot.message_handler(commands=["start", "hello"])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, how are you doing?")

    @bot.message_handler(func=lambda msg: True)
    def echo_all(message):
        bot.reply_to(message, message.text)
