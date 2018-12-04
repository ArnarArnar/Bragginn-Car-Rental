"""Service class for Rentals"""
from Repositories.RentalRepository import RentalRepository
from Repositories.CarRepository import CarRepository
from Repositories.CustomerRepository import CustomerRepository
from Models.Rental import Rental
from Models.Car import Car
from Models.Customer import Customer
from ViewModels.RentalViewModel import RentalViewModel

class RentalService:

    def __init__(self):
        self._rental_repo = RentalRepository()
        self._car_repo = CarRepository()
        self._customer_repo = CustomerRepository()


    def add_rental(self, Rental):
        if self.is_rental_valid(Rental) == True:
            self._rental_repo.add_rental(Rental)

    def is_rental_valid(self, Rental):
        #Validation check
        return True

    def get_rental_list(self):
        return self._rental_repo.get_rental_list()
    
    def get_car_rental_history(self, car_id):
        car_rental_history = []
        # tarf ad na i einn bil her ur grunninunum seme r med tetta carID
        customers = self._customer_repo.get_customer_list()
        rentals = self._rental_repo.get_rental_list()

        for rental in rentals:
            if rental._car_id == car_id:
                order_id = rental._order_id
                total_price = rental._total_price
                length = rental._length
                s_date = rental._start_date

                for customer in customers:
                    if rental._customer_id == customer._customer_id:
                        c_id = customer._customer_id
                        c_first_name = customer._first_name
                        c_last_name = customer._last_name
                
                        rental_view = RentalViewModel(order_id, c_id, c_first_name, c_last_name, car_id, "Volvo", s_date, length, total_price)
                        car_rental_history.append(rental_view)
        return car_rental_history
    
    def get_and_set_next_order_id(self):
        next_id = self._rental_repo.get_next_order_id()
        self._rental_repo.add_order_id(next_id)
        return
