"""Entity model for credit cards"""

class CreditCard:
    
    def __init__(self, customer_id, card_number, expiry, cvc):
        self._customer_id = customer_id
        self._card_number = card_number
        self._expiry = expiry
        self._cvc = cvc
    
    def __repr__(self):
        return "CreditCard('{}', '{}', '{}', '{}')".format(self._customer_id, 
                self._card_number, self._expiry, self._cvc)

    def __str__(self):
        return '{:^12}  |  {:^12}  |   {:^8}'.format(self._card_number, 
                self._expiry, self._cvc)

#Need to add get and set functions for all the elements

#GetFunctions

    def get_customer_id(self):
        return self._customer_id
    
    def get_card_number(self):
        return self._card_number

    def get_expiry(self):
        return self._expiry
    
    def get_cvc(self):
        return self._cvc
    
#SetFunctions

    def set_cutomer_id(self, customer_id):
        self._customer_id = customer_id

    def set_card_number(self, card_number):
        self._card_number = card_number

    def set_expiry(self, expiry):
        self._expiry = expiry

    def set_cvc(self, cvc):
        self._cvc = cvc

        
    