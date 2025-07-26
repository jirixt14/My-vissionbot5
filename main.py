
import os
import telebot
from flask import Flask, request

TOKEN = os.getenv("BOT_TOKEN", "8304347353:AAHRKFhNgqsSweIBYPgLhl7UDn7GcszllFw")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Myvission_CZbot je připraven!")

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your-render-app-url.onrender.com/' + TOKEN)
    return "Webhook nastaven!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
