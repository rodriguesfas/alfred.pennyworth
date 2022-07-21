#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
main.py
"""

import os
import sys
import uuid
import time
import random
import datetime as dt
import telepot

from dotenv import load_dotenv

load_dotenv()

chat_id = os.getenv("telegram.bot.chatid")
bot = telepot.Bot(os.getenv("telegram.bot.token"))


def get_filename():
    """
    @return: path_filename
    """
    directory = os.getenv("path.data.photo")
    current_uuid = uuid.uuid4()
    current_datetime = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ext = ".jpg"
    path_filename = directory + str(current_uuid) + str(current_datetime) + ext
    return path_filename


def get_photo_pygame(filename):
    import pygame
    import pygame.camera

    pygame.camera.init()

    cam_list = pygame.camera.list_cameras()

    if cam_list:
        cam = pygame.camera.Camera(cam_list[0], (640, 480))
        cam.start()
    else:
        bot.sendMessage(chat_id, "Camera is not detected.")

    image = cam.get_image()
    pygame.image.save(image, filename)


def get_photo_imageio(filename):
    import imageio.v3 as iio
    for frame_count, frame in enumerate(iio.imiter("<video0>")):
        iio.imwrite(filename, frame)
        if frame_count > 0:
            break


def handle(msg):
    chat_id = msg["chat"]["id"]
    command = msg["text"]

    print("got command: %s" % command)

    if command == "/photo":
        filename = get_filename()
        #get_photo_pygame(filename)
        get_photo_imageio(filename)
        bot.sendPhoto(chat_id=chat_id, photo=open(filename, "rb"))


bot.message_loop(handle)
print("Esperando Comando...")

while 1:
    time.sleep(10)
