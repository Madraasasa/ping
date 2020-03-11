import telebot
import time
import os

token = os.environ.get('TOKEN', '938006327:AAFMpLy69tCZ8HOfI9HZI_0YouVWsvW21Jw')
bot = telebot.TeleBot(token=token)
chat_id = os.environ.get('CHAT_ID', 120929625)
sec = os.environ.get('SEC', 600)
host = os.environ.get('HOST', 'google.com')


import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

while True:
    a = ping(host)
    result = host
    if a:
        result += '---- up'
        print('-----')
        bot.send_message(chat_id=chat_id, text=result)
    else:
        result += '---- down'
        bot.send_message(chat_id=chat_id, text=result)
    time.sleep(sec)


