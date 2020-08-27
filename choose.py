from tkinter import *
from addbus import *
from passengerbooking import *

from tkinter import ttk

class Choose:

    def __init__(self):

        self.register = Addbus()
        self.passenger = Booking()

    def window3(self):
        try:
            self.register = Addbus()
            self.passenger = Booking()

            self.window3=Tk()
            self.window3.title('booking')
            self.window3.geometry('1000x500')
            self.window3.configure(bg='darkorange1')

            self.lblc1passenger = Label(self.window3, bg='darkorange2', width=75, height=3, font=('Ariel', 10, 'bold'))
            self.lblc1passenger.place(x=0, y=185)

            self.lblc1 = Label(self.window3, bg='darkorange2', width=80, height=3, font=('Ariel', 10, 'bold'))
            self.lblc1.place(x=400, y=120)

            self.lbl9 = Label(self.window3, text='WELCOME TO KATHMANDU DELUX', fg='black', bg='darkorange1', font=('Century', '25', 'bold'))
            self.lbl9.place(x=180, y=10)

            self.reg_but = Button(self.window3, text= "BUS REGISTER ", command=self.register.busadd, bg='darkorange3',font=('Century','10', 'bold'))
            self.reg_but.place(x=425, y=130)

            self.pass_but = Button(self.window3, text="PASSENGER BOOKING", command=self.passenger.booking, bg='darkorange3', font=('Century', '10', 'bold'))
            self.pass_but.place(x=400, y=200)

            self.window3.mainloop()
        except Exception as e:
            print(e)
