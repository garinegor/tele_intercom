from picamera import PiCamera
from time import sleep
from funcs import *
from playsound import playsound
import RPi.GPIO as GPIO



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
        camera.start_preview(fullscreen=True)
        sleep(4)
        camera.stop_preview()
        camera.capture(path)
        print('guest')
        name=who_is(path, 0)
        print(name)
        if name!=None:
            playsound('./voice/'+name+'.mp3')

        sleep(0.2)
