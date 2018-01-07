import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def my_callback(channel):
	print('kek')

GPIO.add_event_detect(21, GPIO.FALLING, callback=my_callback, bouncetime=300)

while True:
	print('lol')
	time.sleep(2)