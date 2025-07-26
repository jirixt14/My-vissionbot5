from flask import Flask, request
import telebot
import os

TOKEN = "8304347353:AAHRKFhNgqsSweIBYPgLhl7UDn7GcszllFw"
bot = telebot.TeleBot(TOKEN, threaded=False)
app = Flask(__name__)

# Základní testovací route (Render vyžaduje GET /)
@app.route('/', methods=['GET'])
def index():
    return "MyVisionBot běží správně."

# Route pro příjem zpráv od Telegramu (webhook)
@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

# Reakce na příkaz /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "👋 Ahoj! Já jsem MyVisionBot a jsem připraven pomáhat. Napiš /bonusy nebo /produkty.")

# Reakce na příkaz /bonusy
@bot.message_handler(commands=['bonusy'])
def bonusy(message):
    bot.send_message(message.chat.id, "🎁 Právě kontroluji nejnovější bonusy... Sleduj kanál: https://t.me/casinoczskbonusy")

# Reakce na příkaz /produkty
@bot.message_handler(commands=['produkty'])
def produkty(message):
    bot.send_message(message.chat.id, "🛒 Tady je aktuální nabídka dropshipping produktů (zatím test).")

# Reakce na příkaz /testhlas
@bot.message_handler(commands=['testhlas'])
def testhlas(message):
    bot.send_message(message.chat.id, "🔊 Ahoj! Právě jsem našel nový bonus – zkontroluj svůj Telegram kanál a vydělej!")

# Spuštění aplikace
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port)
