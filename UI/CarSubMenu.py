import os

from Services.CarService import CarService
from Services.RentalService import RentalService
from Services.ValidationService import ValidationService
from Models.Car import Car
from UI.DisplayHeader import DisplayHeader


class CarSubMenu:

    def __init__(self):
        self.valid = False
        self._display_header = DisplayHeader()
        self._car_service = CarService()
        self._rental_service = RentalService()
        self._validation_service = ValidationService()

    def car_sub_menu(self):
        """Display's the car submenu"""
        self._display_header.display_header_fleet()
        print("\t1. See Fleet List \n"
              "\t2. See All in Rental \n"
              "\t3. See All Available Cars \n"
              "\t4. Add Car \n"
              "\t5. See Car History \n"
              "\tEnter q to quit \n")
        user_input = input('What would you like to do? ')
        # See Fleet List
        if user_input == "1":
            self.see_fleet_list()
        # See All in Rental
        if user_input == "2":
            self.see_all_in_rental()
        # See All Available Cars
        if user_input == "3":
            self.see_all_available()
        # Add Car
        if user_input == "4":
            new_car = self.get_add_car_input()
            self._car_service.add_car(new_car)
        # See Car History
        if user_input == "5":
            car_id = self.get_car_id_input()
            rental_view = self._rental_service.get_car_rental_history(car_id)
            self.see_rental_view_list(rental_view)

#Inputs
    def get_add_car_input(self):
        self.valid = False
        while not self.valid:
            car_id = input("Enter car ID (AAADD if older car AADDD): ")
            self.valid = self._validation_service.is_car_id_valid(car_id)
            if not self.valid:
                print("Car Id can not be longer then X ")
                os.system('pause')
                continue
            self.valid = not self._validation_service.does_car_id_exist(car_id)
            if not self.valid:
                print("Car Id already exists")
                os.system('pause')
        brand = input("Enter car brand: ")
        self.valid = False
        while not self.valid:
            year = input("Enter year of car model (YYYY): ")
            self.valid = self._validation_service.is_year_valid(year)
            if not self.valid:
                print("Year needs to be in the format (YYYY)")
                os.system('pause')
        self.valid = False
        while not self.valid:
            price_per_day = input("Enter price per day: ")
            self.valid = self._validation_service.is_year_valid(year)
            if not self.valid:
                print("Price can not be negative")
                os.system('pause')
        self.valid = False
        while not self.valid:
            car_type = input("Enter car type: ")
            self.valid = self._validation_service.is_year_valid(year)
            if not self.valid:
                print("Car type can only be one of 4 types (Jeep, Luxury, Budget, Family")
                os.system('pause')
        new_car = Car(car_id, brand, year, price_per_day, car_type)
        return new_car

    def get_car_id_input(self):
        self.valid = False
        while not self.valid:
            car_id = input("Enter car ID (AADDD): ")
            self.valid = self._validation_service.is_car_id_valid(car_id)
            if not self.valid:
                print("Car Id can not be longer then X ")
                os.system('pause')
                continue
            self.valid = not self._validation_service.does_car_id_exist(car_id)
            if not self.valid:
                print("Car Id already exists")
                os.system('pause')
        return car_id

#Views
    def see_fleet_list(self):
        fleet_list = self._car_service.get_fleet_list()
        os.system('cls') ##display header function instead
        print(
              "\t ___ _         _     _    _    _   \n"
              "\t| __| |___ ___| |_  | |  (_)__| |_\n"
              "\t| _|| / -_) -_)  _| | |__| (_-<  _|\n"
              "\t|_| |_\___\___|\__| |____|_/__/\__|\n"
              "\n"
            "ID                Brand           Year      Price        Type       \n")
        for car in fleet_list:
            print(car)
        os.system('pause')

    def see_fleet_list_in_rent_a_car(self):
        fleet_list = self._car_service.get_fleet_list()
        os.system('cls') ##display header function instead
        print(
              "\t ___ _         _     _    _    _   \n"
              "\t| __| |___ ___| |_  | |  (_)__| |_\n"
              "\t| _|| / -_) -_)  _| | |__| (_-<  _|\n"
              "\t|_| |_\___\___|\__| |____|_/__/\__|\n"
              "\n"
            "ID                Brand           Year      Price        Type       \n")
        for car in fleet_list:
            print(car)

    def see_all_in_rental(self):
        cars_in_rental = self._car_service.get_all_in_rental()
        os.system('cls') ##display header function instead
        print(
              "\t ___ _         _     _    _    _   \n"
              "\t| __| |___ ___| |_  | |  (_)__| |_\n"
              "\t| _|| / -_) -_)  _| | |__| (_-<  _|\n"
              "\t|_| |_\___\___|\__| |____|_/__/\__|\n"
              "\n"
              "All cars now in Rental: \n"
            "ID                Brand           Year      Price        Type       \n")
        for car in cars_in_rental:
            print(car)
        os.system('pause')

    def see_all_available(self):
        cars_available = self._car_service.get_all_available()
        os.system('cls') ##display header function instead
        print(
              "\t ___ _         _     _    _    _   \n"
              "\t| __| |___ ___| |_  | |  (_)__| |_\n"
              "\t| _|| / -_) -_)  _| | |__| (_-<  _|\n"
              "\t|_| |_\___\___|\__| |____|_/__/\__|\n"
              "\n"
              "All cars now available: \n"
            "ID                Brand           Year      Price        Type       \n")
        for car in cars_available:
            print(car)
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