import csv
import re
from datetime import datetime

from Repositories.RentalRepository import RentalRepository
from Repositories.CarRepository import CarRepository
from Repositories.CustomerRepository import CustomerRepository
from Services.CustomerService import CustomerService
from Models.Rental import Rental
from Models.Car import Car
from Models.Customer import Customer
from Services.ValidationService import ValidationService
from ViewModels.RentalViewModel import RentalViewModel
from UI.RentalSubMenu import RentalSubMenu
from UI.DisplayHeader import DisplayHeader

"""
car_repo = CarRepository()

car_id_to_check = "JZ263"

car_primary_keys = car_repo.get_primary_key()

if car_id_to_check in car_primary_keys:
    print("Bingo!")
else:
    print("no go")

sverrir_validation = ValidationService()

number = 12

TrueOrFalse = sverrir_validation.is_number_negative(number)

print(TrueOrFalse) 

# Dagur test
# rental_sub = RentalSubMenu()

# rental_sub.see_insurance_list()

customer_repo = CustomerRepository()
customer_list = customer_repo.get_customer_list()

def add_customer_list(customer_list):
    with open('TestCustomers.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            for customer in customer_list:
                csv_writer.writerow([customer._customer_id, customer._first_name, customer._last_name,
                                    customer._phone, customer._street, customer._zip, customer._town, 
                                    customer._country, customer._drivers_license])

add_customer_list(customer_list) 
customer_service = CustomerService()

customer_to_del = "2006814019"

customer_service.delete_customer(customer_to_del)

display = DisplayHeader()

display.display_header_fleet()
display.display_header_fleet() """



