import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, 0)

lightOnTime = 2#hardcoded for now, should be changeable by the user
lightOffTime = 2##hardcoded for now, should be changeable by the user

try:
    while True:
        if(GPIO.input(11)==1):#buttonpress
            while True:
                GPIO.output(12, 1)
                time.sleep(lightOnTime)
                GPIO(12, 0)
                time.sleep(lightOffTime)


except KeyboardInterrupt:
    GPIO.cleanup()