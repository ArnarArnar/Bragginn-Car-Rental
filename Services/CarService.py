"""Service class for Cars"""
from Repositories.CarRepository import CarRepository
from Models.Car import Car

class CarService:

    def __init__(self):
        self._car_repo = CarRepository()

    def add_car(self, Car):
        if self.is_car_valid(Car) == True:
            self._car_repo.add_car(Car)

    def is_car_valid(self, Car):
        #Validation check (tetta a vaentanlega heima i service layer)
        # if not carID[:2].isalpha():
        #    raise ValueError("Bilnumer byrjar a bokstofum '{}'".format(carID))
        return True

    def get_fleet_list(self):
        return self._car_repo.get_fleet_list()
        