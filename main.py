from funcs import *
from time import sleep
from telebot import types
from picamera import PiCamera
from playsound import playsound
import RPi.GPIO as GPIO
import config,telebot

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)

camera = PiCamera()
camera.vflip = True
camera.hflip = True

bot = telebot.TeleBot(config.token)

names = {'George':'егор',
         'Irina':'ирка',
         'Artem':'артем'}

while True:
    if GPIO.input(21) == False:
        path='./guests/new.jpg'
        camera.start_preview(fullscreen=True)
        sleep(4)
        camera.stop_preview()
        camera.capture(path)
        print('guest')
        name=who_is(path, 0)
        print(name)
        if name!=None:
            playsound('./voice/'+name+'.mp3')
            bot.send_photo(chat_id=202226598, photo=open('./guests/new.jpg', 'rb'))
            bot.send_message(202226598,'пришел '+names[name])
        else:
            bot.send_photo(chat_id=202226598, photo=open('./guests/new.jpg', 'rb'))
            bot.send_message(202226598,'кто-то пришел')
        sleep(0.2)
