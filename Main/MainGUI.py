from Tkinter import *
import Alarm
import threading

class MainFrame(Frame):

    def primeThread(self):

        thread = threading.Thread(target=Alarm.AlarmPrime())
        thread.deamon = True
        thread.start()

    def __init__(self, master=None):
        Frame.__init__(self, master)


        Alarm.Init()

        self.Bfaster = Button(self, text='Sneller', command=lambda: Alarm.Afaster())
        self.Bslower = Button(self, text='langzaamer',command=lambda: Alarm.Aslower())
        self.Bprime = Button(self, text='Alarm Activeren', command=lambda: self.primeThread())
        self.Bdisable = Button(self, text='Alarm Deactivereen', command=lambda: Alarm.Aoff())

        self.Bfaster.grid(row=0, sticky=E)
        self.Bslower.grid(row=1, sticky=E)
        self.Bdisable.grid(row=2, column=0)
        self.Bprime.grid(row=3, column=0)



        self.pack()


root = Tk()
mf = MainFrame(master=root)
mf.mainloop()