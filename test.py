import csv
import re
from datetime import datetime

from Repositories.RentalRepository import RentalRepository
from Repositories.CarRepository import CarRepository
from Repositories.CustomerRepository import CustomerRepository
from Models.Rental import Rental
from Models.Car import Car
from Models.Customer import Customer
from ViewModels.RentalViewModel import RentalViewModel

car_repo = CarRepository()

car_id_to_check = "JZ263"

car_primary_keys = car_repo.get_primary_key()

if car_id_to_check in car_primary_keys:
    print("Bingo!")
else:
    print("no go")

