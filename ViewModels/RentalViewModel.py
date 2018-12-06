"""ViewModel for Rentals"""

class RentalViewModel:
    #Einskonar constructor, er samt u raun ad configure object sem er nu tegar til
    #Heitir initializer
    def __init__(self, order_id, customer_id, customer_first_name, customer_last_name, 
                car_id, car_brand, start_date, days, insurance, total_price):
        
        #Nota underscore tarna fyrir private breytur, samt er i raun ekkert private i Python
        self._order_id = order_id
        self._customer_id = customer_id
        self._first_name = customer_first_name
        self._last_name = customer_last_name
        self._car_id = car_id
        self._car_brand = car_brand
        self._start_date = start_date
        self._days = days
        self._insurance = insurance
        self._total_price = total_price

    #Get og set foll fyrir allt vantar svo, og __str__ fall

    def __repr__(self):
        return "RentalViewModel('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                self._order_id, self._customer_id, self._first_name, self._last_name, self._car_id, 
                self._car_brand, self._start_date, self._days, self._insurance, self._total_price)

    def __str__(self):
        return '{} : {} : {} : {} : {} : {} : {} : {} : {}  : {}'.format(
                self._order_id, self._customer_id, self._first_name, self._last_name, self._car_id, 
                self._car_brand, self._start_date, self._days, self._insurance, self._total_price)


#GetFunctions

    def get_order_id(self):
        return self._order_id
    
    def get_customer_id(self):
        return self._customer_id
    
    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_car_id(self):
        return self._car_id
    
    def get_car_brand(self):
        return self._car_brand
    
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
    
    def set_first_name(self, first_name):
        self._first_name = first_name
    
    def set_last_name(self, last_name):
        self._last_name = last_name
    
    def set_car_id(self, car_id):
        self._car_id = car_id
    
    def set_car_brand(self, car_brand):
        self._car_brand = car_brand
    
    def set_start_date(self, start_date):
        self._start_date = start_date

    def set_days(self, days):
        self._days = days
    
    def set_insurance(self, insurance):
        self._insurance = insurance
    
    def set_total_price(self, total_price):
        self._total_price = total_price
