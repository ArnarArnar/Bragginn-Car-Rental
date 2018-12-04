"""Entity model for car"""

class Car:

    def __init__(self, car_id, brand, year, price_per_day, car_type):
        self._car_id = car_id
        self._brand = brand
        self._year = year
        self._price_per_day = price_per_day
        self._car_type = car_type
    
    def __repr__(self):
        return "Car('{}', '{}', '{}', '{}', '{}')".format(self._car_id, 
                self._brand, self._year, self._price_per_day, self._car_type)

    def __str__(self):
        return '{}  :   {}  :   {}  :   {}  :   {}'.format(self._car_id, 
                self._brand, self._year, self._price_per_day, self._car_type)

#Need to add get and set functions for all the elements