import os

from UI.CarSubMenu import CarSubMenu
from UI.CustomerSubMenu import CustomerSubMenu
from UI.RentalSubMenu import RentalSubMenu
from UI.DisplayHeader import DisplayHeader


class MainMenu:
    
    def __init__(self):
        self._display_header = DisplayHeader()
        self._car_sub_menu = CarSubMenu()
        self._rental_sub_menu = RentalSubMenu()
        self._customer_sub_menu = CustomerSubMenu()
        
#Main menu 
    def main_menu(self):
        """Display's the main menu"""
        while (input != "q" and input != "Q"):
            self._display_header.display_header()
            print("\t1. Rentals \n"
                  "\t2. Fleet \n"
                  "\t3. Customer \n"
                  "\tEnter q to quit \n")  #Need to fix a quit function so it actually exits the program
            user_input = input('What would you like to do? ')

            if user_input == "1":
                self._rental_sub_menu.rental_sub_menu()
            if user_input == "2":
                self._car_sub_menu.car_sub_menu()
            if user_input == "3":
                self._customer_sub_menu.customer_sub_menu()
            if user_input == "q" or user_input == "Q":
                print("Thank you come again")
                return

