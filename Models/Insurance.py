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