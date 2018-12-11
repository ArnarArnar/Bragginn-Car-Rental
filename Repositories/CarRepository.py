"""Repo class for Cars"""
import csv
import os
from pathlib import Path

from Models.Car import Car

class CarRepository:

    def __init__(self):
        self.__Cars = [] #Hverjar eru nafnavenjurnar? afhverju eru 2 undirstrik her
        self._primary_keys = []

#Post functions
    def add_car(self, Car):
        with open(os.path.realpath('Data/Cars.csv'), 'a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            csv_writer.writerow([Car.get_car_id(), Car.get_brand(), Car.get_year(), Car.get_price_per_day(), Car.get_car_type()])

#Get functions
    def get_fleet_list(self):
        self.__Cars.clear()
        with open(os.path.realpath('Data/Cars.csv')) as cars_file:
            csv_reader = csv.reader(cars_file, delimiter=';')
            cars_list = list(csv_reader)
            for row in cars_list:
                fleet_car = Car(row[0], row[1], row[2], row[3], row[4])
                self.__Cars.append(fleet_car)
        return self.__Cars

    def get_car_primary_keys(self):
        self._primary_keys.clear()
        with open(os.path.realpath('Data/Cars.csv')) as cars_file:
            csv_reader = csv.reader(cars_file, delimiter=';')
            cars_list = list(csv_reader)
            for row in cars_list:
                self._primary_keys.append(row[0])
        return self._primary_keys