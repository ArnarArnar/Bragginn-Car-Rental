import os

from Services.CustomerService import CustomerService
from Services.ValidationService import ValidationService
from Models.Customer import Customer
from Models.CreditCard import CreditCard
from UI.DisplayHeader import DisplayHeader


class CustomerSubMenu:

    def __init__(self):
        self.valid = False
        self._display_header = DisplayHeader()
        self._customer_service = CustomerService()
        self._validation_service = ValidationService()

    def customer_sub_menu(self):
        """Display's the customer submenu"""
        self._display_header.display_header()
        print("\t1. Register New Customer \n"
              "\t2. Search Customers \n"
              "\t3. Deactivate Customer \n"
              "\t4. Change Customer Info \n"
              "\t5. See Customer History \n"
              "\t6. See All Customers \n"
              "\t7. Add Customer Credit Card \n"
              "\tEnter q to quit \n")
        user_input = input('What would you like to do? ')

        if user_input == "1":
            new_customer = self.get_add_customer_input()
            self._customer_service.add_customer(new_customer)
        if user_input == "2":
            customer_id = self.get_customer_id_input()
            customer = self._customer_service.get_customer(customer_id)
            self.see_customer(customer)
        if user_input == "3":
            return
        if user_input == "4":
            return
        if user_input == "5":
            return
        if user_input == "6":
            self.see_customer_list()
        if user_input == "7":
            new_card = self.get_add_creditcard_input()
            self._customer_service.add_credit_card(new_card)

# Inputs
    def get_add_customer_input(self):
        while not self.valid:
            customer_id = input("Enter ID for customer: ")
            self.valid = self._validation_service.is_customer_id_valid(customer_id)
            if not self.valid:
                print("Customer Id is not valid")
                os.system('pause')
        self.valid = False
        first_name = input("Enter customer first name: ") # Do we need to validate?
        last_name = input("Enter customer last name: ") # Do we need to validate?
        while not self.valid:
            phone = input("Enter customer phone: ")
            self.valid = self._validation_service.is_phone_valid(phone)
            if not self.valid:
                print("Please enter a valid phone number")
                os.system('pause')
        self.valid = False
        street = input("Enter customer street: ") # Do we need to validate?
        while not self.valid:
            zip = input("Enter customer zip: ")
            self.valid = self._validation_service.is_zip_valid(zip)
            if not self.valid:
                print("Please enter a valid Zip")
                os.system('pause')
        self.valid = False
        town = input("Enter customer town: ")
        country = input("Enter customer country: ")
        while not self.valid:
            drivers_license = input("Enter customer driver's license number: ")
            self.valid = self._validation_service.is_zip_valid(zip)
            if not self.valid:
                print("Please enter a valid driver's license number")
                os.system('pause')
        self.valid = False
        new_customer = Customer(customer_id, first_name, last_name, phone, street, zip, town, country, drivers_license)
        return new_customer

    def get_add_creditcard_input(self): # customer_id, card_number, expiry, cvc
        while not self.valid:
            customer_id = input("Enter customer ID for owner of credit card: ")
            self.valid = self._validation_service.does_customer_id_exist(customer_id)
            if not self.valid:
                print("Customer does not exist, please register customer first")
                os.system('pause')
                self.see_customer_list()
        self.valid = False
        while not self.valid:
            card_number = input("Enter credit card number: ")
            self.valid = self._validation_service.is_card_number_valid(card_number)
            if not self.valid:
                print("Please enter a valid card number")
                os.system('pause')
        self.valid = False
        while not self.valid:
            expiry = input("Enter expiry date (MM/YY): ")
            self.valid = self._validation_service.is_expiry_valid(expiry)
            if not self.valid:
                print("Please enter a valid expiry date")
                os.system('pause')
        self.valid = False
        while not self.valid:
            cvc = input("Enter cvc number: ")
            self.valid = self._validation_service.is_cvc_valid(cvc)
            if not self.valid:
                print("Please enter a valid cvc number (3 digits on back of card) ")
                os.system('pause')
        self.valid = False
        new_card = CreditCard(customer_id, card_number, expiry, cvc)
        return new_card

    def get_customer_id_input(self):
        self.valid = False
        while not self.valid:
            customer_id = input("Enter customer ID: ")
            self.valid = self._validation_service.does_customer_id_exist(customer_id)
            if not self.valid:
                print("Customer does not exist")
                os.system('pause')
                self.see_customer_list()
        return customer_id

# Views
    def see_customer_list(self):
        customer_list = self._customer_service.get_customer_list()
        os.system('cls')
        print("\t*************** Bragginn Car Rental ************ \n"
                "\t**************************************************\n"
                "\t**************** Customer3 List ****************\n"
                "ID           Name                              Phone           Street         Zip         Town          Country     License: \n")
        for customer in customer_list:
            print(customer)
        os.system('pause')

    def see_customer(self, Customer):
        os.system('cls')
        print("\t*************** Bragginn Car Rental ************ \n"
                "\t************************************************** \n"
                "\t**************** Customer List **************** \n"
                "ID           Name                              Phone           Street         Zip         Town          Country     License: \n")
        print(Customer)
        print("Credit Cards:")
        for creditcard in Customer._card_number:
            print(creditcard)
        os.system('pause')
        