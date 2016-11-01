from tkinter import *
from Main import Alarm



class MainFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.Bfaster = Button(self, text='Sneller', command=Alarm.Afaster())
        self.Bslower = Button(self, text='langzaamer',command=Alarm.Aslower())
        self.Bdisable = Button(self, text='Alarm Deactivereen', command=Alarm.Aoff())

        self.Bfaster.grid(row=0, sticky=E)
        self.Bslower.grid(row=1, sticky=E)
        self.Bdisable.grid(row=2, column=0)



        self.pack()


root = Tk()
mf = MainFrame(root)
root.mainloop()
