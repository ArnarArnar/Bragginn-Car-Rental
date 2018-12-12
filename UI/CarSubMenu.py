import os

from Services.CarService import CarService
from Services.RentalService import RentalService
from Services.ValidationService import ValidationService
from Models.Car import Car
from UI.DisplayHeader import DisplayHeader
from UI.SystemSpecificUI import SystemSpecificUI


class CarSubMenu:

    def __init__(self):
        self.valid = False
        self._display_header = DisplayHeader()
        self._car_service = CarService()
        self._rental_service = RentalService()
        self._validation_service = ValidationService()
        self._system = SystemSpecificUI()

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
            self._system.pause_system()
        # See All in Rental
        if user_input == "2":
            self.see_all_in_rental()
            self._system.pause_system()
        # See All Available Cars
        if user_input == "3":
            self.see_all_available()
            self._system.pause_system()
        # Add Car
        if user_input == "4":
            self._system.clear_screen()
            self.add_car_view()
            new_car = self.get_add_car_input()
            if new_car == "q":
                print("Adding new car to fleet cancelled")
                self._system.pause_system()
                return
            self._car_service.add_car(new_car)
        # See Car History
        if user_input == "5":
            self._system.clear_screen()
            self.see_car_history_veiw()
            car_id = self.get_car_rental_history_input()
            if car_id == "q":
                return
            rental_view = self._rental_service.get_car_rental_history(car_id)
            self.see_rental_view_list(rental_view)

#Inputs
    def get_add_car_input(self):
        self.valid = False
        while not self.valid:
            car_id = input("Enter car ID (AAADD if older car AADDD): ")
            if car_id == "q":
                return car_id
            self.valid = self._validation_service.is_car_id_valid(car_id)
            if not self.valid:
                print("Invalid input!")
                continue
            self.valid = not self._validation_service.does_car_id_exist(car_id)
            if not self.valid:
                print("Car Id already exists")
        while not self.valid:
            brand = input("Enter car brand: ")
            if brand == "q":
                return brand
            self.valid = self._validation_service.is_car_brand_valid(brand)
            if not self.valid:
                print("Invalid input! Brand name cannot be longer then 15 letters")
        self.valid = False
        while not self.valid:
            year = input("The cars production year (YYYY): ")
            if year == "q":
                return year
            self.valid = self._validation_service.is_year_valid(year)
            if not self.valid:
                print("Year needs to be in the format (YYYY), not older then 1980 and of course cannot be in the future")
        self.valid = False
        while not self.valid:
            price_per_day = input("Enter price per day: ")
            if price_per_day == "q":
                return price_per_day
            self.valid = self._validation_service.is_number_valid(price_per_day)
            if not self.valid:
                print("Invalid input!")
        self.valid = False
        print ( "Please select insurance: \n\n"
            "[ 1 ] Budget\n"
            "[ 2 ] Family\n"
            "[ 3 ] Jeep\n"
            "[ 4 ] Luxury\n")
        while not self.valid:
            car_type = input("Enter car type: ")
            if car_type == "q":
                return car_type
            if car_type == "1":
                car_type = "Budget"
                self.valid = True
            if car_type == "2":
                car_type = "Family"
                self.valid = True
            if car_type == "3":
                car_type = "Jeep"
                self.valid = True
            if car_type == "4":
                car_type = "Luxury"
                self.valid = True
            if not self.valid:
                print("Car type can only be one of 4 types (Jeep, Luxury, Budget, Family")
                continue
        new_car = Car(car_id, brand, year, price_per_day, car_type)
        self._system.clear_screen()
        self.add_car_view()
        print("New car registered \n\n"
        "Car name:        " + car_id + "\n" 
        "Car brand:       " + brand + "\n"
        "Production year: " + str(year) + "\n"
        "Price per day:   " + str(price_per_day) + "\n"
        "Car type:        " + car_type + "\n")
        self._system.pause_system()
        return new_car

    def get_car_id_input(self):
        self.valid = False
        while not self.valid:
            car_id = input("Enter car ID (AADDD): ")
            self.valid = self._validation_service.is_car_id_valid(car_id)
            if not self.valid:
                print("Car Id can not be longer then X ")
                self._system.pause_system()
                continue
            self.valid = not self._validation_service.does_car_id_exist(car_id)
            if not self.valid:
                print("Car Id already exists")
                self._system.pause_system()
        return car_id
    
    def get_car_rental_history_input(self):
        self.valid = False
        while not self.valid:
            car_id = input("\nEnter car ID to see rental history: ")
            if car_id == "q":
                return "q"
            self.valid = self._validation_service.does_car_id_exist(car_id)
            if not self.valid:
                self.see_fleet_list()
                print("Car Id does not exist! Please enter a car ID that exists")
        return car_id

#Views
    def see_fleet_list(self):
        fleet_list = self._car_service.get_fleet_list()
        self._system.clear_screen() ##display header function instead
        print(
              "\t ___ _         _     _    _    _   \n"
              "\t| __| |___ ___| |_  | |  (_)__| |_\n"
              "\t| _|| / -_) -_)  _| | |__| (_-<  _|\n"
              "\t|_| |_\___\___|\__| |____|_/__/\__|\n"
              "\n"
            "CarNr          Brand           Type       Year      Price     \n")
        for car in fleet_list:
            print(car)

    def see_fleet_list_in_rent_a_car(self):
        fleet_list = self._car_service.get_fleet_list()
        self._system.clear_screen() ##display header function instead
        print(
              "\t ___ _         _     _    _    _   \n"
              "\t| __| |___ ___| |_  | |  (_)__| |_\n"
              "\t| _|| / -_) -_)  _| | |__| (_-<  _|\n"
              "\t|_| |_\___\___|\__| |____|_/__/\__|\n"
              "\n"
            "CarNr          Brand           Type       Year      Price     \n")
        for car in fleet_list:
            print(car)

    def see_all_in_rental(self):
        cars_in_rental = self._car_service.get_all_in_rental()
        self._system.clear_screen() ##display header function instead
        print(
              "\t ___ _         _     _    _    _   \n"
              "\t| __| |___ ___| |_  | |  (_)__| |_\n"
              "\t| _|| / -_) -_)  _| | |__| (_-<  _|\n"
              "\t|_| |_\___\___|\__| |____|_/__/\__|\n"
              "\n"
              "All cars now in Rental: \n\n"
            "CarNr          Brand           Type       Year      Price     ")
        for car in cars_in_rental:
            print(car)

    def see_all_available(self):
        cars_available = self._car_service.get_all_available()
        self._system.clear_screen() ##display header function instead
        print(
              "\t ___ _         _     _    _    _   \n"
              "\t| __| |___ ___| |_  | |  (_)__| |_\n"
              "\t| _|| / -_) -_)  _| | |__| (_-<  _|\n"
              "\t|_| |_\___\___|\__| |____|_/__/\__|\n"
              "\n"
              "All cars now available: \n"
            "CarNr          Brand           Type       Year      Price     \n")
        for car in cars_available:
            print(car)
    def see_car_history_veiw(self):
        print(  "\t  ___            _  _ _    _                \n" 
                "\t / __|__ _ _ _  | || (_)__| |_ ___ _ _ _  _ \n" 
                "\t| (__/ _` | '_| | __ | (_-<  _/ _ \ '_| || |\n" 
                "\t \___\__,_|_|   |_||_|_/__/\__\___/_|  \_, |\n" 
                "\t                                       |__/ \n\n")

    def see_rental_view_list(self, rvList): #Rental viewlist comes in
        self._system.clear_screen()
        # Here we need a proper header in a seperate function in DisplayHeader.py
        print(  "\t  ___            _  _ _    _                \n" 
                "\t / __|__ _ _ _  | || (_)__| |_ ___ _ _ _  _ \n" 
                "\t| (__/ _` | '_| | __ | (_-<  _/ _ \ '_| || |\n" 
                "\t \___\__,_|_|   |_||_|_/__/\__\___/_|  \_, |\n" 
                "\t                                       |__/ \n\n"              
                "Order  CustomerID   Name                       CarNr   Brand             Type       StartDate    EndDate      Ins.  Total cost: ")
        for rental in rvList:
            print(rental)
        print("\n\n\n\n")
        self._system.pause_system()
        
    def add_car_view(self): #Rental viewlist comes in
        print(  "\t   _      _    _    ___          \n"
                "\t  /_\  __| |__| |  / __|__ _ _ _ \n"
                "\t / _ \/ _` / _` | | (__/ _` | '_|\n"
                "\t/_/ \_\__,_\__,_|  \___\__,_|_|  \n\n" )