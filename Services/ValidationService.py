import re
from datetime import datetime

from Repositories.CarRepository import CarRepository
from Repositories.CustomerRepository import CustomerRepository

class ValidationService:

    def __init__(self):
        self._car_repo = CarRepository()
        self._customer_repo = CustomerRepository()


# General validation services
    def is_number_negative(self, number):
        # can be used for input of all integers eg. price, days etc., can not be negative
        if int(number) < 0:
            return False
        else:
            return True

    def is_date_valid(self, date):
        # Check if entered date is in the valid format DD/MM/YYYY
        current_day = datetime.now()
        try:           
            date = datetime.strptime(date, "%d/%m/%Y")
        except ValueError:
           print("This format does not match!")
           return False
        else:
            if date < current_day:
                print("The date cannot be in past")
                return False
        return True


# Order input validation
    def is_order_id_valid(self, order_id):
        try:
            val = int(order_id)
        except ValueError:
            print("That's not an int!")
            return False
        else:
            if val < 0:
                print("Negative number warning!")
                return False
        return True


# Car input validation
    def is_car_id_valid(self, car_id):
        # This is just an example, maybe we just want to limit length?
        # if re.match(r"[A-Z]{2}[0-9]{3}", car_id):
        # Needs to be valid car ID
        return True

    def is_year_valid(self, year):
        # Must be in format YYYY ex. 2018
        #try:           
        #      #re.match("%Y/", expiry):
        # except ValueError:
        #    print("This format does not match!")
        #    return False
        # return True
        return True

    def is_car_type_valid(self, car_type):
        # Can only enter the types that we decide e.g. budget, off road, luxury etc.
        return True

# Rental validation services customer_id, car_id, start_date, length, total_price
    def does_customer_id_exist(self, customer_id):
        # Here we don't need regex, need to check if it exist in the database
        customer_pkeys = self._customer_repo.get_primary_key()
        if customer_id in customer_pkeys:
            return True
        else:
            return False
        # If it does not exist we print out all customers in database
        # And the option of adding a customer in rental sub menu

    def does_car_id_exist(self, car_id):
        # Here we don't need regex, need to check if it exist in the database
        car_pkeys = self._car_repo.get_primary_key()
        if car_id in car_pkeys:
            return True
        else:
            return False
        # If it does not exist we print out all cars in database in rental sub menu

    def does_insurance_exist(self, insurance):
        return False

    def does_short_code_exist(self, short_code):
        return True

# Customer validation services
    def is_customer_id_valid(self, customer_id):
        # We need to decide what we want customer Id to be, kennitala? passport?
        # This only test if it is a negative number or not a number
        try:
            val = int(customer_id)
        except ValueError:
            print("That's not an int!")
            return False
        else:
            if val < 0:
                print("Negative number warning!")
                return False
        return True

    def is_phone_valid(self, phone):
        # Regex a valid phone number
        if not re.match(r"[0-9]{7,12}$", phone):
            return False
        return True

    def is_zip_valid(self, zip):
        # What should the validation be for this?
        if not re.match(r"[0-9]{3,7}$", zip):
            return False
        return True

    def is_drivers_license_valid(self, drivers_license):
        # This is just an example, maybe we just want to limit length?
        return True
    
    def is_card_number_valid(self, card_number):
        # Validate creditcard number
        #if re.match(r"[0-9]{16}$", card_number):
        return True

    def is_expiry_valid(self, expiry):
        # try:           
        #      #re.match("%d/%m/", expiry):
        # except ValueError:
        #    print("This format does not match!")
        #    return False
        return True

    def is_cvc_valid(self, cvc):
        # Validate cvc (3 digits) Kommentaði þetta út því ekkert komið inn til að setja in cvc þannig ótestað
        # if not re.match("[0-9]{3}$ or ^\d{3}$", cvc):
        #     print ("Error! Make sure you only use 3 digits in cvc")
        #     return False
        # else:
        return True
