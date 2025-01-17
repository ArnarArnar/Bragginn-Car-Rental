"""Repo class for Rentals"""
import csv
import os
from datetime import datetime

from Models.Rental import Rental
from Models.CarReturn import CarReturn
from Models.Insurance import Insurance

class RentalRepository:

    def __init__(self):
        self.__Rentals = [] #Hverjar eru nafnavenjurnar? afhverju eru 2 undirstrik her
        self.__Insurance = []
        self._primary_keys = []

#Post functions
    def add_rental(self, Rental):
        """Adds a rental object to the database"""
        rental_date = datetime.strftime(Rental.get_start_date(), '%d %m %Y')
        rental_end_date = datetime.strftime(Rental.get_end_date(), '%d %m %Y')
        with open(os.path.realpath('Data/Rentals.csv'), 'a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            csv_writer.writerow([Rental.get_order_id(), Rental.get_customer_id(), Rental.get_car_id(),
                                rental_date, Rental.get_days(), Rental.get_insurance(), Rental.get_total_price(), rental_end_date])

    def add_order_id(self, order_id):
        """Adds an order id to the database"""
        with open(os.path.realpath('Data/OrderIDs.csv'), 'a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            csv_writer.writerow([order_id])
    
    def add_insurance(self, Insurance):
        """Adds insurance object to the database"""
        with open(os.path.realpath('Data/Insurance.csv'), 'a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            csv_writer.writerow([Insurance.get_short_code(), Insurance.get_name(), Insurance.get_price()])

    def overwrite_rentals_list(self, rentals_list):
        """OVerwrites all rentals in the database"""
        with open(os.path.realpath('Data/Rentals.csv'), 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=';')
                for rental in rentals_list:
                    csv_writer.writerow([rental.get_order_id(), rental.get_customer_id(), rental.get_car_id(),
                                datetime.strftime(rental.get_start_date(), '%d %m %Y'), rental.get_days(), rental.get_insurance(), 
                                rental.get_total_price(), datetime.strftime(rental.get_end_date(), '%d %m %Y')])

    def add_return(self, CarReturn):
        """Adds return object to the database"""
        with open(os.path.realpath('Data/Returns.csv'), 'a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            csv_writer.writerow([CarReturn.get_order_id(), CarReturn.get_days_late(), CarReturn.get_gas_level(), CarReturn.get_return_comment(), CarReturn.get_extra_fee()])


#Get functions
    def get_rental_list(self):
        """Gets list of all rentals in the database"""
        self.__Rentals.clear()
        with open(os.path.realpath('Data/Rentals.csv')) as rentals_file:
            rentals_reader = csv.reader(rentals_file, delimiter=';')
            rentals_list = list(rentals_reader)
            for row in rentals_list:
                rental_date = datetime.date(datetime.strptime(row[3], '%d %m %Y'))
                rental_end_date = datetime.date(datetime.strptime(row[7], '%d %m %Y'))
                rental_order = Rental(row[0], row[1],  row[2], rental_date, row[4], row[5],
                                      row[6], rental_end_date)
                self.__Rentals.append(rental_order)
        return self.__Rentals
    
    def get_insurance_list(self):
        """Gets list of all insurance objects in the database"""
        self.__Insurance.clear()
        with open(os.path.realpath('Data/Insurance.csv')) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            insurance_list = list(csv_reader)
            for row in insurance_list:
                insurance_type = Insurance(row[0], row[1],  row[2])
                self.__Insurance.append(insurance_type)
        return self.__Insurance

    def get_returns_list(self):
        """Gets list of all Returns in the database"""
        Returns = []
        with open(os.path.realpath('Data/Returns.csv')) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            returns_list = list(csv_reader)
            for row in returns_list:
                return_data = CarReturn(row[0], row[1],  row[2], row[3], row[4])
                Returns.append(return_data)
        return Returns

    def get_next_order_id(self):
        """Gets the next available order id from the database"""
        with open(os.path.realpath('Data/OrderIDs.csv')) as order_id_file:
            order_id_reader = csv.reader(order_id_file, delimiter=';')
            id_list = list(order_id_reader)
            next_id = int(id_list[-1][0]) + 1
        return next_id

    def get_rentals_primary_keys(self):
        """Gets the primary keys of the rentals table"""
        self._primary_keys.clear()
        with open(os.path.realpath('Data/Rentals.csv')) as customer_file:
            csv_reader = csv.reader(customer_file, delimiter=';')
            customer_list = list(csv_reader)
            for row in customer_list:
                self._primary_keys.append(row[0])
        return self._primary_keys

    def get_returns_primary_keys(self):
        """Gets the primary keys of the returns table"""
        self._primary_keys.clear()
        with open(os.path.realpath('Data/Returns.csv')) as customer_file:
            csv_reader = csv.reader(customer_file, delimiter=';')
            returns_list = list(csv_reader)
            for row in returns_list:
                self._primary_keys.append(row[0])
        return self._primary_keys

    def get_insurance_primary_keys(self):
        """Gets the primary keys of the insurance table"""
        self._primary_keys.clear()
        with open(os.path.realpath('Data/Insurance.csv')) as customer_file:
            csv_reader = csv.reader(customer_file, delimiter=';')
            customer_list = list(csv_reader)
            for row in customer_list:
                self._primary_keys.append(row[0])
        return self._primary_keys
