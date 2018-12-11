import re
from datetime import datetime

from Repositories.CarRepository import CarRepository
from Repositories.CustomerRepository import CustomerRepository
from Repositories.RentalRepository import RentalRepository

class ValidationService:

    def __init__(self):
        self._car_repo = CarRepository()
        self._customer_repo = CustomerRepository()
        self._rental_repo = RentalRepository()

# General validation services
    def is_number_negative(self, number):
        # can be used for input of all integers eg. price, days etc., can not be negative
        if int(number) < 0:
            return False
        else:
            return True

    def is_date_valid(self, input_date):
        # Check if entered date is in the valid format DD/MM/YYYY
        try:           
            #date = datetime.date(datetime.strptime(date, "%d/%m/%Y"))
            datetime.date(datetime.strptime(input_date, '%d/%m/%Y'))
        except ValueError:
           return False
        return True

    def is_date_in_past(self, date):
        current_day = datetime.date(datetime.now())
        if date < current_day:
            return True
        else:
            return False


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
        if not re.match(r"[A-Z]{2,3}[0-9]{2,3}", car_id):
            return False
        # Needs to be valid car ID
        return True

    def is_year_valid(self, year):
        #Must be in format YYYY ex. 2018
        currentYear = int(datetime.now().year)
        val = int(year)
        if val < 1980:
            return False
        if currentYear < val:
            return False  
        return True

    def is_car_type_option_valid(self, car_type):
        if car_type == "1" or car_type == "2" or car_type == "3" or car_type == "3":
            return True

    #Má mögulega henda vegna þess að tékkið hér að ofan ætti að vera nóg.
    def is_car_type_valid(self, car_type):
        # Can only enter the types that we decide e.g. budget, off road, luxury etc.
        return True

    def is_car_start_date_available(self, car_id, start_date):
        Rentals = self._rental_repo.get_rental_list()
        for rental in Rentals:
            if car_id == rental._car_id and start_date >= rental._start_date and start_date <= rental._end_date:
                return False
        return True
    
    def is_car_end_date_available(self, car_id, start_date, days, end_date):
        Rentals = self._rental_repo.get_rental_list()
        for rental in Rentals:
            if car_id == rental._car_id and end_date >= rental._start_date and end_date <= rental._end_date:
                return False
        return True

# Rental validation services
    def does_order_id_exist(self, order_id):
        rentals_pkeys = self._rental_repo.get_rentals_primary_keys()
        if order_id in rentals_pkeys:
            return True
        else:
            return False

    def does_customer_id_exist(self, customer_id):
        # Here we don't need regex, need to check if it exist in the database
        customer_pkeys = self._customer_repo.get_customer_primary_keys()
        if customer_id in customer_pkeys:
            return True
        else:
            return False
        # If it does not exist we print out all customers in database
        # And the option of adding a customer in rental sub menu

    def does_car_id_exist(self, car_id):
        # Here we don't need regex, need to check if it exist in the database
        car_pkeys = self._car_repo.get_car_primary_keys()
        if car_id in car_pkeys:
            return True
        else:
            return False
        # If it does not exist we print out all cars in database in rental sub menu

    def does_insurance_name_exist(self, insurance_name):
        Insurances = self._rental_repo.get_insurance_list()
        for insurance in Insurances:
            if insurance._name == insurance_name:
                return True
        return False

    def has_order_already_been_returned(self, order_id):
        returns_pkeys = self._rental_repo.get_returns_primary_keys()  
        if order_id in returns_pkeys:
            return True
        else:
            return False

    def does_short_code_exist(self, short_code):
        insurance_pkeys = self._rental_repo.get_insurance_primary_keys()
        if short_code in insurance_pkeys:
            return True
        else:
            return False

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

    def does_card_exist(self, card_selected):
        card_pkeys = self._customer_repo.get_credit_card_primary_keys()
        if card_selected in card_pkeys:
            return True
        else:
            return False
