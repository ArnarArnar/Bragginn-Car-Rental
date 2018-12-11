"""Repo class for Customers"""
import csv
import os

from Models.Customer import Customer
from Models.CreditCard import CreditCard

class CustomerRepository:

    def __init__(self):
        self.__Customers = [] #Hverjar eru nafnavenjurnar? afhverju eru 2 undirstrik her
        self.__CreditCards = []
        self._primary_keys = []

#Post functions
    def add_customer(self, Customer):
        with open(os.path.realpath('Data/Customers.csv'), 'a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            csv_writer.writerow([Customer.get_customer_id, Customer.get_first_name, Customer.get_last_name, #Nota get foll her i stadinn
                                Customer.get_phone, Customer.get_street, Customer.get_zip, Customer.get_town, 
                                Customer.get_country, Customer.get_drivers_license])

    def overwrite_customer_list(self, customer_list):
        with open(os.path.realpath('Data/Customers.csv'), 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=';')
                for customer in customer_list:
                    csv_writer.writerow([customer.get_customer_id, customer.get_first_name, customer.get_last_name,
                                        customer.get_phone, customer.get_street, customer.get_zip, customer.get_town, 
                                        customer.get_country, customer.get_drivers_license])

    def add_credit_card(self, CreditCard):
        with open(os.path.realpath('Data/CreditCards.csv'), 'a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            csv_writer.writerow([CreditCard.get_customer_id, CreditCard.get_card_number,
                                CreditCard.get_expiry, CreditCard.get_cvc])
    
    def overwrite_credit_card_list(self, credit_card_list):
        with open(os.path.realpath('Data/CreditCards.csv'), 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=';')
                for credit_card in credit_card_list:
                    csv_writer.writerow([credit_card.get_customer_id, credit_card.get_card_number,
                                        credit_card.get_expiry, credit_card.get_cvc])

#Get functions
    def get_customer_list(self):
        self.__Customers.clear()
        with open(os.path.realpath('Data/Customers.csv')) as customer_file:
            csv_reader = csv.reader(customer_file, delimiter=';')
            customer_list = list(csv_reader)
            for row in customer_list:
                db_customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                self.__Customers.append(db_customer)
        return self.__Customers

    def get_credit_card_list(self):
        self.__CreditCards.clear()
        with open(os.path.realpath('Data/CreditCards.csv')) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            credit_card_list = list(csv_reader)
            for row in credit_card_list:
                db_credit_card = CreditCard(row[0], row[1], row[2], row[3])
                self.__CreditCards.append(db_credit_card)
        return self.__CreditCards

    def get_customer_primary_keys(self):
        self._primary_keys.clear()
        with open(os.path.realpath('Data/Customers.csv')) as customer_file:
            csv_reader = csv.reader(customer_file, delimiter=';')
            customer_list = list(csv_reader)
            for row in customer_list:
                self._primary_keys.append(row[0])
        return self._primary_keys

    def get_credit_card_primary_keys(self):
        self._primary_keys.clear()
        with open(os.path.realpath('Data/CreditCards.csv')) as customer_file:
            csv_reader = csv.reader(customer_file, delimiter=';')
            customer_list = list(csv_reader)
            for row in customer_list:
                self._primary_keys.append(row[1])
        return self._primary_keys
        