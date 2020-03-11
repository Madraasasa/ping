import telebot
import time
import os

token = os.environ.get('TOKEN', '938006327:AAFMpLy69tCZ8HOfI9HZI_0YouVWsvW21Jw')
bot = telebot.TeleBot(token=token)
chat_id = os.environ.get('CHAT_ID', 120929625)
sec = os.environ.get('SEC', 600)
host = os.environ.get('HOST', 'google.com')
key = os.environ.get('KEY', True)


import ping3

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    """
    for i in range(0, 4):
        res = ping3.ping(host)
        time.sleep(1)

    return res


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


