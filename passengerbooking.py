from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from datetime import *
#from generatebill import *
from connection import MyDb


class Booking:

    def __init__(self):
        self.booking()
        self.database = MyDb()

    def booking(self):
        try:
            self.window7 = Tk()
            self.window7.title('ticket booking')
            self.window7.geometry('1400x800')
            self.window7.configure(bg='darkorange1')

            self.lblc1big = Label(self.window7, bg='darkorange2', width=32, height=15, font=('Ariel', 15, 'bold'))
            self.lblc1big.place(x=5, y=190)

            self.lblc1search = Label(self.window7, bg='darkorange2', width=32, height=3, font=('Ariel', 15, 'bold'))
            self.lblc1search.place(x=5, y=80)

            self.lblc1ticket = Label(self.window7, bg='darkorange2', width=80, height=2, font=('Ariel', 15, 'bold'))
            self.lblc1ticket.place(x=450, y=500)

            self.lbl9 = Label(self.window7, text='SEARCHING BUS', fg='black', bg='darkorange1', font=('Century', 25, 'bold'))
            self.lbl9.place(x=500, y=1)

            self.lbl = Label(self.window7, text="SEARCH BUS BY:", fg='black', bg='darkorange2', font=('Cambria', 16, 'bold'))
            self.lbl.place(x=30, y=85)

            self.cat5 = ttk.Combobox(self.window7)
            self.cat5.set('--choose --')
            self.cat5['values'] = ('Bus Company', 'Route', ' Departure Time')  # self.combo()
            self.cat5.place(x=240, y=85)

            self.select2_but = Button(self.window7, text="SELECT", command=self.sort, bg='darkorange3', font=('Century', '10', 'bold'))
            self.select2_but.place(x=420, y=85)

            self.lbl = Label(self.window7, text='keyword', fg='black', bg='darkorange2', font=('Cambria', 16, 'bold'))
            self.lbl.place(x=30, y=115)

            self.placen_ent = Entry(self.window7, bg='silver')
            self.placen_ent.place(x=240, y=115)

            self.search1_but = Button(self.window7, text="BUS SEARCH",  bg='darkorange3', font=('Century', '10', 'bold'))
            self.search1_but.place(x=420, y=115)


            self.lbl= Label(self.window7, text='Bus Number', fg='black', bg='darkorange2', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=200)

            self.ent_bnum = Entry(self.window7, bg='silver')
            self.ent_bnum.place(x=240, y=200)

            self.lbl = Label(self.window7, text='Bus Company', fg='black', bg='darkorange2', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=250)

            self.bcom_ent = Entry(self.window7, bg='silver')
            self.bcom_ent.place(x=240, y=250)

            self.lbl = Label(self.window7, text='Driver Name', fg='black', bg='darkorange2', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=300)

            self.dnam_ent = Entry(self.window7, bg='silver')
            self.dnam_ent.place(x=240, y=300)

            self.lbl = Label(self.window7, text='Driver Contact',fg='black', bg='darkorange2', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=350)

            self.dcom_ent = Entry(self.window7, bg='silver')
            self.dcom_ent.place(x=240, y=350)

            self.lbl = Label(self.window7, text='Total Seat',fg='black', bg='darkorange2', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=400)

            self.tseat_ent = Entry(self.window7, bg='silver')
            self.tseat_ent.place(x=240, y=400)

            self.lbl = Label(self.window7, text='Route',fg='black', bg='darkorange2', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=450)

            self.rou_ent = Entry(self.window7, bg='silver')
            self.rou_ent.place(x=240, y=450)

            self.lbl = Label(self.window7, text=' Departure Time', fg='black', bg='darkorange2', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=20, y=500)

            self.dtim_ent = Entry(self.window7, bg='silver')
            self.dtim_ent.place(x=240, y=500)

            self.add_tree = ttk.Treeview(self.window7, height=15,column=('n', 'w', 'p', 'm', 'c', 'g', 'h'))
            self.add_tree.place(x=550, y=80)
            self.add_tree['show'] = 'headings'
            self.add_tree.column('n', width=100)
            self.add_tree.column('w', width=100)
            self.add_tree.column('p', width=100)
            self.add_tree.column('m', width=100)
            self.add_tree.column('c', width=100)
            self.add_tree.column('g', width=100)
            self.add_tree.column('h', width=100)
            self.add_tree.heading('n', text='Bus number')
            self.add_tree.heading('w', text='Bus Company')
            self.add_tree.heading('p', text='Driver Name')
            self.add_tree.heading('m', text='Driver Contact')
            self.add_tree.heading('c', text='Total Seat')
            self.add_tree.heading('g', text='Route')
            self.add_tree.heading('h', text='Departure Time')
        except Exception as e:
            print(e)


    def sort(self):
        try:
            search_bus_by = self.cat5.get()
            if search_bus_by == 'Bus Company':
                self.search1_but = Button(self.window7, text="BUS SEARCH", command=self.search_by_company, bg='darkorange3', font=('Century', '10', 'bold'))
                self.search1_but.place(x=420, y=115)

            elif search_bus_by == 'Route':
                self.search1_but = Button(self.window7, text="BUS SEARCH", command=self.search_by_route, bg='darkorange3', font=('Century', '10', 'bold'))
                self.search1_but.place(x=420, y=115)
            else:
                self.search1_but = Button(self.window7, text="BUS SEARCH", command=self.search_by_time, bg='darkorange3', font=('Century', '10', 'bold'))
                self.search1_but.place(x=420, y=115)
        except Exception as e:
            print(e)

    def by_company(self,keyword):
        try:
            self.database = MyDb()
            qry = "SELECT * FROM bus_register WHERE bus_company LIKE '" + keyword + "%'"
            result = self.database.get_data(qry)
            return result
        except Exception as e:
            print(e)

    def search_by_company(self):
        try:
            sea1 = self.placen_ent.get()
            all_result =self.by_company(sea1)
            self.add_tree.delete(*self.add_tree.get_children())
            for i in all_result:
                self.add_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
            self.add_tree.bind("<Double-1>", self.select_item)

            self.generatebill_but = Button(self.window7, text="GENERATE TICKET", command=self.bill, bg='darkorange3', font=('Century', '10', 'bold'))
            self.generatebill_but.place(x=480, y=510)



        except Exception as e:
            print(e)

    def by_route(self,keyword):
        try:
            self.database = MyDb()
            qry = "SELECT * FROM bus_register WHERE route LIKE '" + keyword + "%'"
            result=self.database.get_data(qry)
            return result
        except Exception as e:
            print(e)

    def search_by_route(self):
        try:
            sea1 = self.placen_ent.get()
            all_result =self.by_route(sea1)
            self.add_tree.delete(*self.add_tree.get_children())
            for i in all_result:
                self.add_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
            self.add_tree.bind("<Double-1>", self.select_item)

            self.generatebill_but = Button(self.window7, text="GENERATE TICKET", command=self.bill,  bg='darkorange3', font=('Century', '10', 'bold'))
            self.generatebill_but.place(x=480, y=510)
        except Exception as e:
            print(e)
    def by_time(self, keyword):
        try:
            self.database = MyDb()
            qry = "SELECT * FROM bus_register WHERE dep_time LIKE '" + keyword + "%'"
            result=self.database.get_data(qry)
            return result
        except Exception as e:
            print(e)

    def search_by_time(self):
        try:
            sea1 = self.placen_ent.get()
            all_result = self.by_time(sea1)
            self.add_tree.delete(*self.add_tree.get_children())
            for i in all_result:
                self.add_tree.insert('', 'end', text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
            self.add_tree.bind("<Double-1>", self.select_item)

            self.generatebill_but = Button(self.window7, text="GENERATE TICKET", command=self.bill,  bg='darkorange3', font=('Century', '10', 'bold'))
            self.generatebill_but.place(x=480, y=510)
        except Exception as e:
            print(e)
    def select_item(self, event):
        try:
            sel_row = self.add_tree.selection()[0]
            sel_item = self.add_tree.item(sel_row)
            self.update_index = self.add_tree.item(sel_row, 'text')
            selected_data = self.add_tree.item(sel_row, 'values')
            self.ent_bnum.delete(0, 'end')
            self.ent_bnum.insert(0, selected_data[0])
            self.bcom_ent.delete(0, 'end')
            self.bcom_ent.insert(0, selected_data[1])
            self.dnam_ent.delete(0, 'end')
            self.dnam_ent.insert(0, selected_data[2])
            self.dcom_ent.delete(0, 'end')
            self.dcom_ent.insert(0, selected_data[4])
            self.tseat_ent.delete(0, 'end')
            self.tseat_ent.insert(0, selected_data[3])
            self.rou_ent.delete(0, 'end')
            self.rou_ent.insert(0, selected_data[5])
            self.dtim_ent.delete(0, 'end')
            self.dtim_ent.insert(0, selected_data[6])
        except Exception as e:
            print(e)

    def bill(self):
        try:
            self.window6 = Tk()
            self.window6.title('generate ticket')
            self.window6.geometry('700x400')
            self.window6.configure(bg='wheat1')


            self.lbl9 = Label(self.window6, text='Kathmandu Delux Volvo  A/c Bus Service', fg='black', bg='wheat2', font=('Century', 25, 'bold'))
            self.lbl9.place(x=15, y=00)

            # self.lblc1delux = Label(self.window6, bg='wheat2', width=70, height=2, font=('Ariel', 15, 'bold'))
            # self.lblc1delux.place(x=0, y=00)

            self.lblc1booking = Label(self.window6, bg='wheat3', width=100, height=2, font=('Ariel', 10, 'bold'))
            self.lblc1booking.place(x=00, y=60)

            self.lbl9 = Label(self.window6, text='Ticket Booking', fg='black', bg='wheat3', font=('Constantia', 15, 'bold'))
            self.lbl9.place(x=240, y=60)


            self.lbl10 = Label(self.window6, text='free wifi ', fg='pink', bg='navy', font=('Constantia', 15, 'bold'))
            self.lbl10.place(x=50, y=100)

            self.lbl = Label(self.window6, text="Bus company", fg='silver', bg='navy', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=180)

            self.bcomm_ent = Entry(self.window6, bg='silver')
            self.bcomm_ent.place(x=155, y=180)

            self.lbl = Label(self.window6, text="Bus Number", fg='silver', bg='navy', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=200)

            self.ent_dop = Entry(self.window6, bg='silver')
            self.ent_dop.place(x=155, y=200,)

            self.lbl = Label(self.window6, text="Date ", fg='silver', bg='navy', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=280, y=150)

            self.ent_d = Entry(self.window6, bg='silver')
            self.ent_d.place(x=330, y=150)
            today = date.today()
            self.ent_d.insert(0,today)

            self.lbl = Label(self.window6, text='Dep_Time',fg='silver', bg='navy', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=480, y=150)

            self.ti_ent = Entry(self.window6, bg='silver')
            self.ti_ent.place(x=570, y=150)

            self.lbl = Label(self.window6, text='Name', fg='silver', bg='navy', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=220)

            self.na_ent = Entry(self.window6, bg='silver')
            self.na_ent.place(x=155, y=220)

            self.lbl = Label(self.window6, text='No.of passenger', fg='silver', bg='navy', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=240)

            self.no_ent = Entry(self.window6, bg='silver')
            self.no_ent.place(x=155, y=240)

            self.lbl = Label(self.window6, text='From.',fg='silver', bg='navy', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=260)

            self.from_ent = Entry(self.window6, bg='silver')
            self.from_ent.place(x=155, y=260)

            self.lbl = Label(self.window6, text='To', fg='silver', bg='navy', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=280)

            self.to_ent = Entry(self.window6, bg='silver')
            self.to_ent.place(x=155, y=280)

            self.lbl = Label(self.window6, text='Fare rs.', fg='silver', bg='navy', font=('Cambria', 12, 'bold'))
            self.lbl.place(x=30, y=300)

            self.rr_ent = Entry(self.window6, bg='silver')
            self.rr_ent.place(x=155, y=300)

            self.generatebill_but = Button(self.window6, text="Store", command=self.store,  bg='grey', font=('Century', '10', 'bold'))
            self.generatebill_but.place(x=500, y=350)
            busnumber = self.ent_bnum.get()
            buscompany = self.bcom_ent.get()
            deptime = self.dtim_ent.get()
            self.bcomm_ent.insert(0, buscompany)
            self.ent_dop.insert(0, busnumber)
            self.ti_ent.insert(0, deptime)

            self.window6.mainloop()
        except Exception as e:
            print(e)

    def store(self, Bus_company,Bus_Number,Name, no_of_passenger, Date, Dep_Time, From_, To_, Fare_rs):
        try:
            # self.database = MyDb()
            # Bus_company=self.bcom_ent.get()
            # Bus_Number =self.ent_dop.get()
            # Date = self.ent_d.get()
            # Dep_Time = self.ti_ent.get()
            # Name = self.na_ent.get()
            # no_of_passenger =self.no_ent.get()
            # From_ = self.from_ent.get()
            # To_ = self.to_ent.get()
            # Fare_rs = self.rr_ent.get()
            if Bus_company == '' or Bus_Number == '' or Date == '' or Dep_Time == '' or Name == '' or no_of_passenger == '' or From_ == '' or To_ == '' or Fare_rs == '':
                # messagebox.showerror('Error', ' Enter each boxes carefully!')
               return False
            else:
                qry = '''insert into ticket_booking (Bus_company,Bus_Number,Name, no_of_passenger,Date,Dep_Time,From_,To_,Fare_rs) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                values = (Bus_company,Bus_Number,Name, no_of_passenger, Date, Dep_Time, From_, To_, Fare_rs)
                self.database.iud(qry, values)
                # messagebox.showinfo('Done', ' stored successfully!')
                return True
        except Exception as e:
            print(e)
            return False

Booking()


