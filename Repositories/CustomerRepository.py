"""Repo class for Customers"""
import csv
from Models.Customer import Customer

class CustomerRepository:

    def __init__(self):
        self.__Customers = [] #Hverjar eru nafnavenjurnar? afhverju eru 2 undirstrik her
        self._primary_keys = []

#Post functions
    def add_customer(self, Customer):
        with open('Data/Customers.csv', 'a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            csv_writer.writerow([Customer._customer_id, Customer._first_name, Customer._last_name, #Nota get foll her i stadinn
                                Customer._phone, Customer._street, Customer._zip, Customer._town, 
                                Customer._country, Customer._drivers_license])


    def add_credit_card(self, CreditCard):
        with open('Data/CreditCards.csv', 'a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            csv_writer.writerow([CreditCard._customer_id, CreditCard._card_number, CreditCard._expiry, CreditCard._cvc])

#Get functions
    def get_customer_list(self):
        with open('Data/Customers.csv') as customer_file:
            csv_reader = csv.reader(customer_file, delimiter=';')
            customer_list = list(csv_reader)
            for row in customer_list:
                db_customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                self.__Customers.append(db_customer)
        return self.__Customers

    def get_primary_key(self):
        with open('Data/Customers.csv') as customer_file:
            csv_reader = csv.reader(customer_file, delimiter=';')
            customer_list = list(csv_reader)
            for row in customer_list:
                self._primary_keys.append(row[0])
        return self._primary_keys
        