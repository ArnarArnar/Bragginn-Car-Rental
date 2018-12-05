"""Entity model for Rental"""

class Rental:

    def __init__(self, order_id, customer_id, car_id, start_date, days, insurance, total_price):
        self._order_id = order_id
        self._customer_id = customer_id
        self._car_id = car_id
        self._start_date = start_date
        self._days = days
        self._insurance = insurance
        self._total_price = total_price

    def __repr__(self):
        return "Rental('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self._order_id ,self._customer_id, 
                self._car_id, self._start_date, self._days, self._insurance, self._total_price)

    def __str__(self):
        return '{:^7s} : {} : {} : {} : {} : {} : {}'.format(self._order_id, self._customer_id, 
                self._car_id, self._start_date, self._days, self._insurance, self._total_price)
                

#Need to add get and set functions for all the elements