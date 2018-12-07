import os
from datetime import datetime

from Services.RentalService import RentalService
from Services.ValidationService import ValidationService
from Models.Rental import Rental
from ViewModels.RentalViewModel import RentalViewModel
from UI.DisplayHeader import DisplayHeader
from UI.CustomerSubMenu import CustomerSubMenu
from UI.CarSubMenu import CarSubMenu



class RentalSubMenu:

    def __init__(self):
        self.valid = False
        self._display_header = DisplayHeader()
        self._rental_service = RentalService()
        self._validation_service = ValidationService()
        self._customer_sub_menu = CustomerSubMenu()
        self._car_sub_menu = CarSubMenu()
        

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
            return_car = self.get_return_a_car_input()
            return
        if user_input == "4":
            return
        if user_input == "5":
            return
        if user_input == "6":
            return

#Inputs
    def get_rental_input(self):
        self.valid = False
        while not self.valid:
            customer_id = input("Enter ID for customer: ")
            self.valid = self._validation_service.does_customer_id_exist(customer_id)
            if not self.valid:
                print("Customer does not exist, please register customer first")
                # Print a list of customers here
                self._customer_sub_menu.see_customer_list()
                print("Customer does not exist, please register customer first")
                #os.system('pause')
        self.valid = False
        while not self.valid:
            self._car_sub_menu.see_fleet_list_in_rent_a_car()
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
        
        print("t\ Order successful \n"
            "t\ Customer " + customer_id + "\n"
            "t\ Car number"  + car_id + "\n"
        )
        os.system('pause')
        return new_rental
    def get_return_a_car_input(self):
        #Má henda út Order ID úr þessu ef við ákveðum að það sé bara hægt að leita eftir bílnúmeri
        #Hef ekki search for Customer ID vegna þess að ef vv. hefur fleiri
        #en tvo bíla á leigu þá þarf að setja inn auka valmynd fyrir það
        self.return_a_car_view()
        self.valid = False
        print ( "Search order by: \n\n"
                "[ 1 ] By car ID\n"
                "[ 2 ] By order ID\n"
                "[ q ] Return to main menu\n")
        return_car_user_input = input('Please select an option: ')
        while not self.valid:
            if return_car_user_input == "1":
                car_id = input("Enter car ID: ")
                self.valid = self._validation_service.does_car_id_exist(car_id)
                if not self.valid:
                    print("Car does not exist")
                    # Print a list of cars that are in rental here
                    os.system('pause')
            if return_car_user_input == "2":
                order_id = input("Enter order ID: ")
                self.valid = self._validation_service.is_order_id_valid(order_id)
                if not self.valid:
                    print("Order id does not exsist")
                    os.system('pause')
            if return_car_user_input == "q":
                return
        self.return_a_car_view()
        self.valid = False
        print ( "Is the Car OK?: \n\n"
                "[ 1 ] Yes\n"
                "[ 2 ] No, write a comment\n"
                "[ q ] Return to main menu\n")
        return_car_user_input_is_ok = input('Please select an option: ')
        while not self.valid:
            if return_car_user_input_is_ok == "1":
                self.valid = self._validation_service.is_number_negative(return_car_user_input_is_ok)
            if return_car_user_input_is_ok == "2":
                print('hér vantar að setja inn skjá þar sem hægt er að skrifa comment um hvað er að')
                os.system('pause')
                return
            if return_car_user_input_is_ok == "q":
                return
        self.return_a_car_view()
        self.valid = False
        print ( "Was the fuel tank full?: \n\n"
            "[ 1 ] Yes\n"
            "[ 2 ] No\n"
            "[ q ] Return to main menu\n")
        while not self.valid:
            return_car_user_input_fuel_full = input('Please select an option: ')
            self.valid = self._validation_service.is_number_negative(return_car_user_input_is_ok)
            if return_car_user_input_fuel_full == "1":
                print('Print reciept. \n\nThank you for renting a car from Bragginn\n')
                os.system('pause')
                return
            if return_car_user_input_fuel_full == "2":
                self.return_a_car_view()
                self.valid = False
                print ( "How much gas was on the car?: \n\n"
                    "[ 1 ] 3/4\n"
                    "[ 2 ] 2/4\n"
                    "[ 3 ] 1/4\n"
                    "[ 4 ] less than 1/4\n"
                    "[ q ] Return to main menu\n")
                while not self.valid:
                    return_car_user_input_fuel_how_much = input('Please select an option: ')
                    self.valid = self._validation_service.is_number_negative(return_car_user_input_fuel_how_much)
                    print ( "Hér kemur Payment Option til að borga fyrir bensínið")
                    os.system('pause')
                    return
            if return_car_user_input_fuel_full == "q":
                return

        
        



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
    
    def return_a_car_view(self):
        os.system('cls')
        print(  "\t ___     _                     _      ___          \n"
                "\t| _ \___| |_ _  _ _ _ _ _     /_\    / __|__ _ _ _ \n"
                "\t|   / -_)  _| || | '_| ' \   / _ \  | (__/ _` | '_|\n"
                "\t|_|_\___|\__|\_,_|_| |_||_| /_/ \_\  \___\__,_|_|   \n\n"  )           
