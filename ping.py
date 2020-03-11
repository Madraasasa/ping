import telebot
import time
import os


bot = telebot.TeleBot(token='938006327:AAFMpLy69tCZ8HOfI9HZI_0YouVWsvW21Jw')
chat_id = 120929625
sec = 600

def ping(hostname):
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        # print(hostname, 'is up!')
        return 0
    else:
        # print(hostname, 'is down!')
        return 1


while True:
    a = ping('google.com')
    print(a)
    bot.send_message(chat_id=chat_id, text= f'result --{a}')
    time.sleep(sec)



