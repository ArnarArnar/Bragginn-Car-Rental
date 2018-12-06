import os

from Services.CustomerService import CustomerService
from Services.RentalService import RentalService
from Services.ValidationService import ValidationService
from Models.Customer import Customer
from Models.CreditCard import CreditCard
from UI.DisplayHeader import DisplayHeader


class CustomerSubMenu:

    def __init__(self):
        self.valid = False
        self._display_header = DisplayHeader()
        self._customer_service = CustomerService()
        self._rental_service = RentalService()
        self._validation_service = ValidationService()

    def customer_sub_menu(self):
        """Display's the customer submenu"""
        self._display_header.display_header_customer()
        print("\t1. Register New Customer \n"
              "\t2. Search Customers \n"
              "\t3. Delete Customer \n"
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
            customer = self._customer_service.get_customer(customer_id) #This is a view model, needs to be a proper class
            self.see_customer(customer)
        if user_input == "3":
            customer_id = self.get_customer_id_input()
            print("Are you sure you want to delete customer number: " + customer_id)
            user_answer = input("Select y to delete customer from database: ")
            if user_answer == 'y' or user_answer == 'Y':
                self._customer_service.delete_customer(customer_id)
                print("Customer deleted from database")
                os.system('pause')
            else:
                print("Customer deletion cancelled ")
                os.system('pause')
                return
        if user_input == "4":
            customer_id = self.get_customer_id_input()
            customer = self._customer_service.get_customer(customer_id)
            change = self.get_change_customer_input(customer)
            self.update_customer(change, customer)
        if user_input == "5":
            customer_id = self.get_customer_id_input()
            customer = self._customer_service.get_customer(customer_id)
            customer_rentals = self._rental_service.get_customer_rental_history(customer_id)
            self.see_customer_history(customer, customer_rentals)
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

    def get_change_customer_input(self, customer): # customer_id, first_name, last_name, phone, street, zip, town, country, drivers_license
        os.system('cls')
        print("\t*************** Bragginn Car Rental ************ \n"
                "\t************************************************** \n"
                "\t**************** Customer List **************** \n"
                "ID           Name                              Phone           Street         Zip         Town          Country     License: \n")
        print(customer)
        print("\t1. Change ID               6. Change zip\n"
                "\t2. Change first name     7. Change town\n"
                "\t3. Change last name      8. Change country \n"
                "\t4. Change phone          9. Change drivers license number"
                "\t5. Change street")
        user_input = input("What would you like to change? ")
        # Here we need to validate that the input is correct try and catch
        return user_input

    def update_customer(self, change, customer):
        new_value = input("Enter new value: ")
        if change == '1': #ID
            id_valid = self._validation_service.is_customer_id_valid(new_value)
            id_already_exist = self._validation_service.does_customer_id_exist(new_value)
            if id_valid and not id_already_exist:
                self._customer_service.update_customer_id(customer, new_value)
            else:
                print("Can not update to this value")
        elif change == '2': #First
            print(" 2 was selected ")
            self._customer_service.update_customer_first_name(customer, new_value)
        elif change == '3': #Last
            self._customer_service.update_customer_last_name(customer, new_value)
        elif change == '4': #phone
            self._customer_service.update_customer_phone(customer, new_value)
        elif change == '5': #street
            self._customer_service.update_customer_street(customer, new_value)
        elif change == '6': #zip
            self._customer_service.update_customer_zip(customer, new_value)
        elif change == '7': #town
            self._customer_service.update_customer_town(customer, new_value)
        elif change == '8': #country
            self._customer_service.update_customer_country(customer, new_value)
        elif change == '9': #license
            self._customer_service.update_customer_license(customer, new_value)

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

    def see_customer_history(self, customer, customer_rentals): #Rental viewlist comes in
        os.system('cls')
        # Here we need a proper header in a seperate function in DisplayHeader.py
        print("\t*************** Bragginn Car Rental ************ \n"
                "\t************************************************** \n"
                "\t**************** Rental List **************** \n"
                "\tcustomerID:     carID:       startDate:      days:      total price: \n")
        
        print("Customer info: ")
        print(customer)
        print("Credit Cards:")
        for creditcard in customer._card_number:
            print(creditcard)
        print("Rental history: ")
        for rental in customer_rentals:
            print(rental)
        os.system('pause')
        