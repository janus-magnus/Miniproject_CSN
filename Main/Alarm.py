import RPi.GPIO as GPIO
import time

def Init():
    GPIO.setmode(GPIO.BOARD)#pin setups
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#button1 input GPIO
    GPIO.setup(12, GPIO.OUT)#LED Powersource(Als output aan staat is het 3.3V zelfde als pin 1 de standaard powerpin)

status = ''

#aanpasbaare blink time
global LED_off_time
LED_off_time = 2
global LED_on_time
LED_on_time = 2



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
        GPIO.output(12, 1)
        time.sleep(LED_on_time)
        GPIO.output(12, 0)
        time.sleep(LED_off_time)

def Aoff():
    global status
    status = 'exit'
    print('poi')

def AlarmPrime():
    global status
    while True:
        if GPIO.input(11) == 1:
            status = 'on'
        if status == 'on':
            Aon()
        if status == 'exit':
            status = ''
            break

GPIO.cleanup()
