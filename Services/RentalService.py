"""Service class for Rentals"""
from datetime import datetime
from datetime import timedelta

from Repositories.RentalRepository import RentalRepository
from Repositories.CarRepository import CarRepository
from Repositories.CustomerRepository import CustomerRepository
from Models.Rental import Rental
from Models.Car import Car
from Models.Customer import Customer
from Models.CarReturn import CarReturn
from ViewModels.RentalViewModel import RentalViewModel


class RentalService:

    def __init__(self):
        self._rental_repo = RentalRepository()
        self._car_repo = CarRepository()
        self._customer_repo = CustomerRepository()

#post functions
    def add_rental(self, Rental):
        self._rental_repo.add_rental(Rental)

    def add_insurance(self, new_insurance):
        self._rental_repo.add_insurance(new_insurance)

    def add_return(self, car_return):
        self._rental_repo.add_return(car_return)

    def delete_order(self, order_id_to_del):
        rentals_list = self._rental_repo.get_rental_list()
        for rental in rentals_list:
            if rental.get_order_id == order_id_to_del: #Maybe need to find a more efficient way
                rentals_list.remove(rental)
        self._rental_repo.overwrite_rentals_list(rentals_list)

# Get functions
    def get_rental_list(self):
        return self._rental_repo.get_rental_list()

    def get_rental(self, order_id):
        Rentals = self._rental_repo.get_rental_list()

        for rental in Rentals:
            if rental.get_order_id == order_id:
                rental_to_return = rental
        return rental_to_return

    def get_insurance_list(self):
        return self._rental_repo.get_insurance_list()
    
    def get_car_rental_history(self, car_id):
        car_rental_history = []
        # tarf ad na i einn bil her ur grunninunum seme r med tetta carID
        customers = self._customer_repo.get_customer_list()
        rentals = self._rental_repo.get_rental_list()
        cars = self._car_repo.get_fleet_list()

        for rental in rentals:
            if rental.get_car_id == car_id:
                order_id = rental.get_order_id
                total_price = rental.get_total_price
                days = rental.get_days
                s_date = rental.get_start_date
                insurance = rental.get_insurance
                e_date = rental.get_end_date

                for car in cars:
                    if car.get_car_id == car_id:
                        car_brand = car.get_brand
                        car_type = car.get_car_type

                for customer in customers:
                    if rental.get_customer_id == customer.get_customer_id:
                        c_id = customer.get_customer_id
                        c_first_name = customer.get_first_name
                        c_last_name = customer.get_last_name
                
                        rental_view = RentalViewModel(order_id, c_id, c_first_name, c_last_name, car_id, 
                                                      car_brand, s_date, days, insurance, total_price, e_date, car_type)
                        car_rental_history.append(rental_view)
        return car_rental_history
    
    def get_customer_rental_history(self, customer_id):
        customer_rental_history = []
        # tarf ad na i einn bil her ur grunninunum seme r med tetta carID
        customers = self._customer_repo.get_customer_list()
        rentals = self._rental_repo.get_rental_list()
        cars = self._car_repo.get_fleet_list()

        for rental in rentals:
            if rental.get_customer_id == customer_id:
                order_id = rental.get_order_id
                total_price = rental.get_total_price
                days = rental.get_days
                s_date = rental.get_start_date
                insurance = rental.get_insurance
                car_id = rental.get_car_id
                e_date = rental.get_end_date

                for car in cars:
                    if car.get_car_id == car_id:
                        car_brand = car.get_brand
                        car_type = car.get_car_type

                for customer in customers:
                    if customer.get_customer_id == customer_id:
                        c_first_name = customer.get_first_name
                        c_last_name = customer.get_last_name
                
                        rental_view = RentalViewModel(order_id, customer_id, c_first_name, c_last_name, car_id, 
                                                      car_brand, s_date, days, insurance, total_price, e_date, car_type)
                        customer_rental_history.append(rental_view)
        return customer_rental_history
    
    def get_and_set_next_order_id(self):
        next_id = self._rental_repo.get_next_order_id()
        self._rental_repo.add_order_id(next_id)
        return next_id

    def calculate_end_date(self, start_date, days_to_add):
        end_date = start_date + timedelta(days=int(days_to_add))
        return end_date

    def calculate_total_price(self, car_id, insurance_short_code, days):
        Cars = self._car_repo.get_fleet_list()
        Insurances = self._rental_repo.get_insurance_list()
        for car in Cars:
            if car.get_car_id == car_id:
                car_price = car.get_price_per_day
        for insurance in Insurances:
            if insurance.get_short_code == insurance_short_code:
                insurance_price = insurance.get_price
        
        VAT = 1.245
        total_price = (int(car_price) * int(days)) + (int(insurance_price) * int(days))
        total_price *= VAT
        return total_price

    def calculate_extra_fee(self, order_id, days_late, gas_level):
        Rentals = self._rental_repo.get_rental_list()
        Cars = self._car_repo.get_fleet_list()
        
        for rental in Rentals:
            if order_id == rental.get_order_id:
                for car in Cars:
                    if rental.get_car_id == car.get_car_id:
                        car_price = car.get_price_per_day
        
        if gas_level == "FULL":
            gas_extra = 0
        elif gas_level == "3/4":
            gas_extra = int(car_price) * 0.75
        elif gas_level == "2/4":
            gas_extra = int(car_price) * 0.5
        elif gas_level == "1/4":
            gas_extra = int(car_price) * 0.25
        elif gas_level == "less than 1/4":
            gas_extra = int(car_price)

        late_days_fee = int(car_price) * int(days_late)
        extra_fee = late_days_fee + gas_extra

        return extra_fee

#Update functions
    def update_customer_id(self, rental_to_change, new_customer_id):
        rentals_list = self._rental_repo.get_rental_list()
        for rental in rentals_list:
            if rental._order_id == rental_to_change.get_order_id:
                rental.set_customer_id(new_customer_id)
        self._rental_repo.overwrite_rentals_list(rentals_list)

    def update_car_id(self, rental_to_change, new_car_id):
        rentals_list = self._rental_repo.get_rental_list()
        for rental in rentals_list:
            if rental.get_order_id == rental_to_change.get_order_id:
                rental.set_car_id(new_car_id)
        self._rental_repo.overwrite_rentals_list(rentals_list)

    def update_start_date(self, rental_to_change, new_start_date):
        rentals_list = self._rental_repo.get_rental_list()
        for rental in rentals_list:
            if rental.get_order_id == rental_to_change.get_order_id:
                rental.set_start_date(new_start_date)
                rental.set_end_date(self.calculate_end_date(new_start_date, rental.get_days))
        self._rental_repo.overwrite_rentals_list(rentals_list)

    def update_days(self, rental_to_change, new_days):
        rentals_list = self._rental_repo.get_rental_list()
        for rental in rentals_list:
            if rental._order_id == rental_to_change._order_id:
                rental.set_days(new_days)
                rental.set_end_date(self.calculate_end_date(rental.get_start_date, new_days))
                rental.set_total_price(self.calculate_total_price(rental.get_car_id, rental.get_insurance, new_days))
        self._rental_repo.overwrite_rentals_list(rentals_list)

    def update_insurance(self, rental_to_change, new_insurance):
        rentals_list = self._rental_repo.get_rental_list()
        for rental in rentals_list:
            if rental._order_id == rental_to_change._order_id:
                rental.set_insurance(new_insurance)
                rental.set_total_price(self.calculate_total_price(rental.get_car_id, new_insurance, rental.get_days))
        self._rental_repo.overwrite_rentals_list(rentals_list)
