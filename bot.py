from funcs import *
from time import sleep
from telebot import types
from picamera import PiCamera
from playsound import playsound
import RPi.GPIO as GPIO
import config,telebot

camera = PiCamera()
camera.vflip = True
camera.hflip = True

bot = telebot.TeleBot(config.token)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "чтобы получить фото с домофона, нажми /photo")
    print(message.chat.id)
@bot.message_handler(content_types=["voice"])
def down_audio(message):
    to_down=bot.download_file(bot.get_file(message.voice.file_id).file_path)
    with open('new.ogg', 'wb') as new_file:
        new_file.write(to_down)
@bot.message_handler(func = lambda:not(GPIO.input(21)))
def button():
    print(1)
    sleep(0.2)

if __name__ == '__main__':
    bot.polling(none_stop=True)