from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# from new.connection import *
from PIL import Image
# import image
from choose import *
import tkinter as tk
from connection import MyDb


class Register:
    def __init__(self):
        self.reg()
        # self.mainsc()
        self.choose = Choose()
        self.database = MyDb()

    def reg(self):
        try:
            self.window = Tk()
            self.window.title('register for login')
            self.window.geometry('1000x500')
            self.window.configure(bg='darkorange1')

            # img_register = PhotoImage.open("bibhuti & santosh (12).JPG")
            # resized = img_register.resize((500, 500), Image.ANTIALIAS)
            # new_pic = PhotoImage(resized)
            # register_label = Label(self.window, image=new_pic)
            # register_label.place(x=1, y=1)

            self.lblc1 = Label(self.window, bg='darkorange2', width=20, height=5, font=('Ariel', 15, 'bold'))
            self.lblc1.place(x=745, y=90)

            self.lblc2 = Label(self.window, bg='darkorange2', width=23, height=14, font=('Ariel', 15, 'bold'))
            self.lblc2.place(x=5, y=60)

            self.lbl9 = Label(self.window, text=' Kathmandu Delux Volvo  A/c Bus Service ', fg='black', bg='darkorange1',font=('Century', 25,'bold'))
            self.lbl9.place(x=200, y=10)

            self.lbl = Label(self.window, text='Enter first name' , fg='black', bg='darkorange2', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=27, y=70)
            self.ent_name = Entry(self.window, bg='silver')
            self.ent_name.place(x=155, y=75)
            self.lbl = Label(self.window, text='Enter last name', fg='black', bg='darkorange2', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=120)
            self.ent_ls = Entry(self.window, bg='silver')
            self.ent_ls.place(x=155, y=125)
            self.lbl = Label(self.window, text='username', fg='black', bg='darkorange2', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=170)
            self.ent_un = Entry(self.window, bg='silver')
            self.ent_un.place(x=155, y=175)
            self.lbl = Label(self.window, text='password', fg='black', bg='darkorange2', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=320)
            self.ent_ps = Entry(self.window, bg='silver')
            self.ent_ps.place(x=155, y=325)
            self.lbl = Label(self.window, text='phone number', fg='black', bg='darkorange2', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=220)
            self.ent_pn = Entry(self.window, bg='silver')
            self.ent_pn.place(x=155, y=225)
            self.lbl = Label(self.window, text='address', fg='black', bg='darkorange2', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=270)
            self.ent_ad = Entry(self.window, bg='silver')
            self.ent_ad.place(x=155, y=275)
            self.registernow_but = Button(self.window, text="REGISTER NOW", command=self.getting, bg='darkorange3', font=('Century',"9", 'bold'))
            self.registernow_but.place(x=155, y=360)

            self.username = Label(self.window, text=' username', fg='black', bg='darkorange2', font=('Cambria', 13, 'bold'))
            self.username.place(x=750, y=97)

            self.un_ent = Entry(self.window, bg='silver')
            self.un_ent.place(x=850, y=100)

            self.password = Label(self.window, text=' password', fg='black', bg='darkorange2', font=('Cambria', 13, 'bold'))
            self.password.place(x=750, y=130)

            self.ps_ent = Entry(self.window, show='*', bg='silver')
            self.ps_ent.place(x=850, y=130)

            self.loginhere_but = Button(self.window, text="LOGIN HERE", command=self.login_backend, bg='darkorange3', font=('Century', 7, 'bold'), )
            self.loginhere_but.place(x=880, y=170)

            self.window.mainloop()
        except Exception as e:
            print(e)

    def getting(self):
        try:
            self.database = MyDb()
            first_name = self.ent_name.get()
            last_name = self.ent_ls.get()
            username = self.ent_un.get()
            password = self.ent_ps.get()
            phone = self.ent_pn.get()
            address = self.ent_ad.get()
            if first_name == '' or last_name == '' or username == '' or password == '' or phone == '' or address == '':
                 messagebox.showerror('Error', ' Enter each boxes carefully!')
                # return False
            else:
                qry ='''insert into registration (username,password,firstname,lastname,address,phone) values(%s,%s,%s,%s,%s,%s)'''
                values = (username, password, first_name, last_name, address, phone)
                self.database.iud(qry, values)
                messagebox.showinfo('Done', ' Registered successfully!')
                # return True
        except Exception as e:
            print(e)
            # return False


    # def login(self):
    #     try:
    #         self.window1 = Tk()
    #         self.window1.title(' login')
    #         self.window1.geometry('700x400')
    #         self.window1.configure(bg='navy')
    #
    #         self.lbl = Label(self.window1, text='Kathmandu Delux Volvo  A/c Bus Service ', fg='red', bg='white',font=('Bradley Hand ITC', 18, 'bold'))
    #         self.lbl.place(x=120, y=10)
    #
    #
    #         self.username = Label(self.window1, text=' username', fg='silver', bg='navy', font=('Cambria', 13, 'bold'))
    #         self.username.place(x=230, y=97)
    #
    #         self.un_ent = Entry(self.window1, bg='silver')
    #         self.un_ent.place(x=330, y=100)
    #
    #         self.password = Label(self.window1, text=' password',  fg='silver', bg='navy', font=('Cambria', 13, 'bold'))
    #         self.password.place(x=230, y=130)
    #
    #         self.ps_ent = Entry(self.window1, show='*', bg='silver')
    #         self.ps_ent.place(x=330, y=130)
    #
    #         self.loginhere_but = Button(self.window1, text="LOGIN HERE", command=self.login_backend, bg='grey', font=('Century', 7, 'bold'),)
    #         self.loginhere_but.place(x=370, y=170)
    #         self.window1.mainloop()
    #     except Exception as e:
    #         print(e)


    def login_backend(self):
        try:
            self.database = MyDb()
            self.choose = Choose()
            userna = self.un_ent.get()
            passw = self.ps_ent.get()

            if userna == '' or passw == '':
                messagebox.showerror("error", "enter username or password first!")
            else:
                qry = '''select * from registration where username=%s and password=%s'''
                values = (userna, passw)
                user = self.database.get_data_p(qry, values)

            if len(user) == 1:
                messagebox.showinfo("Bomm", "Login successfull")
                self.choose.window3()
                # return True
            else:
                messagebox.showerror("Error", "Wrong password or username")
                # return False

        except Exception as e:
            print(e)
            # return False
#
#     def mainsc(self):
#         try:
#             self.window2 = Tk()
#             self.window2.title('sewa')
#             self.window2.geometry('700x400')
#             self.window2.configure(bg='navy')
#
#             self.lbl = Label(self.window2, text='Kathmandu Delux Volvo  A/c Bus Service ', fg='red', bg='white', font=('Bradley Hand ITC', 18, 'bold'))
#             self.lbl.place(x=120, y=10)
#
#             self.login_but = Button(self.window2, text="LOGIN", command=self.login, bg="grey", font=('Century', 10, 'bold'))
#             self.login_but.place(x=300, y=80)
#             self.register_but = Button(self.window2, text="REGISTER", command=self.reg, bg='grey', font=('Century', 11, 'bold'), )
#             self.register_but.place(x=280, y=125)
#             self.window2.mainloop()
#         except Exception as e:
#             print(e)
#
Register()


