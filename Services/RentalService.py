"""Service class for Rentals"""
from datetime import datetime
from datetime import timedelta

from Repositories.RentalRepository import RentalRepository
from Repositories.CarRepository import CarRepository
from Repositories.CustomerRepository import CustomerRepository
from Models.Rental import Rental
from Models.Car import Car
from Models.Customer import Customer
from ViewModels.RentalViewModel import RentalViewModel


class RentalService:

    def __init__(self):
        self._rental_repo = RentalRepository()
        self._car_repo = CarRepository()
        self._customer_repo = CustomerRepository()

#post functions
    def add_rental(self, Rental):
        self._rental_repo.add_rental(Rental)

    def add_insurance(self, new_insurance):
        self._rental_repo.add_insurance(new_insurance)

# Get functions
    def get_rental_list(self):
        return self._rental_repo.get_rental_list()

    def get_insurance_list(self):
        return self._rental_repo.get_insurance_list()
    
    def get_car_rental_history(self, car_id):
        car_rental_history = []
        # tarf ad na i einn bil her ur grunninunum seme r med tetta carID
        customers = self._customer_repo.get_customer_list()
        rentals = self._rental_repo.get_rental_list()
        cars = self._car_repo.get_fleet_list()

        for rental in rentals:
            if rental._car_id == car_id:
                order_id = rental._order_id
                total_price = rental._total_price
                days = rental._days
                s_date = rental._start_date
                insurance = rental._insurance
                e_date = rental._end_date

                for car in cars:
                    if car._car_id == car_id:
                        car_brand = car._brand

                for customer in customers:
                    if rental._customer_id == customer._customer_id:
                        c_id = customer._customer_id
                        c_first_name = customer._first_name
                        c_last_name = customer._last_name
                
                        rental_view = RentalViewModel(order_id, c_id, c_first_name, c_last_name, car_id, 
                                                      car_brand, s_date, days, insurance, total_price, e_date)
                        car_rental_history.append(rental_view)
        return car_rental_history
    
    def get_customer_rental_history(self, customer_id):
        customer_rental_history = []
        # tarf ad na i einn bil her ur grunninunum seme r med tetta carID
        customers = self._customer_repo.get_customer_list()
        rentals = self._rental_repo.get_rental_list()
        cars = self._car_repo.get_fleet_list()

        for rental in rentals:
            if rental._customer_id == customer_id:
                order_id = rental._order_id
                total_price = rental._total_price
                days = rental._days
                s_date = rental._start_date
                insurance = rental._insurance
                car_id = rental._car_id
                e_date = rental._end_date

                for car in cars:
                    if car._car_id == car_id:
                        car_brand = car._brand

                for customer in customers:
                    if customer._customer_id == customer_id:
                        c_first_name = customer._first_name
                        c_last_name = customer._last_name
                
                        rental_view = RentalViewModel(order_id, customer_id, c_first_name, c_last_name, car_id, 
                                                      car_brand, s_date, days, insurance, total_price, e_date)
                        customer_rental_history.append(rental_view)
        return customer_rental_history
    
    def get_and_set_next_order_id(self):
        next_id = self._rental_repo.get_next_order_id()
        self._rental_repo.add_order_id(next_id)
        return next_id

    def calculate_end_date(self, start_date, days_to_add):
        end_date = start_date + timedelta(days=int(days_to_add))
        return end_date
