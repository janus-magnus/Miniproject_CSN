import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)#pin setups
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#button1 input GPIO
GPIO.setup(12, GPIO.OUT)#LED Powersource(Als output aan staat is het 3.3V zelfde als pin 1 de standaard powerpin)
GPIO.setup(37, GPIO.OUT)#button2 output GPIO
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(37, 1)#set pin 37 aan zodat hij als 3.3V output werkt

#aanpasbaare blink time/ nu nog hardcoded
LED_off_time = 2
LED_on_time = 2


def Aon():
    while True:
            if GPIO.input(36):#button2 moet ingedrukt blijven worden tot hij stopt
                break
            GPIO.output(12, 1)
            time.sleep(LED_on_time)
            GPIO.output(12, 0)
            time.sleep(LED_off_time)


while True:
    if GPIO.input(11) == 1:
        Aon()

GPIO.cleanup()