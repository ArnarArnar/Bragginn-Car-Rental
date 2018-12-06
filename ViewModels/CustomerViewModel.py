"""ViewModel for Rentals"""

class CustomerViewModel:
    def __init__(self, customer_id, customer_first_name, customer_last_name, 
                country, card_number):
        
        #Nota underscore tarna fyrir private breytur, samt er i raun ekkert private i Python
        self._customer_id = customer_id
        self._first_name = customer_first_name
        self._last_name = customer_last_name
        self._country = country
        self._card_number = card_number

    #Get og set foll fyrir allt vantar svo, og __str__ fall

    def __repr__(self):
        return "CustomerViewModel('{}', '{}', '{}', '{}', '{}')".format(self._customer_id, 
                                  self._first_name, self._last_name, self._country, self._card_number)

    def __str__(self):
        return '{} : {} : {} : {}'.format(self._customer_id, 
                self._first_name, self._last_name, self._country)

#GetFuntions

    def get_customer_id(self):
        return self._customer_id
    
    def get_first_name(self):
        return self._first_name
    
    def get_last_name(self):
        return self._last_name
    
    def get_country(self):
        return self._country

    def get_card_name(self):
        return self._card_number

#SetFunction

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id
    
    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name
    
    def set_country(self, country):
        self._country = country

    def set_card_name(self, card_name):
        self._card_name = card_name