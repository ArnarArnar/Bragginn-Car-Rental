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
        """Sends a Car object to the repo layer to add to database"""
        self._car_repo.add_car(Car)

    def get_fleet_list(self):
        """Gets list of cars from repo layer and sends to service layer"""
        return self._car_repo.get_fleet_list()
        
    def get_all_in_rental(self):
        """Gets all cars that are currently in rental"""
        Cars_in_rental = []
        Cars = self._car_repo.get_fleet_list()
        Rentals = self._rental_repo.get_rental_list()
        Returns = self._rental_repo.get_returns_list()
        today = datetime.date(datetime.now())
        for rental in Rentals:
            if today >= rental.get_start_date() and today <= rental.get_end_date():
                for car in Cars:
                    if car.get_car_id() == rental.get_car_id():
                        Cars_in_rental.append(car)
                        for ret in Returns:
                            if ret.get_order_id() == rental.get_order_id():
                                Cars_in_rental.remove(car)
        return Cars_in_rental

    def get_all_available(self):
        """Gets all cars that are currently available"""
        Cars_available = self._car_repo.get_fleet_list()
        Rentals = self._rental_repo.get_rental_list()
        today = datetime.date(datetime.now())
        for rental in Rentals:
            if today >= rental.get_start_date() and today <= rental.get_end_date():
                for car in Cars_available:
                    if car.get_car_id() == rental.get_car_id():
                        Cars_available.remove(car)
        return Cars_available

