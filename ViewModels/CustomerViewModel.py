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