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

#Get functions
    def get_car_id(self):
        return self._car_id

    def get_car_brand(self):
        return self._brand

    def get_car_year(self):
        return self._year

    def get_car_price_per_day(self):
        return self._price_per_day

    def get_car_type(self):
        return self._car_type

#Set functions
    def set_car_id(self, car_id):
        self._car_id = car_id

    def set_car_brand(self, brand):
        self._brand = brand

    def set_car_year(self, year):
        self._year = year

    def set_car_price_per_day(self, price_per_day):
        self._price_per_day = price_per_day

    def set_car_type(self, car_type):
        self._car_type = car_type