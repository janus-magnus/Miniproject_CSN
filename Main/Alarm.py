import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)#pin setups
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#button1 input GPIO
GPIO.setup(12, GPIO.OUT)#LED Powersource(Als output aan staat is het 3.3V zelfde als pin 1 de standaard powerpin)
GPIO.setup(37, GPIO.OUT)#button2 output GPIO
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(37, 1)#set pin 37 aan zodat hij als 3.3V output werkt

LED_off_time = int()
LED_on_time = int()
Astatus = True


#aanpasbaare blink time/ nu nog hardcoded
def Init():
    global LED_off_time
    LED_off_time = 2
    global LED_on_time
    LED_on_time = 2

def Afaster(): #Make the LED blink faster
    global LED_off_time
    global LED_on_time
    LED_on_time-=1
    LED_off_time-=1

def Aslower(): #Make the LED blink slower
    global LED_off_time
    global LED_on_time
    LED_off_time+=1
    LED_on_time+=1

def Aon(): #Turn on LED

    while Astatus == True:
        GPIO.output(12, 1)
        time.sleep(LED_on_time)
        GPIO.output(12, 0)
        time.sleep(LED_off_time)

def Aoff():
    global Astatus
    Astatus = False

def AlarmPrime():
    while True:
        if GPIO.input(11) == 1:
            Aon()



GPIO.cleanup()
