from Tkinter import *
#import Alarm
from Main import Alarm # de bovenstaande import is voor op de pi, werkt anders daar

class MainFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        Alarm.Init

        self.Bfaster = Button(self, text='Sneller', command=Alarm.Afaster())
        self.Bslower = Button(self, text='langzaamer',command=Alarm.Aslower())
        self.Bprime = Button(self, text='Alarm Activeren', command=Alarm.AlarmPrime)
        self.Bdisable = Button(self, text='Alarm Deactivereen', command=Alarm.Aoff())

        self.Bfaster.grid(row=0, sticky=E)
        self.Bslower.grid(row=1, sticky=E)
        self.Bdisable.grid(row=2, column=0)
        self.Bprime.grid(row=3, column=0)



        self.pack()


root = Tk()
mf = MainFrame(master=root)
mf.mainloop()