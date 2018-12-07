"""Service class for Cars"""
from datetime import datetime

from Repositories.CarRepository import CarRepository
from Repositories.RentalRepository import RentalRepository
from Models.Car import Car

class CarService:

    def __init__(self):
        self._car_repo = CarRepository()
        self._rental_repo = RentalRepository()

    def add_car(self, Car):
        self._car_repo.add_car(Car)

    def get_fleet_list(self):
        return self._car_repo.get_fleet_list()
        
    def get_all_in_rental(self):
        Cars_in_rental = []
        Cars = self._car_repo.get_fleet_list()
        Rentals = self._rental_repo.get_rental_list()
        today = datetime.date(datetime.now())
        for rental in Rentals:
            if today >= rental._start_date and today <= rental._end_date:
                for car in Cars:
                    if car._car_id == rental._car_id:
                        Cars_in_rental.append(car)
        return Cars_in_rental

    def get_all_available(self):
        Cars_available = self._car_repo.get_fleet_list()
        Rentals = self._rental_repo.get_rental_list()
        today = datetime.date(datetime.now())
        for rental in Rentals:
            if today >= rental._start_date and today <= rental._end_date:
                for car in Cars_available:
                    if car._car_id == rental._car_id:
                        Cars_available.remove(car)
        return Cars_available

