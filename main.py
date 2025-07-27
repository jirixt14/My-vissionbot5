import logging
import os
from flask import Flask, request
import telegram
from telegram import Update
from telegram.ext import Dispatcher, CommandHandler, CallbackContext

TOKEN = os.getenv("BOT_TOKEN", "8304347353:AAHRKFhNgqsSweIBYPgLhl7UDn7GcszllFw")
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

# Nastavení loggeru
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Základní příkazy
def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 Ahoj! Já jsem MyVisionBot.\n\n📌 Dostupné příkazy:\n\n"
                              "🎁 /bonusy – Aktuální casino bonusy\n"
                              "🛒 /produkty – Dropshipping produkty\n"
                              "🔊 /testhlas – Test hlasového výstupu")

def bonusy(update: Update, context: CallbackContext):
    update.message.reply_text("🎁 Nejnovější bonus: Získej 200 free spinů – více na https://t.me/casinoczskbonusy")

def produkty(update: Update, context: CallbackContext):
    update.message.reply_text("🛒 Dnešní doporučený produkt:\nXiaomi Smart Band 7 – jen 799 Kč!\nVíce info: napiš /start")

def testhlas(update: Update, context: CallbackContext):
    update.message.reply_text("🔊 Připravuji hlasové upozornění… (zatím jen textově)")
    # Zde později přidáme přehrání hlasu

# Nastavení webhooku
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

# Kontrolní route
@app.route('/')
def index():
    return '✅ MyVisionBot běží!'

# Připojení handlerů
dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('bonusy', bonusy))
dispatcher.add_handler(CommandHandler('produkty', produkty))
dispatcher.add_handler(CommandHandler('testhlas', testhlas))

# Nastavení webhooku při startu
if __name__ == '__main__':
    URL = "https://my-vissionbot5.onrender.com"
    bot.delete_webhook()
    bot.set_webhook(url=f"{URL}/{TOKEN}")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
