from Tkinter import *
import Alarm
import threading


class MainFrame(Frame):

    def prime_thread(self):  # start een thread voor alarmPrime

        thread = threading.Thread(target=Alarm.alarm_prime)
        thread.deamon = True
        thread.start()

    def __init__(self, master=None):
        Frame.__init__(self, master)

        Alarm.init()

        self.Bfaster = Button(self, text='Sneller', command=lambda: Alarm.a_faster())
        self.Bslower = Button(self, text='langzaamer', command=lambda: Alarm.a_slower())
        self.Bprime = Button(self, text='Alarm Activeren', command=lambda: self.prime_thread())
        self.Bdisable = Button(self, text='Alarm Deactivereen', command=lambda: Alarm.a_off())

        self.Bfaster.grid(row=0, sticky=E)
        self.Bslower.grid(row=1, sticky=E)
        self.Bdisable.grid(row=2, column=0)
        self.Bprime.grid(row=3, column=0)

        self.pack()


def new_frame():  # maakt een nieuwe venster aan

    root = Tk()
    mf = MainFrame(master=root)
    mf.mainloop()