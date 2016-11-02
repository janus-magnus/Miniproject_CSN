import RPi.GPIO as GPIO
import time
import threading


def Init():
    GPIO.setmode(GPIO.BOARD)#pin setups
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#button1 input GPIO
    GPIO.setup(12, GPIO.OUT)#LED Powersource(Als output aan staat is het 3.3V zelfde als pin 1 de standaard powerpin)
    GPIO.setup(37, GPIO.OUT)#button2 output GPIO
    GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.output(37, 1)#set pin 37 aan zodat hij als 3.3V output werkt



#aanpasbaare blink time/ nu nog hardcoded

global LED_off_time
LED_off_time = 2
global LED_on_time
LED_on_time = 2
status = 'go'


def Afaster(): #Make the LED blink faster
    print('hit')
    global LED_off_time
    global LED_on_time
    LED_on_time-=1
    LED_off_time-=1
    print(LED_on_time)

def Aslower(): #Make the LED blink slower
    print('hit')
    global LED_off_time
    global LED_on_time
    LED_off_time+=1
    LED_on_time+=1
    print(LED_on_time)

def Aon(): #Turn on LED
    ticker = 0
    while True:
        if status == 'exit':
            break
        ticker+=1
        GPIO.output(12, 1)
        time.sleep(LED_on_time)
        GPIO.output(12, 0)
        time.sleep(LED_off_time)
        if ticker == 5:
            break

def Aoff():
    global status
    status = 'exit'

def AlarmPrime():
    while True:
        if GPIO.input(11) == 1:
            pt = threading.Thread(target=Aon())
            pt.deamon = True
            pt.start()
            break


GPIO.cleanup()