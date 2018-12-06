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
        return '{:<10} : {:<10}  {:<15} : {:^13} : {:^15} : {:^5} : {:^15} : {:^10} : {:^5}'.format(self._customer_id, 
                self._first_name, self._last_name, self._phone, self._street, self._zip, self._town,
                self._country, self._drivers_license)

#Need to add get and set functions for all the elements

#GetFunctions

    def get_customer_id(self):
        return self._customer_id
    
    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name
    
    def get_phone(self):
        return self._phone
    
    def get_street(self):
        return self._street
    
    def get_zip(self):
        return self._zip
    
    def get_town(self):
        return self._town
    
    def get_country(self):
        return self._country
    
    def get_drivers_license(self):
        return self._drivers_license

#SetFunctions

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id
    
    def set_first_name(self, first_name):
        self._first_name = first_name
    
    def set_last_name(self, last_name):
        self._last_name = last_name
    
    def set_phone(self, phone):
        self._phone = phone
    
    def set_street(self, street):
        self._street = street
    
    def set_zip(self, zip):
        self._zip = zip
    
    def set_town(self, town):
        self._town = town

    def set_country(self, country):
        self._country = country
    
    def set_drivers_license(self, drivers_license):
        self._drivers_license = drivers_license
