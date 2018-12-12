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
    def is_number_valid(self, number):
        """Validates if number is valid or not"""
        try:
            int(number)
        except ValueError:
            return False
        if int(number) < 1:
            return False
        return True
    
    def is_days_valid(self, days):
        """Validates if days is valid or not"""
        try:
            int(days)
        except ValueError:
            return False
        if int(days) < 1 or int(days) > 2000:
            return False
        return True

    def is_date_valid(self, input_date):
        """Validates if date is valid or not"""
        try:
            datetime.date(datetime.strptime(input_date, '%d/%m/%Y'))
        except ValueError:
           return False
        return True

    def is_date_in_past(self, date):
        """Checks if date is in the past"""
        current_day = datetime.date(datetime.now())
        if date < current_day:
            return True
        else:
            return False

# Car input validation
    def is_car_id_valid(self, car_id):
        """Checks if car id is in valid format or not"""
        if re.match(r"[A-Z]{3}[0-9]{2}$", car_id):
            return True
        if re.match(r"[A-Z]{2}[0-9]{3}$", car_id):
            return True
        return False

    def is_year_valid(self, year):
        """Checks if year is in valid format or not, and no older then 1980"""
        try:
            int(year)
        except ValueError:
            return False
        currentYear = int(datetime.now().year)
        val = int(year)
        if val < 1980:
            return False
        if currentYear < val:
            return False
        return True

    def is_car_start_date_available(self, car_id, start_date):
        """Checks if start date for a given car is available"""
        Rentals = self._rental_repo.get_rental_list()
        Returns = self._rental_repo.get_returns_list()
        for rental in Rentals:
            if car_id == rental.get_car_id() and start_date >= rental.get_start_date() and start_date < rental.get_end_date():
                for ret in Returns:
                    if ret.get_order_id() == rental.get_order_id():
                        return True
                return False
        return True

    def is_car_end_date_available(self, car_id, start_date, days, end_date):
        """Checks if length of rent for a given car is available"""
        Rentals = self._rental_repo.get_rental_list()
        Returns = self._rental_repo.get_returns_list()
        for rental in Rentals:
            if car_id == rental.get_car_id() and end_date > rental.get_start_date() and end_date <= rental.get_end_date():
                for ret in Returns:
                    if ret.get_order_id() == rental.get_order_id():
                        return True
                return False
        return True
    
    def is_car_brand_valid(self, brand):
        """Checks if car brand name is valid"""
        if not re.match(r"[A-Za-z]{1,15}$", brand):
            return False
        else:
            return True

# Rental validation services
    def does_order_id_exist(self, order_id):
        """Checks is order id exists in the rentals database"""
        rentals_pkeys = self._rental_repo.get_rentals_primary_keys()
        if order_id in rentals_pkeys:
            return True
        else:
            return False

    def does_customer_id_exist(self, customer_id):
        """Checks if the customer exists in the database"""
        customer_pkeys = self._customer_repo.get_customer_primary_keys()
        if customer_id in customer_pkeys:
            return True
        else:
            return False

    def does_car_id_exist(self, car_id):
        """Checks if the car exists in the database"""
        car_pkeys = self._car_repo.get_car_primary_keys()
        if car_id in car_pkeys:
            return True
        else:
            return False

    def does_insurance_name_exist(self, insurance_name):
        """Checks if the insurance name exists in the database"""
        Insurances = self._rental_repo.get_insurance_list()
        for insurance in Insurances:
            if insurance.get_name() == insurance_name:
                return True
        return False

    def has_order_already_been_returned(self, order_id):
        """Checks if order has already been returned"""
        returns_pkeys = self._rental_repo.get_returns_primary_keys()
        if order_id in returns_pkeys:
            return True
        else:
            return False
    
    def is_order_in_rental(self, order_id):
        """Checks if order is currently in rental"""
        rentals = self._rental_repo.get_rental_list()
        Returns = self._rental_repo.get_returns_list()
        today = datetime.date(datetime.now())
        for rental in rentals:
            if today >= rental.get_start_date() and today <= rental.get_end_date() and rental.get_order_id() == order_id:
                for ret in Returns:
                    if ret.get_order_id() == rental.get_order_id():
                        return False
                return True
        return False

    def does_short_code_exist(self, short_code):
        """Checks if insurance short code exists in database"""
        insurance_pkeys = self._rental_repo.get_insurance_primary_keys()
        if short_code in insurance_pkeys:
            return True
        else:
            return False

    def is_short_code_valid(self, short_code):
        """Checks if short code is valid"""
        if not re.match(r"[A-Z]{1,3}$", short_code):
            return False
        else:
            return True
    
    def is_insurance_name_valid(self, name):
        """Checks if insurance name is valid"""
        if not re.match(r"[A-Za-z]{1,25}$", name):
            return False
        else:
            return True

# Customer validation services
    def is_customer_id_valid(self, customer_id):
        """Checks if customer id is valid"""
        try:
            int(customer_id)
        except ValueError:
            return False
        
        if int(customer_id) < 1:
            return False
        return True
    
    def is_word_length_valid(self, word):
        """Checks if word length is valid"""
        if not re.match(r"[A-Za-z]{1,30}$", word):
            return False
        else:
            return True

    def is_street_valid(self, street):
        """Checks if street name is valid"""
        if not re.match(r"[A-Za-z0-9 ]{1,40}$", street):
            return False
        else:
            return True

    def is_phone_valid(self, phone):
        """Checks if phone is valid"""
        if not re.match(r"[0-9]{7,12}$", phone):
            return False
        else:
            return True

    def is_zip_valid(self, zip):
        """Checks if zip is valid"""
        if not re.match(r"[0-9]{3,7}$", zip):
            return False
        else:
            return True

    def is_drivers_license_valid(self, drivers_license):
        """Checks if drivers license is valid"""
        if not re.match(r"[0-9]{7,12}$", drivers_license):
            return False
        else:
            return True

    def is_card_number_valid(self, card_number):
        """Checks if card number is valid"""
        if re.match(r"[0-9]{16}$", card_number):
            return True
        else:
            return False

    def is_expiry_valid(self, expiry):
        """Checks if expiry is valid"""
        try:
            datetime.date(datetime.strptime(expiry, '%m/%y'))
        except ValueError:
           return False
        return True

    def is_cvc_valid(self, cvc):
        """Checks if cvc is valid"""
        if not re.match(r"[0-9]{3}$", cvc):
            return False
        else:
            return True

    def does_card_exist(self, card_selected):
        """Checks if card number exists in database"""
        card_pkeys = self._customer_repo.get_credit_card_primary_keys()
        if card_selected in card_pkeys:
            return True
        else:
            return False
