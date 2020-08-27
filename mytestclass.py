
from main_page import *
from addbus import *
from passengerbooking import *
import unittest


class Testing(unittest.TestCase):


    def test_login(self):
        login = Register()
        result = login.login_backend('harsh', '0123')
        self.assertTrue(result)

    def test_login1(self):
        login = Register()
        result = login.login_backend('harsh', '2222')
        self.assertFalse(result)


    def test_register(self):
        reg = Register()
        result = reg.getting(username='1111', password='1111', first_name='gajab', last_name='bhushan', address='mars', phone='988644334')
        self.assertTrue(result)

    def test_register1(self):
        reg = Register()
        result = reg.getting(username='', password='1111', first_name='gajab', last_name='bhushan', address='mars',  phone='988644334')
        self.assertFalse(result)

    def test_addbus(self):
        add = Addbus()
        result = add.add_bus(bus_number='5555', bus_company='shankar', driver_name='bipin', driver_contact='9854323566', total_seat='40', route='janakpur to kathmandu', dep_time='1:00')
        self.assertTrue(result)

    def test_addbus1(self):
        add = Addbus()
        result = add.add_bus(bus_number='', bus_company='shankar', driver_name='bipin', driver_contact='9854323566', total_seat='40', route='janakpur to kathmandu', dep_time='1:00')
        self.assertFalse(result)

    def test_delete(self):
        add = Addbus()
        id = str(1)
        result = add.delete_bus(id)
        self.assertEqual(result, True)

    def test_delete1(self):
        add = Addbus()
        result = add.delete_bus('')
        self.assertTrue(result)

    def test_delete2(self):
        add = Addbus()
        id = str(1)
        result = add.delete_bus(id)
        self.assertTrue(result)

    def test_update(self):
        add = Addbus()
        id = int(1)
        result = add.update_bus(id, 'dd', 'fg', 'rr', 'ee', 'tt', 'yy', 'yo')
        self.assertTrue(result)


    def test_store(self):
        keep = Booking()
        result = keep.store(Bus_company='robert', Bus_Number='9999', Name='bipin', no_of_passenger='80', Date='20/2/2020', Dep_Time='9:00', From_='maahendranagar', To_='kathmandu', Fare_rs='600')
        self.assertTrue(result)

    def test_store1(self):
        keep = Booking()
        result = keep.store(Bus_company='', Bus_Number='9999', Name='bipin', no_of_passenger='80', Date='20/2/2020', Dep_Time='9:00', From_='maahendranagar', To_='kathmandu', Fare_rs='600')
        self.assertFalse(result)