from tkinter import *
import RPi.GPIO as GPIO
import time

# Dit is de combinatie file

GPIO.setmode(GPIO.BOARD)#pin setups
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#button1 input GPIO
GPIO.setup(12, GPIO.OUT)#LED Powersource(Als output aan staat is het 3.3V zelfde als pin 1 de standaard powerpin)
GPIO.setup(37, GPIO.OUT)#button2 output GPIO
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(37, 1)#set pin 37 aan zodat hij als 3.3V output werkt

#aanpasbaare blink time/ nu nog hardcoded
LED_off_time = 2
LED_on_time = 2

def Aon(): #Turn on LED
    while True:
            if GPIO.input(36):#button2 moet ingedrukt blijven worden tot hij stopt
                break
            GPIO.output(12, 1)
            time.sleep(LED_on_time)
            GPIO.output(12, 0)
            time.sleep(LED_off_time)

def Aoff():
    GPIO.output(12, 1)


def Afaster(): #Make the LED blink faster
	LED_on_time-=1
	LED_off_time-=1

def Aslower(): #Make the LED blink slower
	LED_off_time+=1
	LED_on_time+=1

while True:
    if GPIO.input(11) == 1:
        Aon()

class MainFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.Bfaster = Button(self, text='Sneller', command=Afaster())
        self.Bslower = Button(self, text='langzaamer',command=Aslower())
        self.Bdisable = Button(self, text='Alarm Deactivereen', command=Aoff())

        self.Bfaster.grid(row=0, sticky=E)
        self.Bslower.grid(row=1, sticky=E)
        self.Bdisable.grid(row=2, column=0)



        self.pack()

root = Tk()
mf = MainFrame(root)
root.mainloop()
GPIO.cleanup()