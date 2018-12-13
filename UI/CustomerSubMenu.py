import os

from Services.CustomerService import CustomerService
from Services.RentalService import RentalService
from Services.ValidationService import ValidationService
from Models.Customer import Customer
from Models.CreditCard import CreditCard
from UI.DisplayHeader import DisplayHeader
from UI.SystemSpecificUI import SystemSpecificUI


class CustomerSubMenu:

    def __init__(self):
        self.valid = False
        self._display_header = DisplayHeader()
        self._customer_service = CustomerService()
        self._rental_service = RentalService()
        self._validation_service = ValidationService()
        self._system = SystemSpecificUI()

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

        # Register New Customer 
        if user_input == "1":
            self.new_customer_view()
            new_customer = self.get_add_customer_input()
            if new_customer == "q":
                print("Adding a new customer has been cancelled")
                self._system.pause_system()
                return
            self._customer_service.add_customer(new_customer)
        # Search Customers
        if user_input == "2":
            customer_id = self.get_customer_id_input()
            if customer_id == "q":
                return
            customer = self._customer_service.get_customer(customer_id)
            credit_cards = self._customer_service.get_customer_credit_cards(customer_id)
            self.see_customer(customer, credit_cards)
        # Delete Customer
        if user_input == "3":
            self.delete_customer_view()
            customer_id = self.get_customer_id_input()
            if customer_id == "q":
                return
            print("Are you sure you want to delete customer number: " + customer_id)
            user_answer = input("Select y to delete customer from database: ")
            if user_answer == 'y' or user_answer == 'Y':
                self._customer_service.delete_customer(customer_id)
                print("Customer deleted from database")
                self._system.pause_system()
            else:
                print("Customer deletion cancelled ")
                self._system.pause_system()
                return
        #Change Customer Info
        if user_input == "4":
            self._system.clear_screen()
            self.change_customer_info_view()
            customer_id = self.get_customer_id_input()
            if customer_id == "q":
                return
            customer = self._customer_service.get_customer(customer_id)
            change = self.get_change_customer_input(customer)
            self.update_customer(change, customer)
        # See Customer History
        if user_input == "5":
            customer_id = self.get_customer_id_input()
            if customer_id == "q":
                return
            customer = self._customer_service.get_customer(customer_id)
            customer_rentals = self._rental_service.get_customer_rental_history(customer_id)
            credit_cards = self._customer_service.get_customer_credit_cards(customer_id)
            self.see_customer_history(customer, customer_rentals, credit_cards)
        # See All Customers
        if user_input == "6":
            self.see_customer_list()
            self._system.pause_system()
        # Add Customer Credit Card
        if user_input == "7":
            self.add_credit_card_view()
            new_card = self.get_add_creditcard_input()
            if new_card == "q":
                print("Adding a new credit card has been cancelled")
                self._system.pause_system()
                return
            self._customer_service.add_credit_card(new_card)

# Inputs
    def get_add_customer_input(self):
        """Gets the input and validates it when adding customer to database"""
        self.valid = False
        while not self.valid:
            customer_id = input("Enter ID for customer: ")
            if customer_id == "q":
                return "q"
            self.valid = self._validation_service.is_customer_id_valid(customer_id)
            if not self.valid:
                print("Customer Id is not valid")
                self._system.pause_system()
                continue
            self.valid = not self._validation_service.does_customer_id_exist(customer_id)
            if not self.valid:
                print("Customer Id already exists")
                self._system.pause_system()
        self.valid = False
        while not self.valid:
            first_name = input("Enter customer first name: ")
            if first_name == "q":
                    return "q"
            self.valid = self._validation_service.is_first_name_valid(first_name)
            if not self.valid:
                print("Please enter between 1-10 letters")
                self._system.pause_system()
        self.valid = False
        while not self.valid:
            last_name = input("Enter customer last name: ")
            if last_name == "q":
                    return "q"
            self.valid = self._validation_service.is_last_name_valid(last_name)
            if not self.valid:
                print("Please enter between 1-15 letters")
                self._system.pause_system()
        self.valid = False
        while not self.valid:
            phone = input("Enter customer phone: ")
            if last_name == "q":
                return "q"
            self.valid = self._validation_service.is_phone_valid(phone)
            if not self.valid:
                print("Please enter a valid phone number")
                self._system.pause_system()
        self.valid = False
        while not self.valid:
            street = input("Enter customer street: ")
            if street == "q":
                return "q"
            self.valid = self._validation_service.is_street_valid(street)
            if not self.valid:
                print("Please enter street name and number (Max length 20 letters)")
                self._system.pause_system()
        self.valid = False
        while not self.valid:
            zip = input("Enter customer zip: ")
            if zip == "q":
                return "q"
            self.valid = self._validation_service.is_zip_valid(zip)
            if not self.valid:
                print("Please enter a valid Zip")
                self._system.pause_system()
        self.valid = False
        while not self.valid:
            town = input("Enter customer town: ")
            if town == "q":
                return "q"
            self.valid = self._validation_service.is_town_valid(town)
            if not self.valid:
                print("Please enter between 1-20 letters")
                self._system.pause_system()
        self.valid = False
        while not self.valid:
            country = input("Enter customer country: ")
            if country == "q":
                return "q"
            self.valid = self._validation_service.is_country_valid(country)
            if not self.valid:
                print("Please enter between 1-10 letters")
                self._system.pause_system()
        self.valid = False
        while not self.valid:
            drivers_license = input("Enter customer driver's license number: ")
            if drivers_license == "q":
                return "q"
            self.valid = self._validation_service.is_drivers_license_valid(drivers_license)
            if not self.valid:
                print("Please enter a valid driver's license number (7-12 digits)")
                self._system.pause_system()
        self.valid = False
        new_customer = Customer(customer_id, first_name, last_name, phone, street, zip, town, country, drivers_license)
        return new_customer

    def get_add_creditcard_input(self):
        """Gets the input and validates it when adding credit card to database"""
        self.valid = False
        while not self.valid:
            customer_id = input("Enter customer ID for owner of credit card: ")
            if customer_id == "q":
                return "q"
            self.valid = self._validation_service.does_customer_id_exist(customer_id)
            if not self.valid:
                print("Customer does not exist, please register customer first")
                self._system.pause_system()
                self.see_customer_list()
        self.valid = False
        customer = self._customer_service.get_customer_viewmodel(customer_id)
        self.add_credit_card_view_and_customer(customer)
        while not self.valid:
            card_number = input("Credit card number: ")
            if card_number == "q":
                return "q"
            self.valid = self._validation_service.is_card_number_valid(card_number)
            if not self.valid:
                print("Please enter a valid card number")
                self._system.pause_system()
        self.valid = False
        while not self.valid:
            expiry = input("Enter expiry date (MM/YY): ")
            if expiry == "q":
                return "q"
            self.valid = self._validation_service.is_expiry_valid(expiry)
            if not self.valid:
                print("Please enter a valid expiry date")
                self._system.pause_system()
        self.valid = False
        while not self.valid:
            cvc = input("Enter cvc number: ")
            if cvc == "q":
                return "q"
            self.valid = self._validation_service.is_cvc_valid(cvc)
            if not self.valid:
                print("Please enter a valid cvc number (3 digits on back of card) ")
                self._system.pause_system()
        self.valid = False
        new_card = CreditCard(customer_id, card_number, expiry, cvc)
        return new_card

    def get_add_creditcard_input_from_rental(self, customer_id):
        """Gets the input and validates it when adding credit card to database straight from a rental"""
        self.valid = False
        customer = self._customer_service.get_customer_viewmodel(customer_id)
        self.add_credit_card_view_and_customer(customer)
        while not self.valid:
            card_number = input("Credit card number: ")
            if card_number == "q":
                return "q"
            self.valid = self._validation_service.is_card_number_valid(card_number)
            if not self.valid:
                print("Please enter a valid card number")
                self._system.pause_system()
        self.valid = False
        while not self.valid:
            expiry = input("Enter expiry date (MM/YY): ")
            if expiry == "q":
                return "q"
            self.valid = self._validation_service.is_expiry_valid(expiry)
            if not self.valid:
                print("Please enter a valid expiry date")
                self._system.pause_system()
        self.valid = False
        while not self.valid:
            cvc = input("Enter cvc number: ")
            if cvc == "q":
                return "q"
            self.valid = self._validation_service.is_cvc_valid(cvc)
            if not self.valid:
                print("Please enter a valid cvc number (3 digits on back of card) ")
                self._system.pause_system()
        self.valid = False
        new_card = CreditCard(customer_id, card_number, expiry, cvc)
        return new_card

    def get_customer_id_input(self):
        """Gets the input for when adding customer id"""
        self.valid = False
        while not self.valid:
            customer_id = input("\nEnter customer ID: ")
            if customer_id == "q":
                return "q"
            self.valid = self._validation_service.does_customer_id_exist(customer_id)
            if not self.valid:
                self.see_customer_list()
                print("Customer does not exist")
        return customer_id

    def get_change_customer_input(self, customer):
        """Displays the menu and gets input for when changing customer info"""
        self._system.clear_screen()
        self.change_customer_info_view()
        print("ID           Name                              Phone           Street         Zip         Town          Country     License")
        print(customer)
        print("\n[1] Change ID                                [6] Change zip\n"
                "[2] Change first name                        [7] Change town\n"
                "[3] Change last name                         [8] Change country \n"
                "[4] Change phone                             [9] Change drivers license number \n"
                "[5] Change street                            [Q] Return to main menu \n\n")
        user_input = input("What would you like to change? ")
        return user_input

    def update_customer(self, change, customer):
        """Gets the input and validates it when when changing customer info"""
        self.valid = False
        if change == '1':
            new_customer_id = input("Enter new ID for customer: ")
            id_valid = self._validation_service.is_customer_id_valid(new_customer_id)
            id_already_exist = self._validation_service.does_customer_id_exist(new_customer_id)
            if id_valid and not id_already_exist:
                self._customer_service.update_customer_id(customer, new_customer_id)
            else:
                print("Can not update to this value")
        elif change == '2':
            new_first_name = input("Enter customer new first name: ")
            self._customer_service.update_customer_first_name(customer, new_first_name)
        elif change == '3':
            new_last_name = input("Enter customer new last name: ")
            self._customer_service.update_customer_last_name(customer, new_last_name)
        elif change == '4':
            while not self.valid:
                new_phone = input("Enter new customer phone: ")
                self.valid = self._validation_service.is_phone_valid(new_phone)
                if not self.valid:
                    print("Please enter a valid phone number")
                    self._system.pause_system()
            self._customer_service.update_customer_phone(customer, new_phone)
        elif change == '5':
            new_street = input("Enter customer new street: ")
            self._customer_service.update_customer_street(customer, new_street)
        elif change == '6':
            while not self.valid:
                new_zip = input("Enter customer new zip: ")
                self.valid = self._validation_service.is_zip_valid(new_zip)
                if not self.valid:
                    print("Please enter a valid Zip")
                    self._system.pause_system()
            self._customer_service.update_customer_zip(customer, new_zip)
        elif change == '7':
            new_town = input("Enter customer new town: ")
            self._customer_service.update_customer_town(customer, new_town)
        elif change == '8':
            new_country = input("Enter customer new country: ")
            self._customer_service.update_customer_country(customer, new_country)
        elif change == '9':
            while not self.valid:
                new_drivers_license = input("Enter customer new driver's license number: ")
                self.valid = self._validation_service.is_drivers_license_valid(new_drivers_license)
                if not self.valid:
                    print("Please enter a valid driver's license number (7-12 digits)")
                    self._system.pause_system()
            self._customer_service.update_customer_license(customer, new_drivers_license)

# Views
    def see_customer_list(self):
        """Displays list of customers"""
        customer_list = self._customer_service.get_customer_list()
        self._system.clear_screen()
        print("\t  ___        _                        \n"
              "\t / __|  _ __| |_ ___ _ __  ___ _ _ ___\n"
              "\t| (_| || (_-<  _/ _ \ '  \/ -_) '_(_-<\n"
              "\t \___\_,_/__/\__\___/_|_|_\___|_| /__/\n\n"
                "customerID   Name                              Phone           House          Zip            City            Country     LicenceNr")
        for customer in customer_list:
            print(customer)

    def see_customer(self, Customer, credit_cards):
        """Displays single customer"""
        self._system.clear_screen()
        print("\t  ___        _                        \n"
              "\t / __|  _ __| |_ ___ _ __  ___ _ _ ___\n"
              "\t| (_| || (_-<  _/ _ \ '  \/ -_) '_(_-<\n"
              "\t \___\_,_/__/\__\___/_|_|_\___|_| /__/\n\n"
                                      
                "customerID   Name                              Phone           House          Zip            City            Country     LicenceNr")
        print(Customer)
        print("Credit Cards:")
        for creditcard in credit_cards:
            print(creditcard)
        self._system.pause_system()

    def see_customer_history(self, customer, customer_rentals, credit_cards):
        """Displays customer history"""
        self._system.clear_screen()
        print(  "\t  ___        _                       _  _ _    _                \n"
                "\t / __|  _ __| |_ ___ _ __  ___ _ _  | || (_)__| |_ ___ _ _ _  _ \n"
                "\t| (_| || (_-<  _/ _ \ '  \/ -_) '_| | __ | (_-<  _/ _ \ '_| || |\n"
                "\t \___\_,_/__/\__\___/_|_|_\___|_|   |_||_|_/__/\__\___/_|  \_, |\n"
                "\t                                                           |__/ \n\n"
                "Customer info:\n\n"
                "customerID   Name                              Phone           House          Zip            City            Country     LicenceNr")
        print(customer)
        print("Credit Cards: \n")
        for creditcard in credit_cards:
            print(creditcard)
        print("\nRental history:\n")
        print("Order  CustomerID   Name                       CarNr   Brand             Type       StartDate    EndDate      Ins.  Total cost ")

        for rental in customer_rentals:
            print(rental)
        self._system.pause_system()

    def change_customer_info_view(self):
        """Displays view for when changing customer info"""
        self._system.clear_screen()
        print(  "\t  ___ _                          ___        _                       ___       __     \n"
                "\t / __| |_  __ _ _ _  __ _ ___   / __|  _ __| |_ ___ _ __  ___ _ _  |_ _|_ _  / _|___ \n"
                "\t| (__| ' \/ _` | ' \/ _` / -_) | (_| || (_-<  _/ _ \ '  \/ -_) '_|  | || ' \|  _/ _ \ \n"
                "\t \___|_||_\__,_|_||_\__, \___|  \___\_,_/__/\__\___/_|_|_\___|_|   |___|_||_|_| \___/\n"
                "\t                    |___/                                                            \n\n")
    
    def new_customer_view(self):
        """Displays view for when adding new customer"""
        self._system.clear_screen()
        print(  "\t _  _               ___        _                     \n"
                "\t| \| |_____ __ __  / __|  _ __| |_ ___ _ __  ___ _ _ \n"
                "\t| .` / -_) V  V / | (_| || (_-<  _/ _ \ '  \/ -_) '_|\n"
                "\t|_|\_\___|\_/\_/   \___\_,_/__/\__\___/_|_|_\___|_|   \n\n")

    def add_credit_card_view(self):
        """Displays view for when adding new credit card"""
        self._system.clear_screen()
        print(  "\t   _      _    _    ___            _ _ _      ___             _ \n"
                "\t  /_\  __| |__| |  / __|_ _ ___ __| (_) |_   / __|__ _ _ _ __| |\n"
                "\t / _ \/ _` / _` | | (__| '_/ -_) _` | |  _| | (__/ _` | '_/ _` |\n"
                "\t/_/ \_\__,_\__,_|  \___|_| \___\__,_|_|\__|  \___\__,_|_| \__,_|\n\n")

    def add_credit_card_view_and_customer(self, Customer):
        """Displays view for when adding new credit card, with customer"""
        self._system.clear_screen()
        print(  "\t   _      _    _    ___            _ _ _      ___             _ \n"
                "\t  /_\  __| |__| |  / __|_ _ ___ __| (_) |_   / __|__ _ _ _ __| |\n"
                "\t / _ \/ _` / _` | | (__| '_/ -_) _` | |  _| | (__/ _` | '_/ _` |\n"
                "\t/_/ \_\__,_\__,_|  \___|_| \___\__,_|_|\__|  \___\__,_|_| \__,_|\n\n")

        print("Customer ID  Name        Country")
        print(Customer)
        print("\nRegistered Credit Cards:")
        for creditcard in Customer._card_number:
            print(creditcard)
        print("\nEnter a new credit card in the format 0000111122223333\n")

    def delete_customer_view(self):
        """Displays view for when deleting customer"""
        self._system.clear_screen()
        print(  "\t ___      _     _          ___        _                     \n"
                "\t|   \ ___| |___| |_ ___   / __|  _ __| |_ ___ _ __  ___ _ _ \n"
                "\t| |) / -_) / -_)  _/ -_) | (_| || (_-<  _/ _ \ '  \/ -_) '_|\n"
                "\t|___/\___|_\___|\__\___|  \___\_,_/__/\__\___/_|_|_\___|_|  \n"
                "\t                                                            \n\n")