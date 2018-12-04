import re
from datetime import datetime

class ValidationService:

# General validation services
    def is_number_negative(self, number):
        # can be used for input of all integers eg. price, days etc., can not be negative
        if number < 0:
            return False
        else:
            return True
    
    def is_date_valid(self, date):
        # Check if entered date is in the valid format DD/MM/YYYY
        current_day = datetime.now()
        date = datetime.strptime(date, "%d/%m/%Y")
        if date < current_day:
            return False
        else:
            return True

# Car input validation
    def is_car_id_valid(self, car_id):
        # This is just an example, maybe we just want to limit length?
        if re.match(r"[A-Z]{2}[0-9]{3}", car_id):
            return True
        else:
            return False
    
    def is_year_valid(self, year):
        # Must be in format YYYY ex. 2018
        return True

    def is_car_type_valid(self, car_type):
        # Can only enter the types that we decide e.g. budget, off road, luxury etc.
        return True

# Rental validation services customer_id, car_id, start_date, length, total_price
    def does_customer_id_exist(self, customer_id):
        # Here we don't need regex, need to check if it exist in the database
        # If it does not exist we print out all customers in database
        # And the option of adding a customer maybe
        return True

    def does_car_id_exist(self, car_id):
        # Here we don't need regex, need to check if it exist in the database
        # If it does not exist we print out all cars in database
        return True

# Customer validation services
    def is_customer_id_valid(self, customer_id):
        # We need to decide what we want customer Id to be, kennitala? passport?
        return True

    def is_phone_valid(self, phone):
        # Regex a valid phone number
        return True

    def is_zip_valid(self, zip):
        # What should the validation be for this?
        return True

    



