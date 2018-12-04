"""Entity model for Rental"""

class Rental:

    def __init__(self, order_id, customer_id, car_id, start_date, length, total_price):
        self._order_id = order_id
        self._customer_id = customer_id
        self._car_id = car_id
        self._start_date = start_date
        self._length = length
        self._total_price = total_price

    def __repr__(self):
        return "Rental('{}', '{}', '{}', '{}', '{}', '{}')".format(self._order_id ,self._customer_id, 
                self._car_id, self._start_date, self._length, self._total_price)

    def __str__(self):
        return '{} : {} : {} : {} : {} : {}'.format(self._order_id, self._customer_id, 
                self._car_id, self._start_date, self._length, self._total_price)
                

#Need to add get and set functions for all the elements