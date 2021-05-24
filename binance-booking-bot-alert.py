import telebot
import requests
import time


API_KEY = 'YOUR-API'

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])

def start(message):
  print(f'>> {message.chat.id}')
  bot.send_message(message.chat.id,'<b> [+] BOT STARTED [+] </b>',parse_mode='html')
  while True:
    try:
    #start request
        r = requests.get("https://api.binance.com/api/v3/ticker/bookTicker", params=dict(symbol="BTCUSDT"))
        btc_top = r.json()
        #get data
        btc_bid = btc_top['bidPrice']
        btc_qty = btc_top['bidQty']
        btc_ask = btc_top['askPrice']
        btc_ask_qty = btc_top['askQty']

            
         # big buy 
        if int(float(btc_qty))*int(float(btc_bid)) >= int(900000):
          p = '🟢🟢🟢🟢🟢'+f'<b>\nBig Buy [ BTC-USDT ] On Binance</b> 🔥'+ f'\n<b>Number of currencies {int(float(btc_qty))}</b>\n'+f'<b>Value of currencies is in USDT {int(float(btc_qty))*int(float(btc_bid))} $ </b>💰'+f'\n<b>BTC/USDT Price {int(float(btc_bid))} $ </b>💸'
          bot.send_message(message.chat.id,p,parse_mode='html')
          time.sleep(1)
        #big sell
        if int(float(btc_ask_qty))*int(float(btc_ask)) >= int(900000):
          p = '🔴🔴🔴🔴🔴'+f'<b>\nBig Sell [ BTC-USDT ] On Binance</b> 🔥'+ f'\n<b>Number of currencies {int(float(btc_ask_qty))}</b>\n'+f'<b>Value of currencies is in USDT {int(float(btc_ask_qty))*int(float(btc_ask))} $ </b>💰'+f'\n<b>BTC/USDT Price {int(float(btc_ask))} $ </b>💸'
          bot.send_message(message.chat.id,p,parse_mode='html')
          time.sleep(1)
    except:
      pass
  

bot.polling()
