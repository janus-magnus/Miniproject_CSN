import RPi.GPIO as GPIO
import time


def init():
    GPIO.setmode(GPIO.BOARD)  # pin setups
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # button1 input GPIO
    GPIO.setup(12, GPIO.OUT)  # LED Powersource(staat gelijk aan 3.3V out)

status = ''

#aanpasbaare blink time/ nu nog hardcoded

global LED_off_time
LED_off_time = 2.0
global LED_on_time
LED_on_time = 2.0


def a_faster():  # Make the LED blink faster
    global LED_off_time
    global LED_on_time
    LED_on_time -= 0.5
    LED_off_time -= 0.5
    print(LED_on_time)


def a_slower():  # Make the LED blink slower
    global LED_off_time
    global LED_on_time
    LED_off_time += 0.5
    LED_on_time += 0.5
    print(LED_on_time)


def a_on():  # Turn on LED
        GPIO.output(12, 1)
        time.sleep(LED_on_time)
        GPIO.output(12, 0)
        time.sleep(LED_off_time)


def a_off():  # deactives alarm
    global status
    status = 'exit'


def alarm_prime():  # wacht op button press een roept dan Aon() in een loop
    global status
    while True:
        if GPIO.input(11) == 1:
            status = 'on'
        if status == 'on':
            a_on()
        if status == 'exit':
            status = ''
            break


GPIO.cleanup()