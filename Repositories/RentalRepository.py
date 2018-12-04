"""Repo class for Rentals"""
import csv
from datetime import datetime

from Models.Rental import Rental

class RentalRepository:

    def __init__(self):
        self.__Rentals = [] #Hverjar eru nafnavenjurnar? afhverju eru 2 undirstrik her
        self._primary_keys = []

#Post functions
    def add_rental(self, Rental):
        rental_date = datetime.strftime(Rental._start_date, '%d %m %Y')
        with open('Data/Rentals.csv', 'a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            csv_writer.writerow([self.get_next_order_id(), Rental._customer_id, Rental._car_id, rental_date, Rental._length, Rental._total_price])

    def add_order_id(self, order_id):
        with open('Data/OrderIDs.csv', 'a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            csv_writer.writerow([order_id])

#Get functions
    def get_rental_list(self):
        with open('Data/Rentals.csv') as rentals_file:
            rentals_reader = csv.reader(rentals_file, delimiter=';')
            rentals_list = list(rentals_reader)
            for row in rentals_list:
                rental_date = datetime.date(datetime.strptime(row[3], '%d %m %Y'))
                rental_order = Rental(row[0], row[1],  row[2], rental_date, row[4], row[5])
                self.__Rentals.append(rental_order)
        return self.__Rentals

    def get_next_order_id(self):
        with open('Data/OrderIDs.csv') as order_id_file:
            order_id_reader = csv.reader(order_id_file, delimiter=';')
            id_list = list(order_id_reader)
            next_id = int(id_list[-1][0]) + 1
        return next_id

    def get_primary_key(self):
        with open('Data/Rentals.csv') as customer_file:
            csv_reader = csv.reader(customer_file, delimiter=';')
            customer_list = list(csv_reader)
            for row in customer_list:
                self._primary_keys.append(row[0])
        return self._primary_keys