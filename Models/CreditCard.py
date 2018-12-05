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
        return '{:^12}  :   {:^12}  :   {:^8}'.format(self._card_number, 
                self._expiry, self._cvc)

#Need to add get and set functions for all the elements