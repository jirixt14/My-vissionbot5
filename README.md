# Myvission_CZbot

Telegram bot pro:
- sledování bonusů (např. z IG Story @cashinovybuh)
- hlasové upozornění
- správu dropshipping inzerátů
- režim tichého provozu 23:00–5:00

## Nasazení na Render
1. Vytvoř nový web service z GitHub repozitáře
2. Build command: `pip install pip install pytelegrambotapi flask`
3. Start command: `python main.py`
4. Přidej ENV proměnnou `TELEGRAM_TOKEN`

## Spuštění lokálně
```bash
export TELEGRAM_TOKEN=tvuj_token
python bot.py
```
