#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
main.py
"""

import os
import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

from dotenv import load_dotenv
load_dotenv()

chat_id = os.getenv('telegram.bot.chatid')
bot = telepot.Bot(os.getenv('telegram.bot.token'))

 
GPIO.setwarnings(False)
 
#LED
def On(pin):
    GPIO.output(pin,GPIO.HIGH)
    return


def Off(pin):
    GPIO.output(pin,GPIO.LOW)
    return


# Numero dos pinos da Raspberry PI configurada no modo BOARD.
GPIO.setmode(GPIO.BOARD)

# Define pino 13 como saída
GPIO.setup(13, GPIO.OUT)
 
# Comandos que vem do software Telegram e sao processados pela Raspberry PI
 
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('got command: %s' % command)
 
    if command == 'On':
        bot.sendMessage(chat_id, On(13))
    if command =='Off':
        bot.sendMessage(chat_id, Off(13))
    if command =='Foto':
        # Envia a foto tirada para o software telegram através do Chat_ID
        bot.sendPhoto(chat_id=chat_id, photo=open('./Capture.jpg', 'rb'))
        # Permite que os comandos digitados no telegram sejam enviados a Raspberry PI
        
        
bot.message_loop(handle)
print('Esperando Comando...')

while 1:
    time.sleep(10)