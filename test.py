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


car = Car("jz260", "Volvo", "1980", "4500", "budget")

# print(car)
#valid = False

# while not valid:
#            car_id = input("Enter car ID: ")
#            if re.match(r"[A-Z]{2}[0-9]{3}", car_id):
#                print("Valid")
#                valid = True


# date_input = input("Enter start date in the format DD/MM/YYYY ")

# start_date = datetime.date(datetime.strptime(date_input, '%d/%m/%Y'))
# rental1 = Rental("2207805389", "JZ260", datetime.date(datetime.today()), 7, 0)
# rental2 = Rental("2207805389", "JZ260", datetime.date(datetime(2019, 7, 22)), 7, 0)
# rental3 = Rental("2207805389", "JZ260", start_date, 3, 0)

# print(rental2)

def add_rental(Rental):
    rental_date = datetime.strftime(Rental._start_date, '%d %m %Y')
    with open('TestRentals.csv', 'a+', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerow([Rental._customer_id, Rental._car_id, rental_date, Rental._length, Rental._total_price])


def get_rental_list():
    __Rentals = []
    with open('TestRentals.csv') as rentals_file:
        rentals_reader = csv.reader(rentals_file, delimiter=';')
        rentals_list = list(rentals_reader)
        for row in rentals_list:
            rental_date = datetime.date(datetime.strptime(row[2], '%d %m %Y'))
            rental_order = Rental(row[0], row[1], rental_date, row[3], row[4])
            __Rentals.append(rental_order)
    return __Rentals

# add_rental(rental3)

# rental_list = get_rental_list()

# for rental in rental_list:
#    print(rental)
#_car_repo = CarRepository()
#primary_keys = _car_repo.get_primary_key()

#for key in primary_keys:
#    print(key)

_rental_repo = RentalRepository()

next1 = _rental_repo.get_next_id()

_rental_repo.add_order_id()

print(next1)


