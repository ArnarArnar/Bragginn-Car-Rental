"""Entity model for insurance"""

class Insurance:
    
    def __init__(self, short_code, name, price):
        self._name = name
        self._short_code = short_code
        self._price = price
    
    def __repr__(self):
        return "Car({}', {}', '{}')".format(self._short_code, self._name, self._price)

    def __str__(self):
        return '{}  :   {}  :   {}'.format(self._short_code, self._name, self._price)

#Need to add get and set functions for all the elements

#GetFunctions

    def get_name(self):
        return self._name

    def get_short_code(self):
        return self._short_code
    
    def get_price(self):
        return self._price

#SetFunctions

    def set_name(self, name):
        self._name = name
    
    def set_short_code(self, short_code):
        self._short_code = short_code
    
    def set_price(self, price):
        self._price = price

    