from picamera import PiCamera
from time import sleep
from funcs import *
import RPi.GPIO as GPIO
import pygame, os


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)

camera = PiCamera()
camera.vflip = True
camera.hflip = True

while True:
    if GPIO.input(21) == False:
        path='./guests/new.jpg'
        camera.capture(path)
        camera.start_preview()
        sleep(4)
        camera.stop_preview()
        name=who_is(path, 0)
        print(name)
        if name!=None:
            pygame.mixer.Sound('./voice/'+name+'.wav').play()

        sleep(0.2)
