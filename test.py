import csv
import re
import os
from datetime import datetime
from datetime import timedelta

from Repositories.RentalRepository import RentalRepository
from Repositories.CarRepository import CarRepository
from Repositories.CustomerRepository import CustomerRepository
from Services.CustomerService import CustomerService
from Services.RentalService import RentalService
from Models.Rental import Rental
from Models.Car import Car
from Models.Customer import Customer
from Services.ValidationService import ValidationService
from ViewModels.RentalViewModel import RentalViewModel
from UI.RentalSubMenu import RentalSubMenu
from UI.DisplayHeader import DisplayHeader


validation = ValidationService()

valid = validation.is_insurance_name_valid("123455656562")

print(valid)

