"""Entity model for insurance"""

class Insurance:
    
    def __init__(self, id, name, price):
        self._id = id
        self._name = name
        self._price = price
    
    def __repr__(self):
        return "Car('{}', '{}', '{}')".format(self._id, 
                self._name, self._price)

    def __str__(self):
        return '{}  :   {}  :   {}'.format(self._id, 
                self._name, self._price)

#Need to add get and set functions for all the elements