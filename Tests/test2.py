import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)# set de modes van pin nummering

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#dit zet pin 11 op als input met een interne pulldown circuit

GPIO.setup(12, GPIO.OUT)# dit zet pin 12 als output, hier zit de LED op
GPIO.output(12, 0)

try:
    while True:
        GPIO.output(12, GPIO.input(11))#LED gaat aan als de knop in gedrukt wordt

except KeyboardInterrupt:
    GPIO.cleanup()