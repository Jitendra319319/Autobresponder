import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")  # Railway environment variable
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Hello! This is Auto Reply 🤖")

bot.infinity_polling()
