import os
from datetime import datetime

from Services.RentalService import RentalService
from Services.ValidationService import ValidationService
from Models.Rental import Rental
from ViewModels.RentalViewModel import RentalViewModel
from UI.DisplayHeader import DisplayHeader


class RentalSubMenu:

    def __init__(self):
        self.valid = False
        self._display_header = DisplayHeader()
        self._rental_service = RentalService()
        self._validation_service = ValidationService()

    def rental_sub_menu(self):
        """Display's the rentals submenu"""
        self._display_header.display_header_rentals()
        print("\t1. Rent a Car \n"
              "\t2. Rental History \n"
              "\t3. Return Car \n"
              "\t4. Cancel Order \n"
              "\t5. Change Order \n"
              "\t6. See All Orders \n"
              "\tEnter q to quit \n")
        user_input = input('What would you like to do? ')

        if user_input == "1":
            new_rental = self.get_rental_input()
            self._rental_service.add_rental(new_rental)
        if user_input == "2":
            #Hafa kannski ser get user input fall sem er ur user input interface klasa
            car_id = input("Enter ID of car to see rental history: ")
            rental_view = self._rental_service.get_car_rental_history(car_id)
            self.see_rental_view_list(rental_view)
            #Senda rentalView svo i view sem prentar ut listann
        if user_input == "3":
            return
        if user_input == "4":
            return
        if user_input == "5":
            return
        if user_input == "6":
            return

#Inputs
    def get_rental_input(self):
        while not self.valid:
            customer_id = input("Enter ID for customer: ")
            self.valid = self._validation_service.does_customer_id_exist(customer_id)
            if not self.valid:
                print("Customer does not exist, please register customer first")
                # Print a list of customers here
                os.system('pause')
        self.valid = False
        while not self.valid:
            car_id = input("Enter ID of car to rent: ")
            self.valid = self._validation_service.does_car_id_exist(car_id)
            if not self.valid:
                print("Car does not exist")
                # Print a list of cars here
                os.system('pause')
        self.valid = False
        while not self.valid:
            start_date_input = input("Enter start date in the format DD/MM/YYYY: ")
            self.valid = self._validation_service.is_date_valid(start_date_input)
            if not self.valid:
                print("Car does not exist")
                # Print a list of cars here
                os.system('pause')
        start_date = datetime.date(datetime.strptime(start_date_input, '%d/%m/%Y'))
        self.valid = False
        while not self.valid:
            days = input("Enter how many days to rent: ")
            self.valid = self._validation_service.is_number_negative(days)
            if not self.valid:
                print("Can not rent for negative days")
                # Print a list of cars here
                os.system('pause')
        self.valid = False
        while not self.valid:
            insurance = input("Enter insurance short code: ")
            self.valid = self._validation_service.does_short_code_exist(insurance)
            if not self.valid:
                print("Can not rent for negative days")
                # Print a list of cars here
                os.system('pause')
        total_price = 0 #Here we need to go to the service layer and calculate total price
        order_id = self._rental_service.get_and_set_next_order_id()
        new_rental = Rental(order_id, customer_id, car_id, start_date, days, insurance, total_price)
        return new_rental

#Views
    def see_rental_list(self):
        rental_list = self._rental_service.get_rental_list()
        os.system('cls')
        # Here we need a proper header in a seperate function in DisplayHeader.py
        print("\t ___         _        _   _    _    _   \n"
              "\t| _ \___ _ _| |_ __ _| | | |  (_)__| |_ \n"
              "\t|   / -_) ' \  _/ _` | | | |__| (_-<  _|\n"
              "\t|_|_\___|_||_\__\__,_|_| |____|_/__/\__|\n\n"
                "\tcustomerID:     carID:       startDate:      days:      total price: \n")
        for rental in rental_list:
            print(rental)
        os.system('pause')

    def see_rental_view_list(self, rvList): #Rental viewlist comes in
        os.system('cls')
        # Here we need a proper header in a seperate function in DisplayHeader.py
        print("\t ___         _        _   _    _    _   \n"
              "\t| _ \___ _ _| |_ __ _| | | |  (_)__| |_ \n"
              "\t|   / -_) ' \  _/ _` | | | |__| (_-<  _|\n"
              "\t|_|_\___|_||_\__\__,_|_| |____|_/__/\__|\n\n"              
                "\tcustomerID:     carID:       startDate:      days:      total price: \n")
        for rental in rvList:
            print(rental)
        os.system('pause')
