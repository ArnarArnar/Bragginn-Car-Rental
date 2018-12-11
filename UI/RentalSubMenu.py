import os
from datetime import datetime

from Services.RentalService import RentalService
from Services.CustomerService import CustomerService
from Services.ValidationService import ValidationService
from Models.Rental import Rental
from Models.CarReturn import CarReturn
from Models.Insurance import Insurance
from ViewModels.RentalViewModel import RentalViewModel
from UI.DisplayHeader import DisplayHeader
from UI.CustomerSubMenu import CustomerSubMenu
from UI.CarSubMenu import CarSubMenu
from UI.SystemSpecificUI import SystemSpecificUI


class RentalSubMenu:

    def __init__(self):
        self.valid = False
        self._display_header = DisplayHeader()
        self._rental_service = RentalService()
        self._customer_service = CustomerService()
        self._validation_service = ValidationService()
        self._customer_sub_menu = CustomerSubMenu()
        self._car_sub_menu = CarSubMenu()
        self._system = SystemSpecificUI()


    def rental_sub_menu(self):
        """Display's the rentals submenu"""
        self._display_header.display_header_rentals()
        print("\t1. Rent a Car \n"
              "\t2. Rental History \n"
              "\t3. Return Car \n"
              "\t4. Cancel Order \n"
              "\t5. Change Order \n"
              "\t6. See All Orders \n"
              "\t7. Add Insurance Type \n"
              "\tEnter q to quit \n")
        user_input = input('What would you like to do? ')
        # Rent a Car
        if user_input == "1":
            new_rental = self.get_rental_input()
            self._rental_service.add_rental(new_rental)
            self.see_rental_overview(new_rental)
        # Rental History
        if user_input == "2":
            self.rental_history_view()
            car_id = self.get_car_rental_history_input()
            rental_view = self._rental_service.get_car_rental_history(car_id)
            self.see_rental_view_list(rental_view)
        # Return Car
        if user_input == "3":
            car_return = self.get_return_a_car_input()
            if car_return == "q":
                print("return car cancelled")
                self._system.pause_system()
                return
            self._rental_service.add_return(car_return)
            self.see_return_overvew(car_return)
        # Cancel Order
        if user_input == "4":
            self.cancel_order_view()
            order_id = self.get_order_id_input()
            rental = self._rental_service.get_rental(order_id)
            self.cancel_order_view()
            self.see_order(rental)
            print("\n\nAre you sure you want to cancel order number " + order_id + " and delete it from the database\n\n")
            print(  "[ 1 ] Delete order from database\n"
                    "[ Q ] To exit without changes\n\n")
            user_answer = input("Please select an option: ")
            if user_answer == '1':
                self._rental_service.delete_order(order_id)
                print("Order deleted from database")
                self._system.pause_system()
            else:
                print("Order deletion cancelled ")
                self._system.pause_system()
                return
        # Change order
        if user_input == "5":
            self.change_order_view()
            order_id = self.get_order_id_input()
            rental = self._rental_service.get_rental(order_id)
            self.see_order(rental)
            change = self.get_change_order_input(rental)
            self.update_rental(change, rental)
        # See All Orders
        if user_input == "6":
            self.all_order_view()
            self._system.pause_system()
        # Add Insurance Type
        if user_input == "7":
            self.see_insurance_list()
            insurance = self.get_insurance_input()
            self._rental_service.add_insurance(insurance)

#Inputs
    def get_rental_input(self):
        self.valid = False
        while not self.valid:
            customer_id = input("Enter ID for customer: ")
            self.valid = self._validation_service.does_customer_id_exist(customer_id)
            if not self.valid:
                self._customer_sub_menu.see_customer_list()
                print("Customer does not exist, please register customer first")
        self.valid = False
        while not self.valid:
            self._car_sub_menu.see_fleet_list_in_rent_a_car()
            car_id = input("Enter ID of car to rent: ")
            self.valid = self._validation_service.does_car_id_exist(car_id)
            if not self.valid:
                print("Car does not exist")
        self.valid = False
        while not self.valid:
            start_date_input = input("Enter start date in the format DD/MM/YYYY: ")
            self.valid = self._validation_service.is_date_valid(start_date_input)
            if not self.valid:
                print("Date is not in valid format")
            start_date = datetime.date(datetime.strptime(start_date_input, '%d/%m/%Y'))
            self.valid = not self._validation_service.is_date_in_past(start_date)
            if not self.valid:
                print("Date can not be in the past")

            self.valid = self._validation_service.is_car_start_date_available(car_id, start_date)
            if not self.valid:
                print("This start date is not available for chosen car")
        self.valid = False
        while not self.valid:
            days = input("Enter how many days to rent: ")
            self.valid = self._validation_service.is_number_negative(days)
            if not self.valid:
                print("Can not rent for negative days")
                # Print a list of cars here
                self._system.pause_system()
                continue
            end_date = self._rental_service.calculate_end_date(start_date, days)
            self.valid = self._validation_service.is_car_end_date_available(car_id, start_date, days, end_date)
            if not self.valid:
                print("Car is not available for this rental period")
        self.valid = False
        self.see_insurance_list()

        insurance = input('Please enter a short code: ')
        while not self.valid:
            self.valid = self._validation_service.does_short_code_exist(insurance)
            if not self.valid:
                print("Insurance short code does not exist")
        total_price = self._rental_service.calculate_total_price(car_id, insurance, days)
        order_id = self._rental_service.get_and_set_next_order_id()
        new_rental = Rental(order_id, customer_id, car_id, start_date, days, insurance, total_price, end_date)
        return new_rental

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
            car_id = input("Enter car ID to see rental history: ")
            self.valid = self._validation_service.does_car_id_exist(car_id)
            if not self.valid:
                print("Car Id does not exist! Please enter a car ID that exists")
                # See fleet list from car service if we want
                self._system.pause_system()
        return car_id

    def get_return_a_car_input(self):
        self.return_a_car_view()
        self.valid = False
        while not self.valid:
            order_id = input("\nEnter order ID: ")
            if order_id == "q":
                return "q"
            self.valid = self._validation_service.does_order_id_exist(order_id)
            if not self.valid:
                self._car_sub_menu.see_all_in_rental()
                print("\nOrder id does not exsist")
                continue
            self.valid = not self._validation_service.has_order_already_been_returned(order_id)
            if not self.valid:
                print("Order has already been returned")
                self._system.pause_system()
        self.return_a_car_view()
        self.return_a_car_view_order_selected(order_id)
        self._system.pause_system()
        self.valid = False
        self._system.clear_screen()
        self.return_a_car_view()
        print ( "Is the Car being return late?: \n\n"
                "[ 1 ] It's right on time!\n"
                "[ 2 ] It's too late\n"
                "[ q ] Return to main menu\n")

        while not self.valid:
            return_car_user_input_is_ok = input('Please select an option: ')
            if return_car_user_input_is_ok == "1":
                self.valid = True
                days_late = 0
            if return_car_user_input_is_ok == "2":
                self.valid = True
                days_late = input("How many days late? ")
            if return_car_user_input_is_ok == "q":
                return "q"
        self.return_a_car_view()
        self.valid = False
        print ( "Is the Car OK?: \n\n"
                "[ 1 ] Yes\n"
                "[ 2 ] No, write a comment\n"
                "[ q ] Return to main menu\n")
        while not self.valid:
            return_car_user_input_is_ok = input('Please select an option: ')
            if return_car_user_input_is_ok == "1":
                self.valid = True
                return_comment = "No comment"
            if return_car_user_input_is_ok == "2":
                self.valid = True
                return_comment = input("What's wrong with the car? ")
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
            if return_car_user_input_fuel_full == "1":
                gas_level = "FULL"
                self.valid = True
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
                    how_much_fuel = input('Please select an option: ')
                    if how_much_fuel == "1":
                        gas_level = "3/4"
                    if how_much_fuel == "2":
                        gas_level = "2/4"
                    if how_much_fuel == "3":
                        gas_level = "1/4"
                    if how_much_fuel == "4":
                        gas_level = "less than 1/4"
                    self.valid = True
            if return_car_user_input_fuel_full == "q":
                return
        extra_fee = self._rental_service.calculate_extra_fee(order_id, days_late, gas_level)
        car_return = CarReturn(order_id, days_late, gas_level, return_comment, extra_fee)
        return car_return

    def get_insurance_input(self): # name, price
        self.valid = False
        while not self.valid:
            name = input("Enter name new of insurance: ")
            self.valid = not self._validation_service.does_insurance_name_exist(name)
            if not self.valid:
                print("Insurance already exists ")
                self._system.pause_system()
                self.see_insurance_list()
        self.valid = False
        while not self.valid:
            short_code = input("\nEnter short code for Insurance: ")
            self.valid = not self._validation_service.does_short_code_exist(short_code)
            if not self.valid:
                print("Short Code already exists ")
                self._system.pause_system()
                self.see_insurance_list()
        self.valid = False
        while not self.valid:
            price = input("Enter price per day for insurance: ")
            self.valid = self._validation_service.is_number_negative(price)
            if not self.valid:
                print("Car does not exist")
                # Print a list of cars here
                self.see_insurance_list()
                self._system.pause_system()
        new_insurance = Insurance(short_code, name, price)
        return new_insurance

    def get_order_id_input(self):
        self.valid = False
        while not self.valid:
            order_id = input("Please enter a order ID: ")
            self.valid = self._validation_service.does_order_id_exist(order_id)
            if not self.valid:
                self._system.clear_screen()
                print("Order ID does not exist")
                self.change_order_view_list_all()
        return order_id

    def get_order_id_input_to_cancel(self):
        self.valid = False
        while not self.valid:
            order_id = input("Please enter a order id to delete: ")
            self.valid = self._validation_service.does_order_id_exist(order_id)
            if not self.valid:
                self._system.clear_screen()
                print("Order ID does not exist")
                self.see_rental_list()
                print("\n")
        return order_id

    def get_change_order_input(self, rental):
        self._system.clear_screen()
        self.change_order_view()
        print("OderID        CustomerID CarID ..... þarf að breyta þessu view modeli: \n")
        print(rental)
        print("\n[1] Change what customer registered for the rent   [4] Change duration of the rent\n"
                "[2] Change car                                     [5] Change insurance\n"
                "[3] Change start date                              [Q] Return to main menu\n\n")
        user_input = input("What would you like to change? ")
        return user_input

    def update_rental(self, change, rental): # customer_id, car_id, start_date, days, insurance
        self.valid = False
        if change == '1': #ID
            while not self.valid:
                new_customer_id = input("Enter new ID for customer: ")
                id_valid = self._validation_service.is_customer_id_valid(new_customer_id)
                id_already_exist = not self._validation_service.does_customer_id_exist(new_customer_id)
                if id_valid and not id_already_exist:
                    self.valid = True
                    self._rental_service.update_customer_id(rental, new_customer_id)
                else:
                    print("Can not update to this value")
        elif change == '2': #car_id
            while not self.valid:
                new_car_id = input("Enter new car id: ")
                self.valid = self._validation_service.does_car_id_exist(new_car_id)
                if not self.valid:
                    print("Please enter a valid car id")
                    self._system.pause_system()
            self._rental_service.update_car_id(rental, new_car_id)
        elif change == '3': #Start_date
            while not self.valid:
                new_start_date_input = input("Enter start date in the format DD/MM/YYYY: ")
                self.valid = self._validation_service.is_date_valid(new_start_date_input)
                if not self.valid:
                    print("Date is not in valid format")
                    self._system.pause_system()
                new_start_date = datetime.date(datetime.strptime(new_start_date_input, '%d/%m/%Y'))
                self.valid = not self._validation_service.is_date_in_past(new_start_date)
                if not self.valid:
                    print("Date can not be in the past")
                    self._system.pause_system()
            self._rental_service.update_start_date(rental, new_start_date)
        elif change == '4': #days
            while not self.valid:
                new_days = input("Enter how many days to rent: ")
                self.valid = self._validation_service.is_number_negative(new_days)
                if not self.valid:
                    print("Can not rent for negative days")
                    # Print a list of cars here
                    self._system.pause_system()
            self._rental_service.update_days(rental, new_days)
        elif change == '5': #insurance
            self.valid = False
            while not self.valid:
                new_insurance = input("Enter insurance short code: ")
                self.valid = self._validation_service.does_short_code_exist(new_insurance)
                if not self.valid:
                    print("Insurance short code does not exist")
                    # Print list of available insurance
                    self._system.pause_system()
            self._rental_service.update_insurance(rental, new_insurance)

#Views
    def see_rental_list(self):
        rental_list = self._rental_service.get_rental_list()
        # Here we need a proper header in a seperate function in DisplayHeader.py
        print("\t ___         _        _   _    _    _   \n"
              "\t| _ \___ _ _| |_ __ _| | | |  (_)__| |_ \n"
              "\t|   / -_) ' \  _/ _` | | | |__| (_-<  _|\n"
              "\t|_|_\___|_||_\__\__,_|_| |____|_/__/\__|\n\n"
            "Order CustomerID   CarID    StartDate    EndDate     Ins.  Total cost")
        for rental in rental_list:
            print(rental)

    def see_rental_view_list(self, rvList): #Rental viewlist comes in
        self._system.clear_screen()
        # Here we need a proper header in a seperate function in DisplayHeader.py
        print(  "\t ___         _        _   _  _ _    _                \n"
                "\t| _ \___ _ _| |_ __ _| | | || (_)__| |_ ___ _ _ _  _ \n"
                "\t|   / -_) ' \  _/ _` | | | __ | (_-<  _/ _ \ '_| || |\n"
                "\t|_|_\___|_||_\__\__,_|_| |_||_|_/__/\__\___/_|  \_, |\n"
                "\t                                                |__/ \n\n"
        "Order  CustomerID   Name                       CarNr   Brand     Type    StartDate     EndDate     Ins.  Total cost: \n")
        for rental in rvList:
            print(rental)
        self._system.pause_system()
    
    def return_a_car_view_order_selected(self, order_id):
        
        print("Order selected for return: \n")
        print("Rental overview: \n\n"
                "Order  CustomerID   Name                       CarNr   Brand     Type    StartDate     EndDate     Ins.  Total cost: \n")
        print("hér vantar að geta séð gamla pöntun")
        print(order_id)

    def see_rental_overview(self, rental): #Rental viewlist comes in
        self._system.clear_screen()
        customer = self._customer_service.get_customer(rental._customer_id)
        credit_cards = self._customer_service.get_customer_credit_cards(rental._customer_id)
        print(  "\t  ___         _                               _            \n"
                "\t / _ \ _ _ __| |___ _ _   _____ _____ _ ___ _(_)_____ __ __\n"
                "\t| (_) | '_/ _` / -_) '_| / _ \ V / -_) '_\ V / / -_) V  V /\n"
                "\t \___/|_| \__,_\___|_|   \___/\_/\___|_|  \_/|_\___|\_/\_/ \n\n")
        print("Rental overview: \n\n"
                "Order CustomerID   CarID    StartDate    EndDate     Ins.  Total cost")
        print(rental)
        print("\nCustomer:\n\n"
                "ID           Name                              Phone           Street         Zip         Town             Country     License ")
        print(customer)
        if not credit_cards:
            print("\nCustomer has no registered credit card, please enter card: ")
            self._system.pause_system()
            new_card = self._customer_sub_menu.get_add_creditcard_input_from_rental(rental._customer_id)
            self._customer_service.add_credit_card(new_card)
            card_selected = new_card._card_number
        else:
            print("\nRegistered Credit Cards:\n")
            for card in credit_cards:
                print(card)
            while not self.valid:
                card_selected = input("Enter number of card to use: ")
                self.valid = self._validation_service.does_card_exist(card_selected)
                if not self.valid:
                    print("Please enter a number of customer credit card")
                    self._system.pause_system()


        print(  "\t ___                         _                              __      _ \n"
                "\t| _ \__ _ _  _ _ __  ___ _ _| |_   ____  _ __ __ ___ ______/ _|_  _| |\n"
                "\t|  _/ _` | || | '  \/ -_) ' \  _| (_-< || / _/ _/ -_|_-<_-<  _| || | |\n"
                "\t|_| \__,_|\_, |_|_|_\___|_||_\__| /__/\_,_\__\__\___/__/__/_|  \_,_|_|\n"
                "\t          |__/                                                        \n\n\n")
        print("\tPayment to order number " + str(rental._order_id) + " has been successfully charged to card no " + str(card_selected) + "\n\n")
        print("\tThe car with the number " + str(rental._car_id) + " will be available for pickup at " + str(rental._start_date) + "\n\n\n\n")
        self._system.pause_system()


    def see_return_overvew(self, car_return):
        self._system.clear_screen()
        rental_list = self._rental_service.get_rental_list()
        for rental in rental_list:
            if rental._order_id == car_return._order_id:
                rental_returned = rental

        customer = self._customer_service.get_customer(rental_returned._customer_id)
        credit_cards = self._customer_service.get_customer_credit_cards(rental_returned._customer_id)
        print(  "\t ___     _                    ___                  _            \n"
                "\t| _ \___| |_ _  _ _ _ _ _    / _ \__ _____ _ ___ _(_)_____ __ __\n"
                "\t|   / -_)  _| || | '_| ' \  | (_) \ V / -_) '_\ V / / -_) V  V /\n"
                "\t|_|_\___|\__|\_,_|_| |_||_|  \___/ \_/\___|_|  \_/|_\___|\_/\_/ \n\n")
        print("Rental overview: \n\n"
                "Order CustomerID   CarID    StartDate    EndDate     Ins.  Total cost")
        print(rental_returned)
        print("\nReturn information:\n")
        print("Days late    Gas level      Extra fee       Comment")
        print(car_return)
        print("\nCustomer information: \n")
        print("customerID   Name                              Phone           House          Zip            City            Country     LicenceNr")
        print(customer)
        if not credit_cards:
            print("Customer has no registered credit card, please enter card: ")
            self._system.pause_system()
            new_card = self._customer_sub_menu.get_add_creditcard_input_from_rental(rental._customer_id)
            self._customer_service.add_credit_card(new_card)
            card_selected = new_card._card_number
        else:
            print("\nRegistered Credit Cards:")
            for card in credit_cards:
                print(card)
            self.valid = False
            while not self.valid:
                card_selected = input("\nEnter number of card to use: ")
                self.valid = self._validation_service.does_card_exist(card_selected)
                if not self.valid:
                    print("\nPlease enter a number of customer credit card")
                    self._system.pause_system()
        self._system.clear_screen()
        print(  "\t ___                         _                              __      _ \n"
                "\t| _ \__ _ _  _ _ __  ___ _ _| |_   ____  _ __ __ ___ ______/ _|_  _| |\n"
                "\t|  _/ _` | || | '  \/ -_) ' \  _| (_-< || / _/ _/ -_|_-<_-<  _| || | |\n"
                "\t|_| \__,_|\_, |_|_|_\___|_||_\__| /__/\_,_\__\__\___/__/__/_|  \_,_|_|\n"
                "\t          |__/                                                        \n\n\n")
        print("     Payment to order number " + str(rental._order_id) + " has been successfully charged to card no " + str(card_selected) + "\n\n")
        print("\t\tThank you for selecting Bragginn Car rental\n\n\n\n")
        self._system.pause_system()


    def return_a_car_view(self):
        self._system.clear_screen()
        print(  "\t ___     _                     _      ___          \n"
                "\t| _ \___| |_ _  _ _ _ _ _     /_\    / __|__ _ _ _ \n"
                "\t|   / -_)  _| || | '_| ' \   / _ \  | (__/ _` | '_|\n"
                "\t|_|_\___|\__|\_,_|_| |_||_| /_/ \_\  \___\__,_|_|   \n\n"  )

    def see_insurance_list(self):
        insurance_list = self._rental_service.get_insurance_list()
        self._system.clear_screen()
        print(  "\t ___                                   \n"
                "\t|_ _|_ _  ____  _ _ _ __ _ _ _  __ ___ \n"
                "\t | || ' \(_-< || | '_/ _` | ' \/ _/ -_)\n"
                "\t|___|_||_/__/\_,_|_| \__,_|_||_\__\___|\n\n"
                "Short code      Name of insurance            Price per day\n")
        for insurance in insurance_list:
            print(insurance)


    def see_order(self, rental):
        # Here we need a proper header in a seperate function in DisplayHeader.py
        print("\tcustomerID:     carID:       startDate:      days:      total price: \n")
        print(rental)

    def cancel_order_view(self):
        self._system.clear_screen()
        print(  "\t  ___                  _    ___         _         \n"
                "\t / __|__ _ _ _  __ ___| |  / _ \ _ _ __| |___ _ _ \n"
                "\t| (__/ _` | ' \/ _/ -_) | | (_) | '_/ _` / -_) '_|\n"
                "\t \___\__,_|_||_\__\___|_|  \___/|_| \__,_\___|_|  \n")

    def change_order_view(self):
        self._system.clear_screen()
        print(  "\t  ___ _                          ___         _         \n"
                "\t / __| |_  __ _ _ _  __ _ ___   / _ \ _ _ __| |___ _ _ \n"
                "\t| (__| ' \/ _` | ' \/ _` / -_) | (_) | '_/ _` / -_) '_|\n"
                "\t \___|_||_\__,_|_||_\__, \___|  \___/|_| \__,_\___|_|  \n"
                "\t                    |___/                              \n")

    def change_order_view_list_all(self):
        rental_list = self._rental_service.get_rental_list()
        print(  "\t  ___ _                          ___         _         \n"
                "\t / __| |_  __ _ _ _  __ _ ___   / _ \ _ _ __| |___ _ _ \n"
                "\t| (__| ' \/ _` | ' \/ _` / -_) | (_) | '_/ _` / -_) '_|\n"
                "\t \___|_||_\__,_|_||_\__, \___|  \___/|_| \__,_\___|_|  \n"
                "\t                    |___/                              \n")
        for rental in rental_list:
            print(rental)

    def all_order_view(self):
        rental_list = self._rental_service.get_rental_list()
        self._system.clear_screen()
        print(  "\t   _   _ _    ___         _            \n"
                "\t  /_\ | | |  / _ \ _ _ __| |___ _ _ ___\n"
                "\t / _ \| | | | (_) | '_/ _` / -_) '_(_-<\n"
                "\t/_/ \_\_|_|  \___/|_| \__,_\___|_| /__/\n\n"
                "Order CustomerID   CarID    StartDate    EndDate     Ins.  Total cost \n")
        for rental in rental_list:
            print(rental)

    def rental_history_view(self):
        self._system.clear_screen()
        print(  "\t ___         _        _   _  _ _    _                \n"
                "\t| _ \___ _ _| |_ __ _| | | || (_)__| |_ ___ _ _ _  _ \n"
                "\t|   / -_) ' \  _/ _` | | | __ | (_-<  _/ _ \ '_| || |\n"
                "\t|_|_\___|_||_\__\__,_|_| |_||_|_/__/\__\___/_|  \_, |\n"
                "\t                                                |__/ \n\n")
