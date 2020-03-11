import telebot
import time
import os

token = os.environ.get('TOKEN', '938006327:AAFMpLy69tCZ8HOfI9HZI_0YouVWsvW21Jw')
bot = telebot.TeleBot(token=token)
chat_id = os.environ.get('CHAT_ID', 120929625)
sec = os.environ.get('SEC', 600)
host = os.environ.get('HOST', 'google.com')
key = os.environ.get('KEY', True)



import requests
from bs4 import BeautifulSoup


def ping(host):
    headers = {"Access-Control-Allow-Origin": "*", 'Content-Type': 'application/json'}

    s = requests.get(f'https://2whois.ru/?t=ping&data={host}')
    # answer = s.text
    bs = BeautifulSoup(s.text)
    answer = bs.find('pre')
    loss = answer.text.find('received')
    packet = answer.text.find('% packet loss')
    result = answer.text[loss+10:packet]
    if int(result) ==100:
        return 0
    else:
        return 1


while True:
    a = ping(host)
    result = host

    if a:
        result += '---- up'
        print(result)
        if key:
            bot.send_message(chat_id=chat_id, text=result)

    else:
        print(result)
        bot.send_message(chat_id=chat_id, text=result)
    time.sleep(sec)
