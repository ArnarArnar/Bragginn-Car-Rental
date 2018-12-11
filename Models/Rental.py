"""Entity model for Rental"""

class Rental:

    def __init__(self, order_id, customer_id, car_id, start_date, days, insurance, total_price, end_date):
        self._order_id = order_id
        self._customer_id = customer_id
        self._car_id = car_id
        self._start_date = start_date
        self._days = days
        self._insurance = insurance
        self._total_price = total_price
        self._end_date = end_date

    def __repr__(self):
        return "Rental('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self._order_id ,self._customer_id, 
                self._car_id, self._start_date, self._days, self._insurance, self._total_price, self._end_date)

    def __str__(self):
        return '{:^7} : {} : {} : {} : {} : {} : {} : {}'.format(self._order_id, self._customer_id, 
                self._car_id, self._start_date, self._days, self._insurance, self._total_price, self._end_date)
                
#GetFunctions

    def get_order_id(self):
        return self._order_id

    def get_customer_id(self):
        return self._customer_id

    def get_car_id(self):
        return self._car_id
    
    def get_start_date(self):
        return self._start_date

    def get_days(self):
        return self._days
    
    def get_insurance(self):
        return self._insurance

    def get_total_price(self):
        return self._total_price
        
#SetFunctions

    def set_order_id(self, order_id):
        self._order_id = order_id
    
    def set_customer_id(self, customer_id):
        self._customer_id = customer_id
    
    def set_car_id(self, car_id):
        self._car_id = car_id

    def set_start_date(self, start_date):
        self._start_date = start_date
    
    def set_days(self, days):
        self._days = days
    
    def set_insurance(self, insurance):
        self._insurance = insurance

    def set_total_price(self, total_price):
        self._total_price = total_price

    