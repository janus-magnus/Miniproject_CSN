from Tkinter import *
import tkMessageBox as tm
import RPi.GPIO as GPIO
import MainGUI


GPIO.setmode(GPIO.BOARD)  # pin setups
GPIO.setup(37, GPIO.OUT)  # button2 output GPIO
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # button2 input
GPIO.output(37, 1)  # set pin 37 aan zodat hij als 3.3V output werkt


class loginFrame(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.label_1 = Label(self, text="Username")
        self.label_2 = Label(self, text="Password")
        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self.login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def login_btn_clickked(self):
            username = self.entry_1.get()
            password = self.entry_2.get()

            if username == "john" and password == "password":
                root.destroy()  # sluit huidig venster
                MainGUI.new_frame()  # opent nieuw MainGUI venster
                #tm.showinfo("Login info", "Welcome John")
            else:
                tm.showerror("Login error", "Incorrect username")

while True:  # wacht op een button press en opent dan een nieuw loginGUI
    if GPIO.input(36) == 1:
        root = Tk()
        lf = loginFrame(master=root)
        lf.mainloop()
        break
