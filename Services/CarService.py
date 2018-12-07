"""Service class for Cars"""
from Repositories.CarRepository import CarRepository
from Models.Car import Car

class CarService:

    def __init__(self):
        self._car_repo = CarRepository()

    def add_car(self, Car):
        self._car_repo.add_car(Car)


    def get_fleet_list(self):
        return self._car_repo.get_fleet_list()
        