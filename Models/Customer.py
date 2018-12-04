"""Entity model for Customer"""

class Customer:

    def __init__(self, customer_id, first_name, last_name, phone, street, zip, town, country, drivers_license):
        self._customer_id = customer_id
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._street = street
        self._zip = zip
        self._town = town
        self._country = country
        self._drivers_license = drivers_license

    def __repr__(self):
        return "Customer('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self._customer_id, 
                self._first_name, self._last_name, self._phone, self._street, self._zip, self._town,
                self._country, self._drivers_license)

    def __str__(self):
        return '{} : {} : {} : {} : {} : {} : {} : {} : {}'.format(self._customer_id, 
                self._first_name, self._last_name, self._phone, self._street, self._zip, self._town,
                self._country, self._drivers_license)

#Need to add get and set functions for all the elements